"""This contains tests for 4 functions.

Notes
-----
dic_interpreter is not tested directly here because it is
implicitly tested through dic_calculator, which calls on it.

Even though these would be considered explicitly unit tests,
I consider date_check and dic_calculator to be integration tests
implicitly because within their functions, they do call other
functions. Hence if the asserts for date_check and dic_calculator
fail, that may be an issue due to functions not interacting with
each other in intended and/or considered ways.

Lastly, these tests are extensive. I'm sure I might've missed
one or two edge case considerations overall, but I'm fairly
confident that I've covered the vast majority of edge cases.
"""
from functions import city_format, moon_scraper, date_check, dic_calculator


def test_city_format():
    """Asserts if the city is formatted properly for web-scraping.

    Notes
    -----
    There are few asserts, but they cover the edge cases.
    1. Inputs with no punctuation
    2. Input with normal punctuation
    3. Input with the one exceptional punctuation.
    """
    assert city_format("Sacramento") == "sacramento"
    assert city_format("St. Louis") == "st-louis"
    assert city_format("Coeur d’Alene") == "coeur-d-alene"


def test_moon_scraper():
    """Asserts if correct moonrise/moonset is given for a US City & Date.

    Notes
    -----
    The function moon_scraper() doesn't have to be concerned about:
    (1) If proper date is given, but no inputted city.
    (2) If the date is properly given or not.

    These flaws are handled properly by other functions that call this.
    The function moon_scraper() does handle:
    (1) If proper date is given, but not given a city.
    (2) If proper date is given, but city is not accessible by web-scraper.
    (3) If proper date is given, but city is spelled oddly.

    Output of moon_scraper() is always ["moonrise", "moonset"]
    """
    assert (moon_scraper("Hyrule", 2014, 2, 5)
            == ["Invalid City Name OR", "No Moonrise/set time exists"])
    assert moon_scraper("San Diego", 2006, 1, 7) == ["11:55 am", "12:35 am"]
    assert moon_scraper("San Diego", 2006, 7, 16) == ["11:50 pm", "12:02 pm"]
    assert moon_scraper("Sacr@amen@to", 2016, 1, 12) == ["9:04 am", "8:24 pm"]
    assert moon_scraper("Concord", 2022, 6, 8) == ["1:37 pm", "1:50 am"]
    assert moon_scraper("ChIcAgO", 2019, 4, 10) == ["9:47 am", "No moonset"]
    assert moon_scraper("SeaTTle", 2013, 10, 11) == ["2:22 pm", "No moonset"]
    assert moon_scraper("DaLLas", 2010, 12, 27) == ["No moonrise", "11:41 am"]
    assert moon_scraper("PHO!!enix", 2027, 7, 27) == ["No moonrise", "2:10 pm"]


def test_date_check():
    """Asserts if the date is a legitimate date.
    If it is, assert that it gives the proper moonrise/set & phase.
    If it is, but city's mis-spelled/isn't supported,
    assert correct output accordingly.
    If it isn't, assert that it gives the proper output.

    Notes
    -----
    Cannot compute moon-phase prior to 1/6/2000. Thus, "Invalid Date".
    Input: date_check(str_city, str_year, str_month, str_day)
    Output of date_check() is always ["moonrise", "moonset", "phase"]
    """
    assert (date_check("San Diego", "2000", "1", "5")
            == ["5:54 am", "4:21 pm", "Can't compute before 1-6-2000"])
    assert (date_check("San Diego", "2000", "1", "6")
            == ["6:44 am", "5:10 pm", "New Moon"])
    assert (date_check("San Diego", "2020", "05", "12")
            == ["12:23 am", "10:38 am", "Waning Gibbous"])
    assert (date_check("San Diego", "2020", "5", "12")
            == ["12:23 am", "10:38 am", "Waning Gibbous"])
    assert (date_check("San Diego", "10000", "5", "12")
            == ["Invalid Date", "Invalid Date", "Invalid Date"])
    assert (date_check("San Diego", "2020", "13", "12")
            == ["Invalid Date", "Invalid Date", "Invalid Date"])
    assert (date_check("San Diego", "2020", "5", "49")
            == ["Invalid Date", "Invalid Date", "Invalid Date"])
    assert (date_check("San Diegooo", "2020", "5", "12")
            == ["Invalid City Name OR", "No Moonrise/set time exists", "Waning Gibbous"])


