from typing import Generic, TypeVar

import requests
from pydantic import BaseModel

T = TypeVar("T")


class NamedAPIResource(BaseModel, Generic[T]):
    name: str
    url: str


# I am losing type info
def namedApiResource(cls: T) -> NamedAPIResource[T]:
    return namedApiResourceLazy(lambda: cls)
    # class Inner(NamedAPIResource[T], Generic[T]):
    #     def resolve(self) -> T:
    #         response = requests.get(self.url)
    #         if response.status_code == 200:
    #             data = response.json()
    #             return cls(**data)
    #         else:
    #             return None

    # return Inner


def namedApiResourceLazy(f):
    class Inner(NamedAPIResource):
        def resolve(self):
            response = requests.get(self.url)
            if response.status_code == 200:
                data = response.json()
                return f()(**data)
            else:
                return None

    return Inner
