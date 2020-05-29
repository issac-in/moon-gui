import csv
import string
import datetime as dt

import requests
from bs4 import BeautifulSoup


def dic_interpreter(days_into_cycle: float):
	"""Given the days into cycle (dic), determine the moon phase.

	Parameter
	---------
	days_into_cycle : float
		Days into the current synodic period of the moon.

	Returns
	-------
	phase : str
		The phase corresponding to the day of the synodic period.

	Notes
	-----
	Synodic period = the new moon -> new moon period. (~29.53 days)
	These numbers, I computed & fine-tuned on my own, since they
	were not provided by anyone online. These numbers are what make
	the moon phase computations rigorous. 
	"""
	dic = days_into_cycle

	if (dic <= 2.03) or (dic >= 28.68):
		phase = "New Moon"
	elif 2.03 < dic < 6.01:
		phase = "Waxing Crescent"
	elif 6.01 <= dic < 9.27:
		phase = "First Quarter"
	elif 9.27 <= dic < 13.55:
		phase = "Waxing Gibbous"
	elif 13.55 <= dic < 16.68:
		phase = "Full Moon"
	elif 16.68 <= dic < 21.00:
		phase = "Waning Gibbous"
	elif 21.00 <= dic < 24.07:
		phase = "Third Quarter"
	elif 24.07 <= dic < 28.68:
		phase = "Waning Crescent"

	return phase


def dic_calculator(int_year: int, int_month: int, int_day: int):
	"""Given year/month/day, calculate days into cycle of synodic period.
	(1) Given year/month/day, calculate Julian Day (JD).
	(2) Given JD, find # of days since a known new moon (Jan 6, 2000).
	(3) Divide # of days by the average synodic period (29.53059).
	(4) Drop the whole # to get fraction of current synodic period.
	(5) Multiple fraction by average synodic period to get days into cycle.
	(6) Get moon phase corresponding to days into cycle.

	Parameters
	----------
	int_year : int
		Example: 2020
	int_month : int
		Example: 5
	in_day : int
		Example: 28

	Returns
	-------
	dic_interpreter(days_into_cycle) : str
		Gives the moon phase corresponding to year/month/day.

	Citation
	--------
	Title: Calculate the Moon Phase
	Author: SubsySTEMs
	Date: 2017
	Code version: N/A
	Availability: https://tinyurl.com/ycnl6vs7

	Notes
	-----
	There was no code copied from external sources.
	However, all of the formulas in this function are from SubsySTEMs.
	1/6/2000 is the earliest date this function can compute moon phase.
	"""

	# "If the month is January or February, 
	#  subtract 1 from the year and add 12 to the month" (SubsySTEMs)
	if int_month <= 2:
		int_year -= 1
		int_month += 12
	
	component_1 = 2 - (int_year/100) + ((int_year/100)/4)
	component_2 = 365.25 * (int_year+4716)
	component_3 = 30.6001 * (int_month+1) 
	julian_day = component_1 + int_day + component_2 + component_3 - 1524.5

	# 2451549.5 is the Julian Day for January 6th, 2000;
	# The earliest known new moon date within this function.
	days_since_new = julian_day - 2451549.5
	new_moons_cycles = days_since_new / 29.53059 
	fraction_of_current_synodic_period = new_moons_cycles - int(new_moons_cycles)
	days_into_cycle = fraction_of_current_synodic_period * 29.53059

	return dic_interpreter(days_into_cycle)


def city_format(us_city: str):
	"""Format city name for web-scraping.
	
	Parameter
	---------
	us_city : str
		A city in the United States. (Example: "San Diego")

	Returns
	-------
	formatted_city : str
		A city that is formatted. (Example: "san-diego")

	Citation
	--------
	Title: COGS 18 - Assignment 3: Chatbots
	Author: Shannon Ellis
	Date: 2020
	Code Version: Spring 2020
	Availability: A3 Q10 (Removing punctuation) & Q11 (Preparing text).

	Notes
	-----
	Slightly modified from A3 Q10 & Q11 to suit my project's needs.
	"""
	formatted_city = ''

	for char in us_city.lower():
		if (char == "’") or (char not in string.punctuation):
			formatted_city += char

	formatted_city = formatted_city.replace(" ","-").replace("’","-")

	return formatted_city


