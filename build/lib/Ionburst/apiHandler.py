import requests
import json
from .objdict import objdict

class APIHandler:
    def __init__(self, settings):
        self.ionburst_id = settings.ionburst_id
        self.ionburst_key = settings.ionburst_key
        self.ionburst_uri = settings.ionburst_uri
        self.idToken = None
        self.refreshToken = None
        if self.ionburst_uri and not self.ionburst_uri.endswith('/'):
            self.ionburst_uri = self.ionburst_uri + '/'

    def GetJWT(self):
        req = {
            'Username': self.ionburst_id
        }
        if self.refreshToken:
            req['refreshToken'] = self.refreshToken
        else:
            req['Password'] = self.ionburst_key
        try:
            res = requests.post('{}api/signin'.format(self.ionburst_uri), data=json.dumps(req), headers={'Content-Type': 'application/json'})
            if res.status_code is 200:
                content = res.json()
                self.idToken = content['idToken']
                self.refreshToken = content['refreshToken']
            return res
        except requests.exceptions.RequestException as e:
            return e
        
    def downloadData(self, id, deferred = False, depth = 0):
        if not id:
            return objdict({ 'status_code': 400, 'reason': 'id must be specified to download data', 'text': '' })
        url = '{}api/data/deferred/start/{}'.format(self.ionburst_uri, id) if deferred else '{}api/data/{}'.format(self.ionburst_uri, id)
        try:
            res = requests.get(url,headers={
                'Authorization':'Bearer {}'.format(self.idToken),
                'Content-Type':'application/octet-stream'
            })
            return res
        except requests.exceptions.RequestException as e:
            if e.response.status_code is 401 and not depth:
                response = self.GetJWT()
                if response.status_code is not 200:
                    return response
                return self.downloadData(id, deferred, 1)
            return e

    def uploadData(self, request, deferred = False, depth = 0):
        if 'id' not in request:
            return objdict({ 'status_code': 400, 'reason': 'id must be specified in parameter!', 'text':''})
        if 'data' not in request:
            return objdict({ 'status_code': 400, 'reason': 'data must be specified in parameter!', 'text':'' })
        url = '{}api/data/deferred/start/{}'.format(self.ionburst_uri, request['id']) if deferred else '{}api/data/{}'.format(self.ionburst_uri, request['id'])
        if 'classstr' in request:
            url += '?classstr={}'.format(request['classstr'])
        try:
            res = requests.post(url,data=request['data'],headers={
                'Authorization':'Bearer {}'.format(self.idToken),
                'Content-Type':'application/octet-stream',
                'Content-Length': str(len(request['data']))
            })
            return res
        except requests.exceptions.RequestException as e:
            if e.response.status_code is 401 and not depth:
                response = self.GetJWT()
                if response.status_code is not 200:
                    return response
                return self.uploadData(request, deferred, 1)
            return e

    def deleteData(self, id, deferred = False, depth = 0):
        if not id:
            return objdict({ 'status_code': 400, 'reason': 'id must be specified in parameter!', 'text':'' })
        try:
            res = requests.delete('{}api/data/{}'.format(self.ionburst_uri, id),headers={
                'Authorization':'Bearer {}'.format(self.idToken),
                'Content-Type':'application/octet-stream'
            })
            return res
        except requests.exceptions.RequestException as e:
            if e.response.status_code is 401 and not depth:
                response = self.GetJWT()
                if response.status_code is not 200:
                    return response
                return self.deleteData(id, deferred, 1)
            return e

    def classifications(self):
        try:
            res = requests.get('{}api/Classification'.format(self.ionburst_uri),headers={
                'Content-Type':'application/json'
            })
            return res
        except requests.exceptions.RequestException as e:
            return e

    def checkDeferred(self, token, depth = 0):
        if not token:
            return objdict({ 'status_code': 400, 'reason': 'token must be specified to download data', 'text': '' })
        try:
            res = requests.get('{}api/data/deferred/check/{}'.format(self.ionburst_uri, token),headers={
                'Authorization':'Bearer {}'.format(self.idToken),
                'Content-Type':'application/json'
            })
            return res
        except requests.exceptions.RequestException as e:
            if e.response.status_code is 401 and not depth:
                response = self.GetJWT()
                if response.status_code is not 200:
                    return response
                return self.checkDeferred(token, 1)
            return e

    def fetch(self, token, depth = 0):
        if not token:
            return objdict({ 'status_code': 400, 'reason': 'Deferred token must be specified to download data', 'text': '' })
        try:
            res = requests.get('{}api/data/deferred/fetch/{}'.format(self.ionburst_uri, token),headers={
                'Authorization':'Bearer {}'.format(self.idToken),
                'Content-Type':'application/octet-stream'
            })
            return res
        except requests.exceptions.RequestException as e:
            if e.response.status_code is 401 and not depth:
                response = self.GetJWT()
                if response.status_code is not 200:
                    return response
                return self.fetch(token, 1)
            return e