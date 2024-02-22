from apiResource import NamedAPIResource, namedApiResource, namedApiResourceLazy
from pydantic import BaseModel


from endpointModel import EndpointModel

from shared import Name


class Ability(BaseModel):
    id: int
    name: str
    is_main_series: bool
    # generation: namedApiResource(Generation)
    names: list[Name]


class VersionGameIndex(BaseModel):
    pass


class PokemonHeldItem(BaseModel):
    pass


class Move(BaseModel):
    pass


class MoveLearnMethod(BaseModel):
    pass


class VersionGroup(BaseModel):
    pass


class PokemonMoveVersion(BaseModel):
    move_learn_method: namedApiResource(MoveLearnMethod)
    version_group: namedApiResource(VersionGroup)
    level_learned_at: int


class PokemonMove(BaseModel):
    move: namedApiResource(Move)
    version_group_details: list[PokemonMoveVersion]


class PokemonAbility(BaseModel):
    is_hidden: bool
    slot: int
    ability: namedApiResource(Ability)


class PokemonType(BaseModel):
    slot: int
    type: NamedAPIResource


class PokemonFormType(BaseModel):
    slot: int
    type: NamedAPIResource


class PokemonForm(BaseModel):
    id: int
    name: str
    order: int
    form_name: str
    pokemon: namedApiResourceLazy(lambda: Pokemon)


class Pokemon(EndpointModel):
    url = "pokemon"

    id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    abilities: list[PokemonAbility]
    # forms: List[PokemonFormType]
    forms: list[namedApiResource(PokemonForm)]
    game_indices: list[VersionGameIndex]
    held_items: list[PokemonHeldItem]
    location_area_encounters: str
    moves: list[PokemonMove]
    types: list[PokemonType]
