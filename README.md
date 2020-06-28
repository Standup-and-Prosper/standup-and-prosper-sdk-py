# Standup & Prosper SDK
Standup & Prosper SDK for Python.

[![NuGet version](https://badge.fury.io/py/standup-and-prosper-sdk.svg)](https://badge.fury.io/py/standup-and-prosper-sdk) [![Build Status](https://travis-ci.com/Teaminator/standup-and-prosper-sdk.py.svg?branch=release%2F1.0)](https://travis-ci.com/github/Teaminator/standup-and-prosper-sdk.py)

This is the Standup & Prosper SDK used to integrate with programmatic standups at https://standup.teaminator.io.

## Usage

```sh
pip install standup-and-prosper-sdk
```
(you may need to run `pip` with root permission: `sudo pip install standup-and-prosper-sdk`)

Then import the package:
```python
import standup_and_prosper_sdk
```

## Getting Started

### Get Standup Threads
```python
from standup_and_prosper_sdk import ApiClient, StandupsApi

access_key = "eyARB5k-..." # Create on at https://standup.teaminator.io/app/#/api
team_id = "TEAM_ID"
standup_id = "STANDUP_ID" # Can be found on the https://standup.teaminator.io/app/#/standups page or by querying the existing standups

api_client = ApiClient(access_key)
api = StandupsApi(api_client)
threadResponse = api.get_standup_threads(team_id, standup_id)
print(threadResponse.threads)
```
