# KUDOS 👏 to brave innovator https://github.com/SpicySoftware/AIDevsTasks ❤️
# I just made some minor changes to make it work my way
import json
import requests

from enum import Enum
from typing import Tuple, Dict
from pprint import pprint


class HTTPMethod(Enum):
    GET  = 'GET'
    POST = 'POST'


class AIDevsTasks:

    class WrongRequest(Exception):
        pass

    CREDENTIAL_FILE = 'http-client.private.env.json'
    ENVIRONMENT = 'aidev'

    def __init__(self, task_name: str, debug: bool = True):
        self._task_name = task_name
        self._debug = debug
        self._obtain_credentials(AIDevsTasks.ENVIRONMENT)
        self._token = self._obtain_task_token(self._task_name)

    def log(self, header: str, result: Tuple[int, any]):
        status, result = result
        print(f"=> {header} [{status}]")
        pprint(result)
        print()

    def _obtain_credentials(self, env: str) -> None:
        creds = read_credentials(AIDevsTasks.CREDENTIAL_FILE, env)
        self.creds = creds
        self.base_url = creds['task-api-url']
        self._api_key = creds['task-api-key']


    def _obtain_task_token(self, task_name: str) -> str:
        token_url = f"{self.base_url}/token/{task_name}"
        response = request(HTTPMethod.POST, url=token_url, json=dict(apikey=self._api_key))

        return assert_correct(response)['token']

    def task(self) -> dict:
        task_url = f"{self.base_url}/task/{self._token}"

        result = request(HTTPMethod.GET, url=task_url)

        if self._debug:
            self.log("TASK", result)

        return assert_correct(result)

    def hint(self) -> dict:
        hint_url = f"{self.base_url}/hint/{self._task_name}"

        result = request(HTTPMethod.GET, url=hint_url)

        if self._debug:
            self.log("HINT", result)

        return assert_correct(result)

    def send_answer(self, answer: dict) -> dict:
        answer_url = f"{self.base_url}/answer/{self._token}"

        result = request(HTTPMethod.POST, url=answer_url,json=answer)

        if self._debug:
            self.log("ANSWER", result)

        return result[1] # no correctness check, return anything that was returned

    def __str__(self) -> str:
        return f"Task( {self._task_name} )"


def request(method: HTTPMethod, **kwargs) -> Tuple[int, dict]:
    match method:
        case HTTPMethod.GET:
            response = requests.get(**kwargs)
        case HTTPMethod.POST:
            response = requests.post(**kwargs)

    try:
        data = response.json()
    except json.JSONDecodeError:
        data = dict(code=-1, json=False, text=response.text)

    return response.status_code, data


def assert_correct(response: Tuple[int, dict]) -> dict:
    code, data = response

    assert code in (200, 201, 202, 204), f"Error: unsuccessful HTTP status code: {code}"
    return data


def read_credentials(path: str, env: str) -> dict:
    with open(path, 'r') as file:
        credentials = json.load(file)

    assert env in credentials, f"Environment '{env}' not found in {path}"
    return credentials[env]