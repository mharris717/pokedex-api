from main import Pokemon


def testSmoke():
    assert Pokemon.fetch(1).abilities[0].ability.resolve().name == "overgrow"
