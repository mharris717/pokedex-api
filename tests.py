from main import Pokemon


def assertBulbasaur(poke):
    assert poke.abilities[0].ability.resolve().name == "overgrow"
    assert poke.name == "bulbasaur"
    assert poke.height == 7


def testSmoke():
    poke = Pokemon.fetchOne(1)
    assertBulbasaur(poke)


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


def testFetchListOps():
    pokes = Pokemon.fetchMany(limit=5)
    assert len(pokes.results) == 5
    assert pokes.results[0].name == "bulbasaur"
