from mrs_spellings import MrsWord


def test_swap():
    word = MrsWord("Hello")
    assert word.swap() == {"eHllo", "Hlelo", "Hello", "Helol"}


def test_delete():
    word = MrsWord("Hello")
    assert word.delete() == {"ello", "Hllo", "Helo", "Hell"}


def test_qwerty_swap():
    word = MrsWord("Hello")
    assert word.qwerty_swap() == {
        "Gello",
        "He:lo",
        "Heklo",
        "Hel:o",
        "Helko",
        "Helli",
        "Hellp",
        "Hrllo",
        "Hwllo",
        "Jello",
    }

def test_to_list():
    word = MrsWord("Hello")
    assert sorted(word.swap().to_list()) == sorted(["eHllo", "Hlelo", "Hello", "Helol"])

def test_swap_swap_spellings():
    word = MrsWord("Hello")
    assert word.swap().swap() == {
        "Hello",
        "Helol",
        "Heoll",
        "Hlelo",
        "Hleol",
        "Hlleo",
        "eHllo",
        "eHlol",
        "elHlo",
        "lHelo",
    }


def test_delete_qwerty_swap_spellings():
    word = MrsWord("Hello")
    assert MrsWord("Hello").delete().qwerty_swap() == {
        "Gell",
        "Gelo",
        "Gllo",
        "H:lo",
        "He:l",
        "He:o",
        "Hekl",
        "Heko",
        "Hel:",
        "Heli",
        "Helk",
        "Help",
        "Hklo",
        "Hl:o",
        "Hlko",
        "Hlli",
        "Hllp",
        "Hrll",
        "Hrlo",
        "Hwll",
        "Hwlo",
        "Jell",
        "Jelo",
        "Jllo",
        "e:lo",
        "eklo",
        "el:o",
        "elko",
        "elli",
        "ellp",
        "rllo",
        "wllo",
    }


def test_qwerty_swap_delete_spellings():
    word = MrsWord("Hello")
    assert word.qwerty_swap().delete() == {
        "Gell",
        "Gelo",
        "Gllo",
        "H:lo",
        "He:l",
        "He:o",
        "Hekl",
        "Heko",
        "Hel:",
        "Heli",
        "Helk",
        "Hell",
        "Helo",
        "Help",
        "Hklo",
        "Hl:o",
        "Hlko",
        "Hlli",
        "Hllo",
        "Hllp",
        "Hrll",
        "Hrlo",
        "Hwll",
        "Hwlo",
        "Jell",
        "Jelo",
        "Jllo",
        "e:lo",
        "eklo",
        "el:o",
        "elko",
        "elli",
        "ello",
        "ellp",
        "rllo",
        "wllo",
    }
