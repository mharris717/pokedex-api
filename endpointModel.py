from typing import Any, ClassVar, Optional

from pydantic import BaseModel, ConfigDict, create_model

from apiResource import namedApiResource, pokeGet

BASE_URL = "https://pokeapi.co/api/v2"


class PokeModel(BaseModel):
    model_config = ConfigDict(extra="allow")


class EndpointModel(PokeModel):
    url: ClassVar[str]

    @classmethod
    def fetchOne(cls, id: int):
        data = pokeGet(f"{BASE_URL}/{cls.url}/{id}")
        return cls(**data)

    @classmethod
    def fetchMany(cls, **kwargs):
        data = pokeGet(f"{BASE_URL}/{cls.url}", kwargs)
        return makePage(cls, data)


def makePage(cls, data):
    return create_model(
        cls.__name__,
        __base__=Page,
        results=(list[namedApiResource(cls)], ...),
    )(cls=cls, **data)


class NoPageError(Exception):
    pass


class Page(BaseModel):
    cls: Any
    count: int
    next: Optional[str]
    previous: Optional[str]

    def _fetch(self, url):
        if not url:
            raise NoPageError
        data = pokeGet(url)
        return makePage(self.cls, data)

    def fetchNext(self):
        return self._fetch(self.next)

    def fetchPrevious(self):
        return self._fetch(self.previous)

    def resolveAll(self):
        return [res.resolve() for res in self.results]
