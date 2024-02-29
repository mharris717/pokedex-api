from apiResource import namedApiResource
from endpointModel import EndpointModel, PokeModel


class Language(EndpointModel):
    url = "language"

    id: int
    name: str
    official: bool
    iso639: str
    iso3166: str
    # more fields


class Name(PokeModel):
    name: str
    language: namedApiResource(Language)


class Type(PokeModel):
    pass


class VersionGroup(PokeModel):
    id: int
    name: str
    order: int
    # more fields


class Version(PokeModel):
    id: int
    name: str
    names: list[Name]
    version_group: namedApiResource(VersionGroup)


class VersionGameIndex(PokeModel):
    game_index: int
    version: namedApiResource(Version)


class Description(PokeModel):
    description: str
    language: namedApiResource(Language)


class Item(EndpointModel):
    url = "item"

    id: int
    name: str


class PokemonSpecies(PokeModel):
    id: int
    name: str
