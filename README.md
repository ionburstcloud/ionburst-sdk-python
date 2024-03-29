![PyPI](https://img.shields.io/pypi/v/ionburst-sdk-python?color=fb6a26&style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ionburst-sdk-python?color=fb6a26)
![Gitlab pipeline status](https://img.shields.io/gitlab/pipeline/ionburst/ionburst-sdk-net/main?color=fb6a26&style=flat-square)
[![slack](https://img.shields.io/badge/Slack-4A154B?style=flat-square&logo=slack&logoColor=white)](https://join.slack.com/t/ionburst-cloud/shared_invite/zt-panjkslf-Z5DOpU1OOeNPkXgklD~Cpg)

# Ionburst SDK for Python

The **Ionburst SDK for Python** enables developers to easily integrate with [Ionburst Cloud][ionburst-cloud], building in ultra-secure and private object storage to their applications.

* [API Docs][docs-api]
* [SDK Docs][sdk-website]
* [Issues][sdk-issues]
* [SDK Samples](https://ionburst.cloud/docs/sdk/python)

## Getting Started

### Installation

```sh
pip3 install ionburst-sdk-python
# OR
pip3 install ionburst-sdk-python --user
```

### Configuration

The Ionburst SDK can get its configuration (ionburst_id, ionburst_key, ionburst_uri) from the following three files.

If `ionburst_id` and `ionburst_key` are not specified by environment variable, they are obtained from the credentials file with information from the `config.json` file.

If `ionburst_uri` is not specified in Ionburst constructor, it'll first check `config.json`, and then the credentials file.

#### Environment Variables

```sh
IONBURST_ID=IB******************
IONBURST_KEY=eW91aGF2ZXRvb211Y2h0aW1lb255b3VyaGFuZHMh
```

#### config.json file

```json
{
  "Ionburst": {
    "Profile": "example",
    "IonburstUri": "https://api.example.ionburst.cloud/",
    "TraceCredentialsFile": "OFF"
  }
}
```

#### Credentials file

```sh
[example]
ionburst_id=IB******************
ionburst_key=eW91aGF2ZXRvb211Y2h0aW1lb255b3VyaGFuZHMh
ionburst_uri=https://api.example.ionburst.cloud/
```

### Usage

#### Initialise

```sh
from Ionburst import Ionburst
ionburst = Ionburst()

```

or

```sh
from Ionburst import Ionburst
ionburst = Ionburst("https://api.example.ionburst.cloud/")
```

#### Upload Data

```sh
result = ionburst.put({
  id: '...',
  data: '...',
  classstr: '...' // Not Required
})
```

#### Download Data

```sh
result = ionburst.get(id)
```

#### Delete Data

```sh
result = ionburst.delete(id)
```

#### Upload Data Deferred

```sh
token = ionburst.startDeferredAction({
  action: 'PUT',
  id: '...',
  data: '...',
  classstr: '...'  // Not Required
})
```

#### Download Data Deferred

```sh
token = ionburst.startDeferredAction({
  action: 'GET',
  id: '...'
})
```

#### Check Data Deferred

```sh
result = ionburst.checkDeferred(token)
```

#### Fetch Data Deferred

```sh
result = ionburst.fetch(token)
```

#### Get Classifcations

```sh
data = ionburst.getClassifications()
```

## Getting Help

Please use the following community resources to get help. We use [Gitlab issues][sdk-issues] to track bugs and feature requests.

* Join the Ionburst Cloud community on [Slack](https://join.slack.com/t/ionburst-cloud/shared_invite/zt-panjkslf-Z5DOpU1OOeNPkXgklD~Cpg)
* Get in touch with [Ionburst Support](https://ionburst.cloud/contact)
* If it turns out that you may have found a bug, please open an [issue][sdk-issues]

### Opening Issues

If you find a bug, or have an issue with the Ionburst SDK for Python we would like to hear about it. Check the existing [issues][sdk-issues] and try to make sure your problem doesn’t already exist before opening a new issue. It’s helpful if you include the version of `ionburst-sdk-python` and the OS you’re using. Please include a stack trace and reduced repro case when appropriate, too.

The [Gitlab issues][sdk-issues] are intended for bug reports and feature requests. For help and questions with using the Ionburst SDK for Python please make use of the resources listed in the Getting Help section. There are limited resources available for handling issues and by keeping the list of open issues clean we can respond in a timely manner.

## SDK Change Log

The change log for the SDK can be found in the Gitlab Releases [page](https://gitlab.com/ionburst/ionburst-sdk-python)

## Contributors

A massive thanks to [Costin Botez](https://github.com/costibotez) for developing this SDK.

## Tests

### Dependencies

* [python-dotenv](https://pypi.org/project/python-dotenv/),
* [requests](https://pypi.org/project/requests/)
* [certifi](https://pypi.org/project/certifi/),
* [chardet](https://pypi.org/project/chardet/),
* [idna](https://pypi.org/project/idna/),
* [urllib3](https://pypi.org/project/urllib3/),

[ionburst]: https://ionburst.io
[ionburst-cloud]: https://ionburst.cloud
[sdk-website]: https://ionburst.cloud/docs/sdk/
[sdk-source]: https://gitlab.com/ionburst/ionburst-sdk-python
[sdk-issues]: https://gitlab.com/ionburst/ionburst-sdk-python/issues
[sdk-license]: https://gitlab.com/ionburst/ionburst-sdk-python/-/blob/master/LICENSE
[docs-api]: https://ionburst.cloud/docs/api/