# I acknowledge that the moon phase algorithm is rudimentary.
# But it should pass the following tests to demonstrate its capability.
# I test 2010, 2015, 2020, 2025, & 2030 to prove its worth.
def test_dic_calculator_2010():
    """Asserts if the moonphase is correct given the dates.

    Notes
    -----
    Dates are sourced from: https://www.almanac.com/astronomy/moon/calendar
    Writing asserts this way allows for immediate pin-pointing of issues.
    This test checks primary moon-phases (New, First, Full, Third) to assert
    if there is any significant deviation in the moon phase algorithm.
    This test checks for primary moon-phases of 2010.
    """
    assert dic_calculator(2010, 1, 7) == "Third Quarter"
    assert dic_calculator(2010, 1, 14) == "New Moon"
    assert dic_calculator(2010, 1, 23) == "First Quarter"
    assert dic_calculator(2010, 1, 29) == "Full Moon"
    assert dic_calculator(2010, 2, 5) == "Third Quarter"
    assert dic_calculator(2010, 2, 13) == "New Moon"
    assert dic_calculator(2010, 2, 21) == "First Quarter"
    assert dic_calculator(2010, 2, 28) == "Full Moon"
    assert dic_calculator(2010, 3, 7) == "Third Quarter"
    assert dic_calculator(2010, 3, 15) == "New Moon"
    assert dic_calculator(2010, 3, 23) == "First Quarter"
    assert dic_calculator(2010, 3, 29) == "Full Moon"
    assert dic_calculator(2010, 4, 6) == "Third Quarter"
    assert dic_calculator(2010, 4, 14) == "New Moon"
    assert dic_calculator(2010, 4, 21) == "First Quarter"
    assert dic_calculator(2010, 4, 28) == "Full Moon"
    assert dic_calculator(2010, 5, 5) == "Third Quarter"
    assert dic_calculator(2010, 5, 13) == "New Moon"
    assert dic_calculator(2010, 5, 20) == "First Quarter"
    assert dic_calculator(2010, 5, 27) == "Full Moon"
    assert dic_calculator(2010, 6, 4) == "Third Quarter"
    assert dic_calculator(2010, 6, 12) == "New Moon"
    assert dic_calculator(2010, 6, 18) == "First Quarter"
    assert dic_calculator(2010, 6, 26) == "Full Moon"
    assert dic_calculator(2010, 7, 4) == "Third Quarter"
    assert dic_calculator(2010, 7, 11) == "New Moon"
    assert dic_calculator(2010, 7, 18) == "First Quarter"
    assert dic_calculator(2010, 7, 25) == "Full Moon"
    assert dic_calculator(2010, 8, 2) == "Third Quarter"
    assert dic_calculator(2010, 8, 9) == "New Moon"
    assert dic_calculator(2010, 8, 16) == "First Quarter"
    assert dic_calculator(2010, 8, 24) == "Full Moon"
    assert dic_calculator(2010, 9, 1) == "Third Quarter"
    assert dic_calculator(2010, 9, 8) == "New Moon"
    assert dic_calculator(2010, 9, 14) == "First Quarter"
    assert dic_calculator(2010, 9, 23) == "Full Moon"
    assert dic_calculator(2010, 9, 30) == "Third Quarter"
    assert dic_calculator(2010, 10, 7) == "New Moon"
    assert dic_calculator(2010, 10, 14) == "First Quarter"
    assert dic_calculator(2010, 10, 22) == "Full Moon"
    assert dic_calculator(2010, 10, 30) == "Third Quarter"
    assert dic_calculator(2010, 11, 5) == "New Moon"
    assert dic_calculator(2010, 11, 13) == "First Quarter"
    assert dic_calculator(2010, 11, 21) == "Full Moon"
    assert dic_calculator(2010, 11, 28) == "Third Quarter"
    assert dic_calculator(2010, 12, 5) == "New Moon"
    assert dic_calculator(2010, 12, 13) == "First Quarter"
    assert dic_calculator(2010, 12, 21) == "Full Moon"
    assert dic_calculator(2010, 12, 27) == "Third Quarter"


