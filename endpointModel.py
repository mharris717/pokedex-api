from typing import ClassVar

import requests
from pydantic import BaseModel


class EndpointModel(BaseModel):
    url: ClassVar[str]

    @classmethod
    def fetch(cls, id: int):
        response = requests.get(f"https://pokeapi.co/api/v2/{cls.url}/{id}")
        if response.status_code == 200:
            data = response.json()
            return cls(**data)
        else:
            return None
