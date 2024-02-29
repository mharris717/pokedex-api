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

### EndpointModel

The `EndpointModel` class is a subclass of `PokeModel` and is used to create new instances of specific endpoint models. It has a `url` attribute that specifies the base URL for the endpoint. The `fetchOne` method is used to retrieve a single resource from the endpoint, while the `fetchMany` method is used to retrieve a list of resources.


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

## Design Decisions

### Pydantic

I focused my efforts around Pydantic models. 

Pros:
* You get runtime validation automatically 
* Named resource fields get handled/coerced automatically 
* User gets to work with nice classes instead of raw dicts and lists

Cons: 
* You can't access an endpoint without defining a model 
* Fields not explicitly defined can still be accessed, but they have poor DX for lists/dicts. 
* You can still access the named resource info on fields not explicitly defined, but they are much harder to work with

In hindsight, I think this approach makes the most sense if you're generating the models from a spec. In that case, you can be reasonably confident you're covering everything. If you're producing the SDK in a more manual way, I might take a different approach. You'd sacrifice some DX for the cases you covered, but things you didn't explicitly cover would work identically, instead of being worse or impossible. 

The runtime validation is nice, but for this case seems unimportant. This API is stable and well documented. For cases where the API is evolving rapidly or less reliably documented, the validation would provide more value. 

### No Root/SDK object

There's no explicit SDK object / client object / place for user to set global config. For this API that makes sense, as there really isn't any config, I don't fdeel like you're losing much. For many other APIs, this would be a big gap. 




## TODO

Error handling
EndpointModel URL
Config 
Pydantic vs Raw. IF generating this, would definitely make sense. 
fetch methods
Lack of a config or root sdk object
Handling unspecified fields
Not being able to walk the named resource if not specified. 


