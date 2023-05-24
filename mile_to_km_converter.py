#  Written by Nahom Atnafu
#  Last modified: 5/23/2023
from tkinter import *

#  Converter Method


def convert():
    mileValue = float(milesInput.get())
    kmValue = mileValue * 1.609
    kilometer_result_label.config(text=f"{kmValue}")

#  Window


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=15, pady=15)
window.minsize(width=335, height=100)


#  Button


calculateButton = Button(text="Calculate", command=convert)
calculateButton.grid(column=1, row=2)

#  Entry

milesInput = (Entry(width=8))
milesInput.grid(column=1, row=0)


#  Label
milesLabel = Label(text="Miles")
milesLabel.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text=0)
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

window.mainloop()
