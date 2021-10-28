from day17 import format_math


def test_examples_from_site():
    assert format_math("3 + 4") == "3 + 4 = 7"
    assert format_math("3 - 2") == "3 - 2 = 1"
    assert format_math("4 x 5") == "4 x 5 = 20"
    assert format_math("6 / 3") == "6 / 3 = 2"
    assert format_math("9 / 3") == "9 / 3 = 3"
    assert format_math("21 / 3") == "21 / 3 = 7"
    assert format_math("24 / 3") == "24 / 3 = 8"
    assert format_math("80 / 8") == "80 / 8 = 10"
    assert format_math("60 / 30") == "60 / 30 = 2"
    assert format_math("44 - 11") == "44 - 11 = 33"
    assert format_math("48 + 35") == "48 + 35 = 83"
    assert format_math("8 + 5") == "8 + 5 = 13"
    assert format_math("46 - 11") == "46 - 11 = 35"
    assert format_math("23 x 46") == "23 x 46 = 1058"
    assert format_math("11 + 1") == "11 + 1 = 12"
    assert format_math("29 - 21") == "29 - 21 = 8"
    assert format_math("24 x 26") == "24 x 26 = 624"
    assert format_math("47 + 8") == "47 + 8 = 55"
    assert format_math("42 - 48") == "42 - 48 = -6"
    assert format_math("33 x 44") == "33 x 44 = 1452"
    assert format_math("26 + 3") == "26 + 3 = 29"
    assert format_math("32 + 17") == "32 + 17 = 49"
    assert format_math("3 x 26") == "3 x 26 = 78"
    assert format_math("12 x 25") == "12 x 25 = 300"
    assert format_math("43 + 31") == "43 + 31 = 74"
    assert format_math("28 + 27") == "28 + 27 = 55"
    assert format_math("24 - 11") == "24 - 11 = 13"
    assert format_math("20 x 50") == "20 x 50 = 1000"
    assert format_math("36 - 30") == "36 - 30 = 6"
    assert format_math("34 x 48") == "34 x 48 = 1632"
    assert format_math("26 + 8") == "26 + 8 = 34"
    assert format_math("25 - 44") == "25 - 44 = -19"
    assert format_math("24 x 25") == "24 x 25 = 600"
    assert format_math("40 x 17") == "40 x 17 = 680"
    assert format_math("44 - 7") == "44 - 7 = 37"
    assert format_math("37 x 41") == "37 x 41 = 1517"
    assert format_math("15 - 1") == "15 - 1 = 14"
    assert format_math("16 x 4") == "16 x 4 = 64"
    assert format_math("13 x 43") == "13 x 43 = 559"
    assert format_math("7 x 11") == "7 x 11 = 77"
    assert format_math("12 - 25") == "12 - 25 = -13"
    assert format_math("37 + 6") == "37 + 6 = 43"
    assert format_math("32 x 46") == "32 x 46 = 1472"
    assert format_math("31 x 5") == "31 x 5 = 155"
    assert format_math("17 - 37") == "17 - 37 = -20"
    assert format_math("31 + 36") == "31 + 36 = 67"
    assert format_math("17 x 34") == "17 x 34 = 578"
    assert format_math("24 - 3") == "24 - 3 = 21"
    assert format_math("48 + 33") == "48 + 33 = 81"
    assert format_math("19 + 1") == "19 + 1 = 20"
    assert format_math("45 + 1") == "45 + 1 = 46"
    assert format_math("34 + 24") == "34 + 24 = 58"
    assert format_math("32 + 41") == "32 + 41 = 73"
    assert format_math("1 - 21") == "1 - 21 = -20"
    assert format_math("40 x 8") == "40 x 8 = 320"
    assert format_math("4 - 16") == "4 - 16 = -12"
    assert format_math("30 - 43") == "30 - 43 = -13"
    assert format_math("26 + 49") == "26 + 49 = 75"
    assert format_math("24 x 38") == "24 x 38 = 912"