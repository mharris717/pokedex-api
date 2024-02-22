from pydantic import BaseModel
from typing import Optional
from typing import Generic, List, Optional, TypeVar

import requests

T = TypeVar("T")


class NamedAPIResource(BaseModel, Generic[T]):
    name: str
    url: str


def namedApiResource(cls: T) -> NamedAPIResource[T]:
    class Inner(NamedAPIResource[T]):
        def resolve(self) -> T:
            response = requests.get(self.url)
            if response.status_code == 200:
                data = response.json()
                return cls(**data)
            else:
                return None

    return Inner


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


class Ability(BaseModel):
    id: int
    name: str
    is_main_series: bool
    # generation: namedApiResource(Generation)
    names: List[Name]


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
    version_group_details: List[PokemonMoveVersion]


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
    # pokemon: namedApiResource(Pokemon)


class Pokemon(BaseModel):
    id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    abilities: List[PokemonAbility]
    # forms: List[PokemonFormType]
    forms: List[namedApiResource(PokemonForm)]
    game_indices: List[VersionGameIndex]
    held_items: List[PokemonHeldItem]
    location_area_encounters: str
    moves: List[PokemonMove]
    types: List[PokemonType]

    @classmethod
    def fetch_pokemon(cls, id: int):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
        if response.status_code == 200:
            data = response.json()
            return cls(**data)
        else:
            return None


res = Pokemon.fetch_pokemon(1)
print("bottom")