def test_dic_calculator_2015():
    """Asserts if the moonphase is correct given the dates.

    Notes
    -----
    Dates are sourced from: https://www.almanac.com/astronomy/moon/calendar
    Writing asserts this way allows for immediate pin-pointing of issues.
    This test checks primary moon-phases (New, First, Full, Third) to assert if
    there is any significant deviation in the moon phase algorithm.
    This test checks for primary moon-phases of 2015.
    """
    assert dic_calculator(2015, 1, 4) == "Full Moon"
    assert dic_calculator(2015, 1, 13) == "Third Quarter"
    assert dic_calculator(2015, 1, 20) == "New Moon"
    assert dic_calculator(2015, 1, 26) == "First Quarter"
    assert dic_calculator(2015, 2, 3) == "Full Moon"
    assert dic_calculator(2015, 2, 11) == "Third Quarter"
    assert dic_calculator(2015, 2, 18) == "New Moon"
    assert dic_calculator(2015, 2, 25) == "First Quarter"
    assert dic_calculator(2015, 3, 5) == "Full Moon"
    assert dic_calculator(2015, 3, 13) == "Third Quarter"
    assert dic_calculator(2015, 3, 20) == "New Moon"
    assert dic_calculator(2015, 3, 27) == "First Quarter"
    assert dic_calculator(2015, 4, 4) == "Full Moon"
    assert dic_calculator(2015, 4, 11) == "Third Quarter"
    assert dic_calculator(2015, 4, 18) == "New Moon"
    assert dic_calculator(2015, 4, 25) == "First Quarter"
    assert dic_calculator(2015, 5, 3) == "Full Moon"
    assert dic_calculator(2015, 5, 11) == "Third Quarter"
    assert dic_calculator(2015, 5, 17) == "New Moon"
    assert dic_calculator(2015, 5, 25) == "First Quarter"
    assert dic_calculator(2015, 6, 2) == "Full Moon"
    assert dic_calculator(2015, 6, 9) == "Third Quarter"
    assert dic_calculator(2015, 6, 16) == "New Moon"
    assert dic_calculator(2015, 6, 24) == "First Quarter"
    assert dic_calculator(2015, 7, 1) == "Full Moon"
    assert dic_calculator(2015, 7, 8) == "Third Quarter"
    assert dic_calculator(2015, 7, 15) == "New Moon"
    assert dic_calculator(2015, 7, 23) == "First Quarter"
    assert dic_calculator(2015, 7, 31) == "Full Moon"
    assert dic_calculator(2015, 8, 6) == "Third Quarter"
    assert dic_calculator(2015, 8, 14) == "New Moon"
    assert dic_calculator(2015, 8, 22) == "First Quarter"
    assert dic_calculator(2015, 8, 29) == "Full Moon"
    assert dic_calculator(2015, 9, 5) == "Third Quarter"
    assert dic_calculator(2015, 9, 12) == "New Moon"
    assert dic_calculator(2015, 9, 21) == "First Quarter"
    assert dic_calculator(2015, 9, 27) == "Full Moon"
    assert dic_calculator(2015, 10, 4) == "Third Quarter"
    assert dic_calculator(2015, 10, 12) == "New Moon"
    assert dic_calculator(2015, 10, 20) == "First Quarter"
    assert dic_calculator(2015, 10, 27) == "Full Moon"
    assert dic_calculator(2015, 11, 3) == "Third Quarter"
    assert dic_calculator(2015, 11, 11) == "New Moon"
    assert dic_calculator(2015, 11, 18) == "First Quarter"
    assert dic_calculator(2015, 11, 25) == "Full Moon"
    assert dic_calculator(2015, 12, 2) == "Third Quarter"
    assert dic_calculator(2015, 12, 11) == "New Moon"
    assert dic_calculator(2015, 12, 18) == "First Quarter"
    assert dic_calculator(2015, 12, 25) == "Full Moon"


