from apiResource import NamedAPIResource, namedApiResource
from endpointModel import EndpointModel, PokeModel
from shared import (
    Description,
    Item,
    Name,
    PokemonSpecies,
    Version,
    VersionGameIndex,
    VersionGroup,
)


def importGeneration():
    from generation import Generation

    return Generation


class Ability(PokeModel):
    id: int
    name: str
    is_main_series: bool
    generation: namedApiResource(importGeneration)
    names: list[Name]


class PokemonHeldItemVersion(PokeModel):
    version: namedApiResource(Version)
    rarity: int


class PokemonHeldItem(PokeModel):
    item: namedApiResource(Item)
    version_details: list[PokemonHeldItemVersion]


class Move(EndpointModel):
    url = "move"

    id: int
    name: str


class MoveLearnMethod(EndpointModel):
    url = "move-learn-method"

    id: int
    name: str
    descriptions: list[Description]
    names: list[Name]
    version_groups: list[namedApiResource(VersionGroup)]


class PokemonMoveVersion(PokeModel):
    move_learn_method: namedApiResource(MoveLearnMethod)
    version_group: namedApiResource(VersionGroup)
    level_learned_at: int


class PokemonMove(PokeModel):
    move: namedApiResource(Move)
    version_group_details: list[PokemonMoveVersion]


class PokemonAbility(PokeModel):
    """Child Wrapper on Ability"""

    is_hidden: bool
    slot: int
    ability: namedApiResource(Ability)


class PokemonType(PokeModel):
    slot: int
    type: NamedAPIResource


class PokemonFormType(PokeModel):
    slot: int
    type: NamedAPIResource


class PokemonForm(PokeModel):
    id: int
    name: str
    order: int
    form_name: str
    pokemon: namedApiResource(lambda: Pokemon)


class PokemonCries(PokeModel):
    latest: str
    legacy: str


class Stat(EndpointModel):
    url = "stat"

    id: int
    name: str
    game_index: int
    is_battle_only: bool
    affecting_moves: dict
    affecting_natures: dict
    # more


class PokemonStat(PokeModel):
    stat: namedApiResource(lambda: Stat)
    effort: int
    base_stat: int


class PokemonSprites(PokeModel):
    front_default: str
    # more


class PokemonTypePast(PokeModel):
    generation: namedApiResource(importGeneration)
    types: list[PokemonType]


class Pokemon(EndpointModel):
    url = "pokemon"

    id: int
    name: str
    base_experience: int
    # height intentionally missing so we can test it's still accessible
    # height: int
    is_default: bool
    order: int
    weight: int
    abilities: list[PokemonAbility]
    forms: list[namedApiResource(PokemonForm)]
    game_indices: list[VersionGameIndex]
    held_items: list[PokemonHeldItem]
    location_area_encounters: str
    moves: list[PokemonMove]
    types: list[PokemonType]
    cries: PokemonCries
    species: namedApiResource(PokemonSpecies)
    stats: list[PokemonStat]
    sprites: PokemonSprites
    past_types: list[PokemonTypePast]
