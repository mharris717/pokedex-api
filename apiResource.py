from typing import Generic, TypeVar

import requests
from pydantic import BaseModel

T = TypeVar("T")


class FetchError(Exception):
    def __init__(self, url, params={}):
        self.url = url
        self.params = params
        super().__init__(f"Failed to fetch data from {url} with params {params}")


def pokeGet(url, params={}):
    response = requests.get(url, params)
    if response.status_code == 200:
        return response.json()
    else:
        raise FetchError(url, params)


class NamedAPIResource(BaseModel, Generic[T]):
    name: str
    url: str


def namedApiResource(f):
    if isinstance(f, type):
        return namedApiResource(lambda: f)

    class Inner(NamedAPIResource):
        def resolve(self):
            data = pokeGet(self.url)
            return f()(**data)

    return Inner
