import sys
sys.path.append('../')

import tkinter as tk
from tkinter import font

from PIL import Image, ImageTk

from moon_module.functions import date_check


"""This is what makes the moon GUI, the GUI it is.

Citations
---------
Title: Stackoverflow : tkinter gui layout using frames and grid
Author: Bryan Oakley
Date: December 14th, 2015
Code Version: N/A
Availability: https://tinyurl.com/y836fcwk

Title: Tkinter 8.5 reference: a GUI for Python
Author: John W. Shipman
Date: December 31st, 2013
Code Version: N/A
Availability: https://tinyurl.com/y7f3csvx

Notes
-----
I didn't copy-paste, but I heavily mimicked the structure
of Bryan Oakley's suggested response on Stackoverflow, because
it made a lot of sense, and the readability is pretty good.
I used his structure in tandem with a tkinter reference guide.

So even if I was heavily inspired by his response, I consider
this code to be my own, because I didn't just slap it in, I 
tuned a lot of the things to my specific project.
"""
root = tk.Tk()
root.title("Moon Info GUI")
root.iconbitmap("../moon_images/moon.ico")
root.resizable(width=False, height=False)

default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="Verdana",size=9)

# create the main containers
frame_date = tk.Frame(root, bg="gray32", width=310, height=30, padx=4, pady=4)
frame_city = tk.Frame(root, bg="gray32", width=310, height=30, padx=4, pady=4)
frame_img = tk.Frame(root, bg="gray32", width=310, height=310, padx=4, pady=2)
frame_info = tk.Frame(root, bg="gray32", width=310, height=90, padx=4, pady=4)

# layout the main containers
frame_date.grid(row=0, sticky="ew")
frame_city.grid(row=1, sticky="ew")
frame_img.grid(row=2, sticky="ew")
frame_info.grid(row=3, sticky="ew")

# widgets for frame_date
label_date = tk.Label(frame_date, text="Date:")
label_month = tk.Label(frame_date, text="MM")
label_day = tk.Label(frame_date, text="DD")
label_year = tk.Label(frame_date, text="YYYY")
entry_month = tk.Entry(frame_date, width=3)
entry_day = tk.Entry(frame_date, width=3)
entry_year = tk.Entry(frame_date, width=5)

# layout for frame_date
label_date.grid(row=0)
label_month.grid(row=0, column=1, padx=6)
label_day.grid(row=0, column=3, padx=6)
label_year.grid(row=0, column=5, padx=6)
entry_month.grid(row=0, column=2)
entry_day.grid(row=0, column=4)
entry_year.grid(row=0, column=6)

# widgets for frame_city
label_city = tk.Label(frame_city, text="US City:")
entry_city = tk.Entry(frame_city, width=24)

# layout for frame_city
label_city.grid(row=0)
entry_city.grid(row=0,column=1, padx=6)

# widgets for frame_img
img_default = "../moon_images/moon_phases/Invalid Date.png"
img_moon = ImageTk.PhotoImage(Image.open(img_default))
label_img = tk.Label(frame_img, image=img_moon)

# layout for frame_img
label_img.grid(row=0)

# widgets for frame_info
label_phase = tk.Label(frame_info, text="Moon Phase:")
label_rise = tk.Label(frame_info, text="Moonrise:")
label_set = tk.Label(frame_info, text="Moonset:")
phase_input = tk.Label(frame_info, text="Awaiting Moon Phase")
rise_input = tk.Label(frame_info, text="Awaiting Moon Rise")
set_input = tk.Label(frame_info, text="Awaiting Moon Set")

# layout for frame_info
label_phase.grid(row=0, sticky="w", padx=(0,5))
label_rise.grid(row=1, sticky="w", pady=4)
label_set.grid(row=2, sticky="w")
phase_input.grid(row=0, column=1, sticky="w")
rise_input.grid(row=1, column=1, sticky="w")
set_input.grid(row=2, column=1, sticky="w")


def upon_click():
	"""Takes GUI inputs & outputs moonphase, pic of phase, & moonrise/set.
	When a user types in inputs and clicks the button in the GUI,
	this will get the corresponding moonphase, moonrise/set. AND,
	it will also get the corresponding moonphase image to match!
	
	Citations
	---------
	(0) Title: The Tkinter PhotoImage Class
	Author: Unknown
	Date: Unknown
	Code Version: N/A
	Availability: https://tinyurl.com/3bnlgx

	(1) Title: Why do my Tkinter images not appear?
	Author: Unknown
	Date: Unknown
	Code Version: N/A
	Availability: https://tinyurl.com/v8p9b

	(2) Title: Stackoverflow : How do you replace a label in Tkinter python?
	Author: Bryan Oakley
	Date: December 8th, 2013
	Code Version: N/A
	Availability: https://tinyurl.com/ydcab26a
	"""
	get_year = entry_year.get()
	get_month = entry_month.get()
	get_day = entry_day.get()

	# If no city given, default to "San Diego" because I had a habit of not
	# inputting any city parameter, so I hope this helps users like me.
	if entry_city.get() == "":
		get_city = "San Diego"
	else:
		get_city = entry_city.get()

	# output of moon_info = ["moonrise","moonset","moon phase"]
	moon_info = date_check(get_city, get_year, get_month, get_day)

	phase_img_loc = f"../moon_images/moon_phases/{moon_info[2]}.png"
	# (0) I'm not risking an AI violation for no citation.
	phase_img = ImageTk.PhotoImage(Image.open(phase_img_loc))

	label_img = tk.Label(frame_img, image=phase_img)
	# (1) To avoid having blank images on GUI input changes.
	label_img.image = phase_img
	label_img.grid(row=0)

	# (2) This allows GUI input texts to update, w/o overlaying each other.
	phase_input.configure(text=moon_info[2])
	rise_input.configure(text=moon_info[0])
	set_input.configure(text=moon_info[1])

# widget & layout for input button
button_input = tk.Button(frame_date, 
	text="Enter", width=4, command=upon_click)
button_input.grid(row=0, column=7, padx=(9,0))

root.mainloop()