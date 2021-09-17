import day13


def test_make_title_all_words_lower():
    assert day13.make_title("i am a test sentence") == "I Am A Test Sentence"


def test_make_title_all_words_upper():
    assert day13.make_title("I AM A TEST SENTENCE") == "I AM A TEST SENTENCE"


def test_make_title_text_without_spaces():
    assert day13.make_title("iamatestsentence") == "Iamatestsentence"


def test_make_title_sentence_already_is_upper_first_letter():
    assert day13.make_title("I Am A Test Sentence") == "I Am A Test Sentence"


def test_make_title_empty_string():
    assert day13.make_title("") == ""


def test_make_tile_examples_from_site():
    assert day13.make_title("I am a title") == "I Am A Title"
    assert day13.make_title("I AM A TITLE") == "I AM A TITLE"
    assert day13.make_title("i aM a tITLE") == "I AM A TITLE"
    assert (
        day13.make_title("the first letter of every word is capitalized")
        == "The First Letter Of Every Word Is Capitalized"
    )
    assert day13.make_title("I Like Pizza") == "I Like Pizza"
    assert (
        day13.make_title("Don't count your ChiCKens BeFore They HatCh")
        == "Don't Count Your ChiCKens BeFore They HatCh"
    )
    assert (
        day13.make_title("All generalizations are false, including this one")
        == "All Generalizations Are False, Including This One"
    )
    assert (
        day13.make_title(
            "Me and my wife lived happily for twenty years and then we met."
        )
        == "Me And My Wife Lived Happily For Twenty Years And Then We Met."
    )
    assert (
        day13.make_title("There are no stupid questions, just stupid people.")
        == "There Are No Stupid Questions, Just Stupid People."
    )
    assert (
        day13.make_title("1f you c4n r34d 7h15, you r34lly n33d 2 g37 l41d")
        == "1f You C4n R34d 7h15, You R34lly N33d 2 G37 L41d"
    )
    assert day13.make_title("PIZZA PIZZA PIZZA") == "PIZZA PIZZA PIZZA"
