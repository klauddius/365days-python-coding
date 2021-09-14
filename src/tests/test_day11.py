import day11


def test_stutter_example1():
    assert day11.stutters('incredible') == "in... in... incredible?"


def test_stutter_example2():
    assert day11.stutters('enthusiastic') == "en... en... enthusiastic?"


def test_stutter_example3():
    assert day11.stutters('outstanding') == "ou... ou... outstanding?"


def test_stutter_examples():
    actual_param, expected_param = [
                                       "increasing", "adventures", "enticing",
                                       "unacceptable", "accountable",
                                       "incredible", "exquisite",
                                       "am", "enduring", "outstanding",
                                       "astonishing", "astounding",
                                       "impressive", "revolutionize",
                                       "recurring", "recollection", "so",
                                       "gorgeous", "captivating"
                                   ], [
                                       "in... in... increasing?",
                                       "ad... ad... adventures?",
                                       "en... en... enticing?",
                                       "un... un... unacceptable?",
                                       "ac... ac... accountable?",
                                       "in... in... incredible?",
                                       "ex... ex... exquisite?",
                                       "am... am... am?",
                                       "en... en... enduring?",
                                       "ou... ou... outstanding?",
                                       "as... as... astonishing?",
                                       "as... as... astounding?",
                                       "im... im... impressive?",
                                       "re... re... revolutionize?",
                                       "re... re... recurring?",
                                       "re... re... recollection?",
                                       "so... so... so?",
                                       "go... go... gorgeous?",
                                       "ca... ca... captivating?",
                                   ]
    for i, w in enumerate(actual_param):
        assert day11.stutters(w) == expected_param[i]

