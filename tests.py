from main import Pokemon


def assertBulbasaur(poke):
    assert poke.abilities[0].ability.resolve().name == "overgrow"
    assert poke.name == "bulbasaur"


def testSmoke():
    poke = Pokemon.fetchOne(1)
    assertBulbasaur(poke)


def testFetchList():
    pokes = Pokemon.fetchMany()
    assert len(pokes.results) == 20
    assert pokes.results[0].name == "bulbasaur"
    assertBulbasaur(pokes.results[0].resolve())
    nextPokes = pokes.fetchNext()
    assert len(nextPokes.results) == 20
    assert nextPokes.results[0].name == "spearow"
    assert nextPokes.results[0].resolve().name == "spearow"


def testFetchListOps():
    pokes = Pokemon.fetchMany(limit=5)
    assert len(pokes.results) == 5
    assert pokes.results[0].name == "bulbasaur"
