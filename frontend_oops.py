from tkinter import *
from backend_oops import Database

db = Database()

def get_selected_entry(event):
    # event is a special parameter which holds the information about the type of event
    # So python knows when we pass the function to bind it expects it to have the event parameter

    global selected_tuple

    try:
        index = list.curselection()[0]   # So we do not get the tuple but the number
        selected_tuple = list.get(index)
        # print(index)
        # return selected_tuple
        # Now to fill the entry widget with the selected_tuple
        et.delete(0, END)
        et.insert(END,selected_tuple[1])

        ea.delete(0, END)
        ea.insert(END, selected_tuple[2])

        ey.delete(0, END)
        ey.insert(END, selected_tuple[3])

        eid.delete(0, END)
        eid.insert(END, selected_tuple[4])
    except IndexError:
        pass
        # print("Please first view the list...")
        # list.delete(0, END)
        # list.insert(END,("Please first view the list...") )


def view_command():
    list.delete(0, END)
    """
    We want to insert each of the tuple of the list as a new row in the ListBox
    So for that we iterate through the list.
    END ensures that every new row is inserted at the end of the existing rows
    in the ListBox.
    """
    for row in db.view():
        # print(row)
        list.insert(END, row)  # [1: ] helps us displaying everything except the id
    # Still we have a problem, when we press it again the ListBox gets appended
    # For that we've written  "list.delete(0, END)"

def search_command():
    list.delete(0, END) # To empty the list
    """
    Now iteating throgh the backend function.

    To pass the parameters we use the entry widgets as they kepp track of
    what the user has written...

    We need to append the parameter with the get() method as it is a StringVar object
    """
    for row in db.search(et_value.get(), ea_value.get(), ey_value.get(), eid_value.get()):
        print(row)
        list.insert(END, row)

def add_command():
    db.insert(et_value.get(), ea_value.get(), ey_value.get(), eid_value.get())
    # To show the user that entry is added...
    list.delete(0, END)
    list.insert(END, (et_value.get(), ea_value.get(), ey_value.get(), eid_value.get()))

def delete_command():
    # WE do not make the function call as we cannot pass the event parameter to it
    #  and hence to prevent it we make the selected_tuple variable global to use it here directly
    db.delete(selected_tuple[0])
    view_command()

def update_command():
    db.update(selected_tuple[0] ,et_value.get(), ea_value.get(), ey_value.get(), eid_value.get())
    # print(selected_tuple[0],selected_tuple[1],selected_tuple[2],selected_tuple[3],selected_tuple[4])
    # print(et_value.get(), ea_value.get(), ey_value.get(), eid_value.get())
    view_command()

def destroy_command():
    window.destroy()
    # We could have also done this directly instead...


# These are all wrapper functions as they help us when we need to pass some parameters
window = Tk()

window.geometry("510x350")
window.title("e-BookStore")
# window.iconbitmap("fav_icon.ico")
# window.iconbitmap(r'./home/amit_bahir/Downloads/icon_0W2_icon.ico')
# img = tkinter.Image("photo", file = "icon.gif")
# window.tk.call('wm', 'iconphoto', window._w, img)
# window.iconbitmap('@icon.xbm')

# Modelling the labels
Label(window, text = "Title    :   ", width= '20', font=('Arial', 16)).grid(row=0,column=0)
Label(window, text = "Author  :   ", width= '20', font=('Arial', 16)).grid(row=1,column=0)
Label(window, text = "Year     :   ", width= '20', font=('Arial', 16)).grid(row=2,column=0)
Label(window, text = "IdNo     :   ", width= '20', font=('Arial', 16)).grid(row=3,column=0)
# The above adjustments are done only for pleasing purpose


# Entry value for Title
et_value = StringVar()      # Function that creates the spatial object
et = Entry(window, textvariable = et_value , width = 20)
et.grid(row=0, column = 4)

# Entry value for Author
ea_value = StringVar()
ea = Entry(window, textvariable = ea_value , width = 20)
ea.grid(row=1, column = 4)

# Entry value for Year
ey_value = StringVar()
ey = Entry(window, textvariable = ey_value , width = 20)
ey.grid(row=2, column = 4)

# Entry value for Identification Number
eid_value = StringVar()
eid = Entry(window, textvariable = eid_value , width = 20)
eid.grid(row=3, column = 4)

# Now creating the ListBox for displaying the information about the books in our store
list = Listbox(window, height = 15, width = 40)
list.grid(row= 5, column = 0, rowspan = 6, columnspan = 4)


# Now adding a scrollbar to the ListBox
sb = Scrollbar(window)
sb.grid(row=5, column = 3, rowspan = 10)

# Configuring the ListBox and the scrollbar
list.config(yscrollcommand = sb.set)
sb.config(command = list.yview)

"""
We'll use the bind() method of the tkinter library
It is used to bind a function to an event widget.
ListboxSelect is the event type in characters
get_selected_entry() is the function that returns us the tuple carrying the info
"""
list.bind('<<ListboxSelect>>' , get_selected_entry)



# Now Creating the buttons for user
# View all records button
b_view = Button(window, text = "View all",width = 10,command = view_command)
"""
We don't put () at the end of the function name
as we want it to execute when we press the button
and NOT when python reads it...
"""
b_view.grid(row = 5, column = 4)

# Search for an entry button
b_search = Button(window, text = "Search",width = 10, command = search_command)
b_search.grid(row = 6, column = 4)

# Add an entry button
b_add = Button(window, text = "Add", width = 10,command = add_command)
b_add.grid(row = 7, column = 4)

# Update button
b_update = Button(window, text = "Update", width = 10,command = update_command)
b_update.grid(row = 8, column = 4)

# Delete button
b_delete = Button(window, text = "Delete", width = 10,command = delete_command)
b_delete.grid(row = 9, column = 4)

# Close button
b_close = Button(window, text = "Close",width = 10, command  = destroy_command)
b_close.grid(row = 10, column = 4)


window.mainloop()
