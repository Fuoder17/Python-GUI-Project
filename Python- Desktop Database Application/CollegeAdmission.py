from tkinter import *
import BackendCA


def get_selected_row(event):
    try:
        global selected_item
        index = list_box.curselection()[0]
        selected_item = list_box.get(index)
        # This allows the value slected in the listbox to be insert into the entry box
        # and deleted as a new value are selected from the listbox
        student_frist_name.delete(0,END)
        student_frist_name.insert(END,selected_item[1])
        studnet_last_name.delete(0,END)
        studnet_last_name.insert(END,selected_item[2])
        student_email.delete(0,END)
        student_email.insert(END,selected_item[3])
        student_id.delete(0,END)
        student_id.insert(END,selected_item[4])
    except IndexError:
        pass

def view_command():
    # This ensure you don't have repeating values in the listbox so it deletes
    # from the index of zero to the end
    list_box.delete(0,END)
    # Iterate through the list to then add to listbox
    for view_values in BackendCA.view():
        list_box.insert(END,view_values)

def search_command():
    list_box.delete(0,END)
    for search_values in BackendCA.search(FN_text.get(),LN_text.get(),SE_text.get(),SID_text.get()):
        list_box.insert(END,search_values)

def add_command():
    BackendCA.insert(FN_text.get(),LN_text.get(),SE_text.get(),SID_text.get())
    # Clears the list before print the new values added
    list_box.delete(0,END)
    # Inserting the new values in a new line but thats not what we want so pass it as a tuples
    # list_box.insert(END,FN_text.get(),LN_text.get(),SE_text.get(),SID_text.get())
    list_box.insert(END,(FN_text.get(),LN_text.get(),SE_text.get(),SID_text.get()))

def delete_command():
    BackendCA.delete(selected_item[0])
    list_box.delete(0,END)
    for new_values in BackendCA.view():
        list_box.insert(END,new_values)


def update_command():
    BackendCA.update(selected_item[0],FN_text.get(),LN_text.get(),SE_text.get(),SID_text.get())


College_Admission = Tk()

College_Admission.wm_title("Admission List")

# LABELS
FN_label = Label(College_Admission, text = "First Name")
FN_label.grid(row =0, column = 0)

LN_label = Label(College_Admission, text = "Last Name")
LN_label.grid(row =0, column = 2)

email_label = Label(College_Admission, text = "Email")
email_label.grid(row =1, column = 0)

SID_label = Label(College_Admission, text = "Student ID")
SID_label.grid(row =1, column = 2)

# ENTRIES
FN_text = StringVar()
student_frist_name = Entry(College_Admission, textvariable = FN_text)
student_frist_name.grid(row = 0, column = 1)

LN_text = StringVar()
studnet_last_name = Entry(College_Admission, textvariable = LN_text)
studnet_last_name.grid(row = 0, column = 3)

SE_text = StringVar()
student_email = Entry(College_Admission, textvariable = SE_text)
student_email.grid(row = 1, column = 1)

SID_text = StringVar()
student_id = Entry(College_Admission, textvariable = SID_text )
student_id.grid(row = 1, column = 3)

list_box = Listbox(College_Admission, height = 7, width = 35)
list_box.grid(row = 2, column = 0, rowspan = 7, columnspan = 2)

# Scrolling Object
scroll_bar = Scrollbar(College_Admission)
scroll_bar.grid(row = 2, column = 2, rowspan = 6)

# Use the configure method to connect listbox to the scrollbar
list_box.configure(yscrollcommand = scroll_bar.set)
scroll_bar.configure(command = list_box.yview)

# list_box.bind('<<EVENT TYPE>>', function)
# This allows you to bind the get_selected_row functions to the listbox widget to create an event which takes two arguments. This takes the event type and function you want to bind to the event type.
list_box.bind('<<ListboxSelect>>',get_selected_row)


# Button
viewall_button = Button(College_Admission,text = "View all", width = 12, command= view_command)  #< Wrapper functions assist with passing parameter, example is the search function.
viewall_button.grid(row = 2, column = 3)

searchntry_button = Button(College_Admission,text = "Search Entry", width = 12, command = search_command)

addentry_button = Button(College_Admission,text = "Add Entry", width = 12, command = add_command)
addentry_button.grid(row = 4, column = 3)

update_button = Button(College_Admission,text = "Update Selected", width = 12, command = update_command)
update_button.grid(row = 5, column = 3)

delete_button = Button(College_Admission,text = "Delete Selected", width = 12, command = delete_command)
delete_button.grid(row = 6, column = 3)

close_button = Button(College_Admission,text = "Close", width = 12, command = College_Admission.destroy )
close_button.grid(row = 7, column = 3)


College_Admission.mainloop()