def test_dic_calculator_2020():
    """Asserts if the moonphase is correct given the dates.

    Notes
    -----
    Dates are sourced from: https://www.almanac.com/astronomy/moon/calendar
    Writing asserts this way allows for immediate pin-pointing of issues.
    This test checks primary moon-phases (New, First, Full, Third) to assert
    if there is any significant deviation in the moon phase algorithm.
    This test checks for primary moon-phases of 2020.
    """
    assert dic_calculator(2020, 1, 2) == "First Quarter"
    assert dic_calculator(2020, 1, 10) == "Full Moon"
    assert dic_calculator(2020, 1, 17) == "Third Quarter"
    assert dic_calculator(2020, 1, 24) == "New Moon"
    assert dic_calculator(2020, 2, 1) == "First Quarter"
    assert dic_calculator(2020, 2, 8) == "Full Moon"
    assert dic_calculator(2020, 2, 15) == "Third Quarter"
    assert dic_calculator(2020, 2, 23) == "New Moon"
    assert dic_calculator(2020, 3, 2) == "First Quarter"
    assert dic_calculator(2020, 3, 9) == "Full Moon"
    assert dic_calculator(2020, 3, 16) == "Third Quarter"
    assert dic_calculator(2020, 3, 24) == "New Moon"
    assert dic_calculator(2020, 4, 1) == "First Quarter"
    assert dic_calculator(2020, 4, 7) == "Full Moon"
    assert dic_calculator(2020, 4, 14) == "Third Quarter"
    assert dic_calculator(2020, 4, 22) == "New Moon"
    assert dic_calculator(2020, 4, 30) == "First Quarter"
    assert dic_calculator(2020, 5, 7) == "Full Moon"
    assert dic_calculator(2020, 5, 14) == "Third Quarter"
    assert dic_calculator(2020, 5, 22) == "New Moon"
    assert dic_calculator(2020, 5, 29) == "First Quarter"
    assert dic_calculator(2020, 6, 5) == "Full Moon"
    assert dic_calculator(2020, 6, 12) == "Third Quarter"
    assert dic_calculator(2020, 6, 20) == "New Moon"
    assert dic_calculator(2020, 6, 28) == "First Quarter"
    assert dic_calculator(2020, 7, 4) == "Full Moon"
    assert dic_calculator(2020, 7, 12) == "Third Quarter"
    assert dic_calculator(2020, 7, 20) == "New Moon"
    assert dic_calculator(2020, 7, 27) == "First Quarter"
    assert dic_calculator(2020, 8, 3) == "Full Moon"
    assert dic_calculator(2020, 8, 11) == "Third Quarter"
    assert dic_calculator(2020, 8, 18) == "New Moon"
    assert dic_calculator(2020, 8, 25) == "First Quarter"
    assert dic_calculator(2020, 9, 1) == "Full Moon"
    assert dic_calculator(2020, 9, 10) == "Third Quarter"
    assert dic_calculator(2020, 9, 17) == "New Moon"
    assert dic_calculator(2020, 9, 23) == "First Quarter"
    assert dic_calculator(2020, 10, 1) == "Full Moon"
    assert dic_calculator(2020, 10, 9) == "Third Quarter"
    assert dic_calculator(2020, 10, 16) == "New Moon"
    assert dic_calculator(2020, 10, 23) == "First Quarter"
    assert dic_calculator(2020, 10, 31) == "Full Moon"
    assert dic_calculator(2020, 11, 8) == "Third Quarter"
    assert dic_calculator(2020, 11, 14) == "New Moon"
    assert dic_calculator(2020, 11, 21) == "First Quarter"
    assert dic_calculator(2020, 11, 30) == "Full Moon"
    assert dic_calculator(2020, 12, 7) == "Third Quarter"
    assert dic_calculator(2020, 12, 14) == "New Moon"
    assert dic_calculator(2020, 12, 21) == "First Quarter"
    assert dic_calculator(2020, 12, 29) == "Full Moon"


