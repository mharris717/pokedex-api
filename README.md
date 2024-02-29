# Pokedex API SDK

This project is an SDK for the Pokedex API. It provides a set of classes and methods to interact with the API and retrieve data about Pokemon, their abilities, moves, types, and more.

## Installation (in magical pretend land where I published this)

To install the Pokedex API SDK, you can use pip:

```bash
pip install pokedex-api-sdk
```

## Usage

Here's a simple example of how to use the SDK to retrieve information about a specific Pokemon:

```python
from pokedex_api_sdk import Pokemon, Generation

bulbasaur = Pokemon.fetchOne(1)  
print(bulbasaur.name)
print(bulbasaur.abilities[0].ability.resolve().name)

generations = Generation.fetchMany()
print(generations.results[0].name)

```

 
## Documentation

### Fetching by ID

The `fetchOne` method retrieves a single object. 

```python
poke = Pokemon.fetchOne(1)
print(poke.name)
```

### Fetching Lists

The `fetchMany` method is used to retrieve a list of resources. It takes two optional parameters: `limit` and `offset`. The `limit` parameter specifies the maximum number of resources to retrieve, and the `offset` parameter specifies the index of the first resource to retrieve.

It returns a Page object. You can access the total count, next and previous pages, and most importantly the results. `results` is a list of NamedApiResources. Call `resolve` on an item in the list to fetch the corresponding full object. 

You can fetch all referenced objects with `resolveAll`, but be careful, as this does a separate request for each one. 

Here's an example of how to use the `fetchMany` method to retrieve a list of Pokemon:

```python
pokes = Pokemon.fetchMany(limit=20, offset=10)
print(pokes.count)
print(pokes.results[0].name)
resolved_pokemon = pokes.results[0].resolve()
print(resolved_pokemon.name)
```

```python
pokes = Pokemon.fetchMany(limit=5)
resolved = pokes.resolveAll() 
print(resolved[0].name)
```

### NamedApiResource

The `namedApiResource` function is used to create a new instance of the `NamedAPIResource` class. It takes the referenced class (or a lambda returning the class) as the only arg. 

The `resolve` method of the `NamedAPIResource` class sends a GET request to the `url` attribute of the instance. You call `resolve` to fetch the full referenced object. 

Here's an example of how to call the `resolve` method on a `NamedAPIResource` instance:

```python
# Create a new Pokemon instance
bulbasaur = Pokemon.fetchOne(1) 

# Call the resolve method on the Pokemon's abilities
for ability in bulbasaur.abilities:
    resolved_ability = ability.ability.resolve()
    print(resolved_ability.name)
```

### EndpointModel

The `EndpointModel` class is a subclass of `PokeModel` and is used to create new instances of specific endpoint models. It has a `url` attribute that specifies the base URL for the endpoint. The `fetchOne` method is used to retrieve a single resource from the endpoint, while the `fetchMany` method is used to retrieve a list of resources.

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

### Field definitions

I defined most of the fields on Pokemon/Generation, along with the classes for most of the references/children. I did not do everything, which I assume is just fine for this exercise. 

The way I structured the NamedApiResource code could definitely be better. I started out trying to get the type hints right, but eventually abandoned that for time. I'll bet I could do this as well or better without the helper `namedApiResource` factory method, but that's the approach I ended on with the time available. 