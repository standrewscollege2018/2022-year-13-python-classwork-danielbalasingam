######### Set up the GUI ##############
from tkinter import *
from tkinter import messagebox

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


def print_selection():
    ''' Print out the selected item '''

    print(items_listbox.curselection())
    for num in items_listbox.curselection():
        print(all_items[num].get_name())
        # Display name and value in a label
        details.set(f"{all_items[num].get_name()} costs ${all_items[num].get_value()}")

def delete_item():
    ''' Delete the selected item '''
    for num in items_listbox.curselection():
        if messagebox.askyesno("Warning", f"Are you sure that you want to delete this?") == True:
            del all_items[num]
    items_listbox.delete(0, END)
    populate_listbox()

def populate_listbox():
    # Populate listbox with names of items
    for i in all_items:
        items_listbox.insert(END, i.get_name())

def add_items():
    name = newname.get()
    price = newprice.get()
    all_items.append([name, price])

# List of all objects
all_items = []

# Import the items from csv file
generate_items()

print(all_items)

root = Tk()
root.title("Listbox demo")
root.geometry("800x500")

# Set up listbox
items_listbox = Listbox(root, selectmode=SINGLE)
items_listbox.grid(rowspan=5)

# Button to enter selection
select_btn = Button(root, text="Select", command=print_selection)
select_btn.grid(row=6)
populate_listbox()

# Label to display information about selected item
details = StringVar()
details_lbl = Label(root, textvariable=details)
details_lbl.grid(row=7)

delete_btn = Button(root, text="Delete", command=delete_item)
delete_btn.grid(row=6, column=1)

l1 = Label(root, text="Add new item.")
l1.grid(row=0, column=2)

l2 = Label(root, text="Name:")
l2.grid(row=1, column=2)
newname = Entry(root)
newname.grid(row=1, column=3)

l3 = Label(root, text="Price:")
l3.grid(row=2, column=2)
newprice = Entry(root)
newprice.grid(row=2, column=3)

add_btn = Button(root, text="Add", command=add_items)
add_btn.grid(row=6, column=3)

root.mainloop()