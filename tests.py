import pytest

from apiResource import FetchError
from endpointModel import NoPageError
from generation import Generation
from pokemon import Pokemon


def assertBulbasaur(poke: Pokemon):
    assert poke.abilities[0].ability.resolve().name == "overgrow"
    assert poke.name == "bulbasaur"
    assert poke.height == 7


def testFetchOne():
    poke = Pokemon.fetchOne(1)
    assertBulbasaur(poke)

    gen = Generation.fetchOne(1)
    assert gen.name == "generation-i"


def testFieldNotExplicitlyDefined():
    poke = Pokemon.fetchOne(1)
    assert poke.height == 7


def testFetchList():
    pokes = Pokemon.fetchMany()
    assert len(pokes.results) == 20
    assert pokes.count == 1302
    assert pokes.results[0].name == "bulbasaur"
    assertBulbasaur(pokes.results[0].resolve())

    nextPokes = pokes.fetchNext()
    assert nextPokes.count == 1302
    assert len(nextPokes.results) == 20
    assert nextPokes.results[0].name == "spearow"
    assert nextPokes.results[0].resolve().name == "spearow"

    prevPokes = nextPokes.fetchPrevious()
    assert len(prevPokes.results) == 20
    assertBulbasaur(prevPokes.results[0].resolve())


def testFetchListOps():
    pokes = Pokemon.fetchMany(limit=5)
    assert len(pokes.results) == 5
    assert pokes.results[0].name == "bulbasaur"


def testFetchListResolveAll():
    pokes = Pokemon.fetchMany(limit=3).resolveAll()
    assert len(pokes) == 3
    assertBulbasaur(pokes[0])


def testError():
    with pytest.raises(FetchError):
        Pokemon.fetchOne(-1)

    firstPage = Pokemon.fetchMany()
    with pytest.raises(NoPageError):
        firstPage.fetchPrevious()
