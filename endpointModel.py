from dataclasses import dataclass
from typing import Any, ClassVar

import requests
from pydantic import BaseModel

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
            return Page(cls, data)
        else:
            return None


@dataclass
class Page:
    cls: Any
    data: Any

    @property
    def results(self):
        resource = namedApiResource(self.cls)
        return [resource(**result) for result in self.data["results"]]

    def fetchNext(self):
        response = requests.get(self.data["next"])
        if response.status_code == 200:
            data = response.json()
            return Page(self.cls, data)
        else:
            return None