def moon_scraper(us_city: str, year: (str,int), month: (str,int), day: (str,int)):
	"""Get the moonrise & moonset of a given US city & date.
	(1) Obtain formatted US city & scrape website table given year/month.
	(2) If it doesn't work out, it'll let you know. Otherwise,
	(3) Access the table row corresponding to given day.
	(4) Scrape the moonrise and moonset content, and save it in a list.

	Parameters
	----------
	us_city : str
		A city in the United States.
	year : str or int
		Speaks for itself. (Example: "2020" or 2020)
	month : str or int
		Speaks for itself. (Example: "5" or 5)
	day : str or int
		Speaks for itself. (Example: "28" or 28)
	
	Returns
	-------
	moon_outputs : list
		Returns a list of moonrise/moonset. (Example: ["moonrise","moonset"])

	Citation
	--------
	Title: Sunrise Sunset Scraper
	Author: Michael Pereira (@monkeycycle)
	Date: July 3rd, 2018
	Code Version: Version 1
	Availability: https://tinyurl.com/yd49exdb

	Notes
	-----
	I am consider this code to be part of my graded project code.

	I started out with the source code in the link, but I significantly
	modified it. It's quite different, in what it does and how it goes
	about doing so. But it felt right to credit what helped me start during
	a mental road-block during the coding process.

	Technically web-scraping, because I am scraping a website for its data.
	However, the way I do it does not put any remotely significant load on
	the website, and how the user can interact with this is not in a way
	that would ever impact the website I am scraping. Additionally, the
	data isn't being saved to a local file - running this wil require
	internet access. Lastly, the robots.txt didn't seem to have anything
	against crawling the specific part of the website that I did, so I
	should be fine.
	"""

	city = city_format(us_city)
	link = (f"https://www.timeanddate.com/moon/"
			f"usa/{city}?month={month}&year={year}")
	page = requests.get(link)
	soup = BeautifulSoup(page.content,'html.parser')

	# This is the specific table with the moonrise/moonset data.
	table_moon = soup.find(id="tb-7dmn")

	moon_outputs = []
	if table_moon == None:
		moon_outputs = ["Invalid City Name OR","No Moonrise/set time exists"]
	else:
		table_moon_body = table_moon.find('tbody')
		table_moon_rows = table_moon_body.find_all('tr')
		output = ""
		for row in table_moon_rows:
			# If we find the matching row day with the input day...
			if int(row.contents[0].text.strip()) == int(day):
				content_counter = 1
				raw_list = []
				while content_counter <= 5:
					content_str = row.contents[content_counter].text
					# These specifically because it's critical to intended output.
					if ("-" in content_str) or ("am" in content_str) or ("pm" in content_str):
						raw_list.append(content_str)
					content_counter += 1
				# If day is earlier in month, don't have to iterate through rest.
				break

		# If there is, the 4th element is always junk-data.		
		if len(raw_list) > 3:
			raw_list.pop()
		
		# the website I'm scraping has 2 moonrise columns
		# so raw_list[0] & raw_list[2] are moonrise 1 & 2 
		# (& raw_list[1] is moonset).
		# raw_list[0] & raw_list[2] possible outputs are "-" or "XX:XX am/pm"
		# hence comparing len is a very good idea to get the data I want.
		if len(raw_list[0]) == len(raw_list[2]):
			moon_outputs.append("No moonrise")
		elif len(raw_list[0]) > len(raw_list[2]):
			moon_outputs.append(raw_list[0])
		elif len(raw_list[0]) < len(raw_list[2]):
			moon_outputs.append(raw_list[2])

		if "-" in raw_list[1]:
			moon_outputs.append("No moonset")
		elif "-" not in raw_list[1]:
			moon_outputs.append(raw_list[1])

	return moon_outputs


def date_check(str_city: str, str_year: str, str_month: str, str_day: str):
	"""Validate date & obtain moon phase, moon-rise, and moon-set.

	Parameters
	----------
	str_city, stry_year, str_month, str_day : str
		These are meant to be str, because their input data is from the GUI.
		And the GUI data, when accessed, are type string.

	Returns
	-------
	list_output : list
		The output will always be ["moonrise","moonset","moon phase"]
	"""
	valid_date = True

	try:
		year = int(str_year)
		month = int(str_month)
		day = int(str_day)
		# To confirm if the date is legitimate or not.
		input_date = dt.datetime(year, month, day)

	# If any of these are produced, then input parameters are bad.
	except (SyntaxError, ValueError, TypeError):
		valid_date = False

	# To hard-enforce limitation of dic_calculator() for accuracy-sake.
	if valid_date and (input_date >= dt.datetime(2000,1,6)):
		moon_phase = dic_calculator(year, month, day)
		moon_rise_and_set = moon_scraper(str_city, year, month, day)
	elif valid_date and (input_date <= dt.datetime(2000,1,6)):
		moon_phase = "Can't compute before 1-6-2000"
		moon_rise_and_set = moon_scraper(str_city, year, month, day)
	else:
		# Cannot compute anything w/o the date.
		moon_phase = "Invalid Date"
		moon_rise_and_set = ["Invalid Date","Invalid Date"]

	moon_rise_and_set.append(moon_phase)
	# Defined it this way, so that people who look at this are not
	# confused when moon_rise_and_set has the moon phase in it too.
	list_output = moon_rise_and_set

	return list_output