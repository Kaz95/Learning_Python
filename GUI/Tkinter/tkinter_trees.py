from tkinter import *
from tkinter import ttk

root = Tk()     # Tk() Creates main window

shipyard_treeview = ttk.Treeview(root)   # ttk.Treeview(parent) Sets a treeview to a given parent window
general_store_treeview = ttk.Treeview(root)
blacksmith_treeview = ttk.Treeview(root)
stables_treeview = ttk.Treeview(root)
inventory_treeview = ttk.Treeview(root)

i = ['Galley', '251', '1']
a = ['Warship', '256', '1']


def callback(event):
    print(shipyard_treeview.selection())  # Gets tuple with id as first value
    # print(treeview.set('I001', 'quantity'))
    # print(treeview.item('I001'))
    tup = shipyard_treeview.selection()
    # Gets value of quantity for item selected.
    # Quantity can be swapped for another column
    print(shipyard_treeview.set(tup[0], 'quantity'))
    print(shipyard_treeview.item(tup[0])['text'])    # Gets name of item selected


# General grid formatting
general_store_treeview.grid(row=0, column=0)
blacksmith_treeview.grid(row=0, column=1)
stables_treeview.grid(row=0, column=2)
shipyard_treeview.grid(row=0, column=3)
inventory_treeview.grid(row=1, columnspan=4, sticky=W+E, pady=50)

# Gen Store formatting
general_store_treeview.config(columns='quantity')
general_store_treeview.column('quantity', width=55, anchor='center')
general_store_treeview.column('#0', width=150)
general_store_treeview.heading('quantity', text='Quantity')
general_store_treeview.heading('#0', text='Item')

# Blacksmith formatting
blacksmith_treeview.config(columns='quantity')
blacksmith_treeview.column('quantity', width=55, anchor='center')
blacksmith_treeview.column('#0', width=150)
blacksmith_treeview.heading('quantity', text='Quantity')
blacksmith_treeview.heading('#0', text='Item')

# Stables formatting
stables_treeview.config(columns='quantity')
stables_treeview.column('quantity', width=55, anchor='center')
stables_treeview.column('#0', width=150)
stables_treeview.heading('quantity', text='Quantity')
stables_treeview.heading('#0', text='Item')

# Shipyard formatting
shipyard_treeview.config(columns='quantity')
shipyard_treeview.column('quantity', width=55, anchor='center')
shipyard_treeview.heading('quantity', text='Quantity')
shipyard_treeview.column('#0', width=150)
shipyard_treeview.heading('#0', text='Item')

# Inventory formatting
inventory_treeview.config(columns='quantity')
inventory_treeview.column('quantity', width=55, anchor='center')
inventory_treeview.heading('quantity', text='Quantity')
inventory_treeview.column('#0', width=550)
inventory_treeview.heading('#0', text='Item')

# Shipyard values
shipyard_treeview.insert('', 'end', i[1], text=i[0])
shipyard_treeview.insert('', 'end', a[1], text=a[0])
shipyard_treeview.set(i[1], 'quantity', i[2])
shipyard_treeview.set(a[1], 'quantity', a[2])
shipyard_treeview.bind('<<TreeviewSelect>>', callback)

root.mainloop()
