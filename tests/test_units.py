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