def test_dic_calculator_2025():
    """Asserts if the moonphase is correct given the dates.

    Notes
    -----
    Dates are sourced from: https://www.almanac.com/astronomy/moon/calendar
    Writing asserts this way allows for immediate pin-pointing of issues.
    This test checks primary moon-phases (New, First, Full, Third) to assert if
    there is any significant deviation in the moon phase algorithm.
    This test checks for primary moon-phases of 2025.
    """
    assert dic_calculator(2025, 1, 6) == "First Quarter"
    assert dic_calculator(2025, 1, 13) == "Full Moon"
    assert dic_calculator(2025, 1, 21) == "Third Quarter"
    assert dic_calculator(2025, 1, 29) == "New Moon"
    assert dic_calculator(2025, 2, 5) == "First Quarter"
    assert dic_calculator(2025, 2, 12) == "Full Moon"
    assert dic_calculator(2025, 2, 20) == "Third Quarter"
    assert dic_calculator(2025, 2, 27) == "New Moon"
    assert dic_calculator(2025, 3, 6) == "First Quarter"
    assert dic_calculator(2025, 3, 13) == "Full Moon"
    assert dic_calculator(2025, 3, 22) == "Third Quarter"
    assert dic_calculator(2025, 3, 29) == "New Moon"
    assert dic_calculator(2025, 4, 4) == "First Quarter"
    assert dic_calculator(2025, 4, 12) == "Full Moon"
    assert dic_calculator(2025, 4, 20) == "Third Quarter"
    assert dic_calculator(2025, 4, 27) == "New Moon"
    assert dic_calculator(2025, 5, 4) == "First Quarter"
    assert dic_calculator(2025, 5, 12) == "Full Moon"
    assert dic_calculator(2025, 5, 20) == "Third Quarter"
    assert dic_calculator(2025, 5, 26) == "New Moon"
    assert dic_calculator(2025, 6, 2) == "First Quarter"
    assert dic_calculator(2025, 6, 11) == "Full Moon"
    assert dic_calculator(2025, 6, 18) == "Third Quarter"
    assert dic_calculator(2025, 6, 25) == "New Moon"
    assert dic_calculator(2025, 7, 2) == "First Quarter"
    assert dic_calculator(2025, 7, 10) == "Full Moon"
    assert dic_calculator(2025, 7, 17) == "Third Quarter"
    assert dic_calculator(2025, 7, 24) == "New Moon"
    assert dic_calculator(2025, 8, 1) == "First Quarter"
    assert dic_calculator(2025, 8, 9) == "Full Moon"
    assert dic_calculator(2025, 8, 15) == "Third Quarter"
    assert dic_calculator(2025, 8, 22) == "New Moon"
    assert dic_calculator(2025, 8, 30) == "First Quarter"
    assert dic_calculator(2025, 9, 7) == "Full Moon"
    assert dic_calculator(2025, 9, 14) == "Third Quarter"
    assert dic_calculator(2025, 9, 21) == "New Moon"
    assert dic_calculator(2025, 9, 29) == "First Quarter"
    assert dic_calculator(2025, 10, 6) == "Full Moon"
    assert dic_calculator(2025, 10, 13) == "Third Quarter"
    assert dic_calculator(2025, 10, 21) == "New Moon"
    assert dic_calculator(2025, 10, 29) == "First Quarter"
    assert dic_calculator(2025, 11, 5) == "Full Moon"
    assert dic_calculator(2025, 11, 11) == "Third Quarter"
    assert dic_calculator(2025, 11, 19) == "New Moon"
    assert dic_calculator(2025, 11, 27) == "First Quarter"
    assert dic_calculator(2025, 12, 4) == "Full Moon"
    assert dic_calculator(2025, 12, 11) == "Third Quarter"
    assert dic_calculator(2025, 12, 19) == "New Moon"
    assert dic_calculator(2025, 12, 27) == "First Quarter"


