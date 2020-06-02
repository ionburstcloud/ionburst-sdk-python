from .settings import Settings
from .apiHandler import APIHandler

class Ionburst:

    def __init__(self, server_url = None):
        self.settings = Settings(server_url)
        self.__apihandler = APIHandler(self.settings)
    
    def __check_token(self):
        if not self.settings.ionburst_id:
            raise ValueError('ionburst_id is not specified!')
        if not self.settings.ionburst_key:
            raise ValueError('ionburst_key is not specified!')
        if not self.settings.ionburst_uri:
            raise ValueError('ionburst_uri is not specified!')
        if not self.__apihandler.idToken:
            res = self.__apihandler.GetJWT()
            if res.status_code is not 200:
                raise SyntaxError('{}, status: {}. {}'.format(res.reason, res.status_code, res.text))

    def get(self, id = None):
        self.__check_token()
        res = self.__apihandler.downloadData(id)
        if res.status_code is 200:
            return res.content
        else:
            raise SyntaxError('{}, status: {}. {}'.format(res.reason, res.status_code, res.text))

    def put(self, request = {}):
        self.__check_token()
        res = self.__apihandler.uploadData(request)
        if res.status_code is 200:
            return res.text
        else:
            raise SyntaxError('{}, status: {}. {}'.format(res.reason, res.status_code, res.text))

    def delete(self, id =  None):
        self.__check_token()
        res = self.__apihandler.deleteData(id)
        if res.status_code is 200:
            return res.text
        else:
            raise SyntaxError('{}, status: {}. {}'.format(res.reason, res.status_code, res.text))

    def getClassifications(self):
        if not self.settings.ionburst_uri:
            raise ValueError('ionburst_uri is not specified!')
        res = self.__apihandler.classifications()
        if res.status_code is 200:
            return res.text
        else:
            raise SyntaxError('{}, status: {}. {}'.format(res.reason, res.status_code, res.text))

    def startDeferred(self, request = {}):
        self.__check_token()
        if 'action' not in request:
            raise ValueError('action must be specified in the parameter!')
        if 'id' not in request:
            raise ValueError('id must be specified in the parameter!')
        if request['action'] is 'GET':
            res = self.__apihandler.downloadData(request['id'], True)
        elif request['action'] is 'PUT':
            res = self.__apihandler.uploadData(request, True)
        else:
            raise ValueError('Deferred action is only available for PUT or GET')
        if res.status_code is 200:
            return res.text
        else:
            raise SyntaxError('{}, status: {}. {}'.format(res.reason, res.status_code, res.text))

    def checkDeferred(self, token = None):
        self.__check_token()
        res = self.__apihandler.checkDeferred(token)
        if res.status_code is 200 or res.status_code is 202:
            return res.text
        else:
            raise SyntaxError('{}, status: {}. {}'.format(res.reason, res.status_code, res.text))
    
    def fetch(self,token = None):
        self.__check_token()
        res = self.__apihandler.fetch(token)
        if res.status_code is 200:
            return res.content
        else:
            raise SyntaxError('{}, status: {}. {}'.format(res.reason, res.status_code, res.text))