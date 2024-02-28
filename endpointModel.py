from typing import Any, ClassVar, Optional

import requests
from pydantic import BaseModel, ConfigDict, create_model

from apiResource import namedApiResource


class PokeModel(BaseModel):
    model_config = ConfigDict(extra="allow")


class EndpointModel(PokeModel):
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
        response = requests.get(f"https://pokeapi.co/api/v2/{cls.url}", kwargs)
        if response.status_code == 200:
            data = response.json()
            return makePage(cls, data)
        else:
            return None


def makePage(cls, data):
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

    def _fetch(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return makePage(self.cls, data)
        else:
            return None

    def fetchNext(self):
        return self._fetch(self.next)

    def fetchPrevious(self):
        return self._fetch(self.previous)
