from apiResource import namedApiResource
from pydantic import BaseModel


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
