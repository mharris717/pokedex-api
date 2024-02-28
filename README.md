# Pokedex API SDK

This project is an SDK for the Pokedex API. It provides a set of classes and methods to interact with the API and retrieve data about Pokemon, their abilities, moves, types, and more.

## Installation

To install the Pokedex API SDK, you can use pip:

```bash
pip install pokedex-api-sdk
```

## Usage

Here's a simple example of how to use the SDK to retrieve information about a specific Pokemon:

```python
from pokedex_api_sdk import Pokemon

# Create a new Pokemon instance
bulbasaur = Pokemon.fetchOne(1) 

# Print the Pokemon's name
print(bulbasaur.name)
```

 
## Documentation

The `namedApiResource` function is used to create a new instance of the `NamedAPIResource` class. It takes a function `f` as an argument, which is used to resolve the resource when the `resolve` method is called on the instance.

If the function `f` is a type, it is wrapped in a lambda function and passed to `namedApiResource` again. This is to ensure that the function `f` is always a function, not a type.

The `resolve` method of the `NamedAPIResource` class sends a GET request to the `url` attribute of the instance. If the response status code is 200, it parses the response JSON and creates a new instance of the type returned by the function `f`. If the response status code is not 200, it returns `None`.

Here's an example of how to call the `resolve` method on a `NamedAPIResource` instance:

```python
from pokedex_api_sdk import Pokemon

# Create a new Pokemon instance
bulbasaur = Pokemon.fetchOne(1) 

# Call the resolve method on the Pokemon's abilities
for ability in bulbasaur.abilities:
    resolved_ability = ability.ability.resolve()
    print(resolved_ability.name)
```

### Fetching Lists

The `fetchMany` method is used to retrieve a list of resources. It takes two optional parameters: `limit` and `offset`. The `limit` parameter specifies the maximum number of resources to retrieve, and the `offset` parameter specifies the index of the first resource to retrieve.

Here's an example of how to use the `fetchMany` method to retrieve a list of Pokemon:

```python
from pokedex_api_sdk import Pokemon

# Fetch a list of Pokemon
pokemons = Pokemon.fetchMany(limit=20, offset=10)

# Print the count of Pokemon
print(pokemons.count)

# Print the name of the first Pokemon
print(pokemons.results[0].name)
# Resolve the first Pokemon in the list
resolved_pokemon = pokemons.results[0].resolve()

# Print the name of the resolved Pokemon
print(resolved_pokemon.name)

```





## TODO

Error handling
EndpointModel URL
Config 
Pydantic vs Raw. IF generating this, would definitely make sense. 


