from dataclasses import dataclass
from typing import Any, ClassVar, Optional

import requests
from pydantic import BaseModel, create_model

from apiResource import namedApiResource


class EndpointModel(BaseModel):
    url: ClassVar[str]

    @classmethod
    def fetchOne(cls, id: int):
        response = requests.get(f"https://pokeapi.co/api/v2/{cls.url}/{id}")
        if response.status_code == 200:
            data = response.json()
            return cls(**data)
        else:
            return None

    @classmethod
    def fetchMany(cls, **kwargs):
        url = f"https://pokeapi.co/api/v2/{cls.url}"
        if kwargs:
            url += "?" + "&".join(f"{k}={v}" for k, v in kwargs.items())

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return makePage(cls, data)
        else:
            return None


def makePage(cls, data):
    # class Inner(Page, BaseModel):
    #     results: list[namedApiResource(cls)]

    return create_model(
        cls.__name__,
        __base__=Page,
        results=(list[namedApiResource(cls)], ...),
    )(cls=cls, **data)


class Page(BaseModel):
    cls: Any
    count: int
    next: Optional[str]
    previous: Optional[str]

    # @property
    # def results(self):
    #     resource = namedApiResource(self.cls)
    #     return [resource(**result) for result in self.data["results"]]

    def fetchNext(self):
        response = requests.get(self.next)
        if response.status_code == 200:
            data = response.json()
            return makePage(self.cls, data)
        else:
            return None
