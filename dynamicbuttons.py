class Item():

    def __init__(self, name, value):
        self._name = name
        self._value = value

        all_items.append(self)

    def get_name(self):
        ''' Return name of item '''

        return self._name

    def get_value(self):
        ''' Return value of item '''

        return self._value


def generate_items():
    ''' Import students from a csv file'''
    # Import the csv package to enable the program to work with a csv
    import csv
    # Open the csv file, call is csvfile
    with open('products2.csv', newline='') as csvfile:
        # use the reader() function and put the results into a variable called filereader
        filereader = csv.reader(csvfile)
        # Loop through the csv, one row at a time

        for line in filereader:
            # For each row, create a new item

            Item(line[0], int(line[1]))


# function to print value
def print_value(v):
    print(v)
    item_value.set(f"${v}")


# Import tkinter
from tkinter import *
from functools import partial

# List to store all items
all_items = []

# Create items by importing from csv
generate_items()

# Create GUI
root = Tk()
root.title("Dynamic buttons")
root.resizable(width=FALSE, height=FALSE)
root.geometry("600x400")
root.configure(bg="grey")
item_value = IntVar()
value_lbl = Label(root, textvariable=item_value, bg="grey")
value_lbl.grid(row=2, column=4)



# Create button for each item
col = 0
for i in all_items:
    btn = Button(root, text=i.get_name(), command=partial(print_value, i.get_value()), bg="white")
    btn.grid(row=0, column=col, padx=5)
    col += 1

root.mainloop()