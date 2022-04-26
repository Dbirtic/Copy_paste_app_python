from ctypes.wintypes import WORD
import tkinter
from tkinter import END, VERTICAL, Button, Entry, ttk
from tkinter.messagebox import showinfo

# key down function
"""def click():
    entered_text = textentry.get() # this will collect the text from the textbox
    output.delete(0.0, END)
    try:
        definition = my_dict[entered_text]
    except:
        definition = "sorry, there is no word like that please try again"
    output.insert(END, definition)
"""
window = tkinter.Tk()
window.title("Window")

# adjust window/frame size
window.geometry("600x600")

frm = ttk.Frame(window, padding=10)
frm.grid()

# create label
#ttk.Label(frm, text="Hi man!", font="none 12").grid(row=0, column=0, sticky=tkinter.E)
#ttk.Button(frm, text="Quit", command=window.destroy).grid(column=0, row=3)
# create a text entry box
#textentry = Entry(frm, width=20, bg="white")
#textentry.grid(row=2, column=0, sticky=tkinter.W)

# add a submit button
#Button(window, text="SUBMIT", width=6, command=click).grid(row=3, column=0)

# create another label
#ttk.Label(frm, text="\nDefinition:", font="none 12 bold").grid(row=4, column=0, sticky=tkinter.W)

# define columns
columns = ('first_name', 'last_name', 'email')

tree = ttk.Treeview(frm, columns=columns, show='headings')

# define headings
tree.heading('first_name', text='First Name')
tree.heading('last_name', text='Last Name')
tree.heading('email', text='Email')

# generate sample data
contacts = []
for n in range(1, 100):
    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

# add data to the treeview
for contact in contacts:
    tree.insert('', END, values=contact)

def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=0, column=0, sticky='nsew')

# create a text box
#output = tkinter.Text(frm, width=50, height=6, wrap="word")
#output.grid(row=5, column=0, columnspan=2, sticky=tkinter.W)

# add a scrollbar
scrollbar = ttk.Scrollbar(frm, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# the dictionary
my_dict = {'algorithm': 'Step by step instructions to complete a task', 'bug': 'piece of code that causes program to fail'}

# run the main loop
window.mainloop()