from apiResource import namedApiResource
from endpointModel import EndpointModel, PokeModel
from pokemon import Ability, Move
from shared import Name, PokemonSpecies, Type, VersionGroup


class Region(PokeModel):
    id: int
    name: str
    # names: list[Name]
    # main_generation: namedApiResource(Generation)
    # pokedexes: list[namedApiResource(Pokedex)]
    # version_groups: list[namedApiResource(VersionGroup)]


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
