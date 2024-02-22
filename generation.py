from pydantic import BaseModel

from apiResource import namedApiResource
from endpointModel import EndpointModel
from main import Ability, Move
from shared import Name, Type, VersionGroup


class Region(BaseModel):
    id: int
    name: str
    # names: list[Name]
    # main_generation: namedApiResource(Generation)
    # pokedexes: list[namedApiResource(Pokedex)]
    # version_groups: list[namedApiResource(VersionGroup)]


class PokemonSpecies(BaseModel):
    id: int
    name: str


class Generation(EndpointModel):
    url = "generation"

    id: int
    name: str
    abilities: list[namedApiResource(Ability)]
    names: list[Name]
    main_region: namedApiResource(Region)
    moves: list[namedApiResource(Move)]
    pokemon_species: list[namedApiResource(PokemonSpecies)]
    types: list[namedApiResource(Type)]
    version_groups: list[namedApiResource(VersionGroup)]
