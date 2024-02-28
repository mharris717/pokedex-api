from typing import Generic, TypeVar

import requests
from pydantic import BaseModel

T = TypeVar("T")


class NamedAPIResource(BaseModel, Generic[T]):
    name: str
    url: str


def namedApiResource(f):
    if isinstance(f, type):
        return namedApiResource(lambda: f)

    class Inner(NamedAPIResource):
        def resolve(self):
            response = requests.get(self.url)
            if response.status_code == 200:
                data = response.json()
                return f()(**data)
            else:
                return None

    return Inner