def test_dic_calculator_2030():
    """Asserts if the moonphase is correct given the dates.

    Notes
    -----
    Dates are sourced from: https://www.almanac.com/astronomy/moon/calendar
    Writing asserts this way allows for immediate pin-pointing of issues.
    This test checks primary moon-phases (New, First, Full, Third) to assert if
    there is any significant deviation in the moon phase algorithm.
    This test checks for primary moon-phases of 2030.
    """
    assert dic_calculator(2030, 1, 3) == "New Moon"
    assert dic_calculator(2030, 1, 11) == "First Quarter"
    assert dic_calculator(2030, 1, 19) == "Full Moon"
    assert dic_calculator(2030, 1, 26) == "Third Quarter"
    assert dic_calculator(2030, 2, 2) == "New Moon"
    assert dic_calculator(2030, 2, 10) == "First Quarter"
    assert dic_calculator(2030, 2, 17) == "Full Moon"
    assert dic_calculator(2030, 2, 24) == "Third Quarter"
    assert dic_calculator(2030, 3, 3) == "New Moon"
    assert dic_calculator(2030, 3, 12) == "First Quarter"
    assert dic_calculator(2030, 3, 19) == "Full Moon"
    assert dic_calculator(2030, 3, 26) == "Third Quarter"
    assert dic_calculator(2030, 4, 2) == "New Moon"
    assert dic_calculator(2030, 4, 10) == "First Quarter"
    assert dic_calculator(2030, 4, 17) == "Full Moon"
    assert dic_calculator(2030, 4, 24) == "Third Quarter"
    assert dic_calculator(2030, 5, 2) == "New Moon"
    assert dic_calculator(2030, 5, 10) == "First Quarter"
    assert dic_calculator(2030, 5, 17) == "Full Moon"
    assert dic_calculator(2030, 5, 23) == "Third Quarter"
    assert dic_calculator(2030, 5, 31) == "New Moon"
    assert dic_calculator(2030, 6, 8) == "First Quarter"
    assert dic_calculator(2030, 6, 15) == "Full Moon"
    assert dic_calculator(2030, 6, 22) == "Third Quarter"
    assert dic_calculator(2030, 6, 30) == "New Moon"
    assert dic_calculator(2030, 7, 8) == "First Quarter"
    assert dic_calculator(2030, 7, 14) == "Full Moon"
    assert dic_calculator(2030, 7, 22) == "Third Quarter"
    assert dic_calculator(2030, 7, 30) == "New Moon"
    assert dic_calculator(2030, 8, 6) == "First Quarter"
    assert dic_calculator(2030, 8, 13) == "Full Moon"
    assert dic_calculator(2030, 8, 20) == "Third Quarter"
    assert dic_calculator(2030, 8, 28) == "New Moon"
    assert dic_calculator(2030, 9, 4) == "First Quarter"
    assert dic_calculator(2030, 9, 11) == "Full Moon"
    assert dic_calculator(2030, 9, 19) == "Third Quarter"
    assert dic_calculator(2030, 9, 27) == "New Moon"
    assert dic_calculator(2030, 10, 3) == "First Quarter"
    assert dic_calculator(2030, 10, 11) == "Full Moon"
    assert dic_calculator(2030, 10, 19) == "Third Quarter"
    assert dic_calculator(2030, 10, 26) == "New Moon"
    assert dic_calculator(2030, 11, 2) == "First Quarter"
    assert dic_calculator(2030, 11, 9) == "Full Moon"
    assert dic_calculator(2030, 11, 18) == "Third Quarter"
    assert dic_calculator(2030, 11, 24) == "New Moon"
    assert dic_calculator(2030, 12, 1) == "First Quarter"
    assert dic_calculator(2030, 12, 9) == "Full Moon"
    assert dic_calculator(2030, 12, 17) == "Third Quarter"
    assert dic_calculator(2030, 12, 24) == "New Moon"
    assert dic_calculator(2030, 12, 31) == "First Quarter"
