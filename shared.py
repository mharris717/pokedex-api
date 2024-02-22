from pydantic import BaseModel

from apiResource import namedApiResource
from endpointModel import EndpointModel


class Language(BaseModel):
    id: int
    name: str
    official: bool
    iso639: str
    iso3166: str
    # names: List[Name]


class Name(BaseModel):
    name: str
    language: namedApiResource(Language)


class Type(BaseModel):
    pass


class VersionGroup(BaseModel):
    id: int
    name: str
    order: int
    # more fields


class Version(BaseModel):
    id: int
    name: str
    names: list[Name]
    version_group: namedApiResource(VersionGroup)


class VersionGameIndex(BaseModel):
    game_index: int
    version: namedApiResource(Version)


class Description(BaseModel):
    description: str
    language: namedApiResource(Language)


class Item(EndpointModel):
    url = "item"

    id: int
    name: str
