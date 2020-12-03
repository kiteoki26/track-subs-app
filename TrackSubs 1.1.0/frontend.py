from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from backend import backend

top=Tk()
top.geometry("800x300")

top.title("TrackSubs")


def get_selected_row(event):
    global item
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END) #clear all entry boxes

    selection=table.selection()
    item = table.item(selection)
    e1.insert(0, item["values"][1])
    e2.insert(0, item["values"][3])
    e3.insert(0, item["values"][5])
    e4.insert(0, item["values"][6])   
    
    if (item["values"][2]) == "Monthly":
        type_option.current(1)
    elif (item["values"][2])== "Daily":
        type_option.current(2) 
    else:
        type_option.current(3)
    if (item["values"][4]) == "Active":
        status_option.current(1)
    else:
        status_option.current(2)

def sort_column(table, col, reverse):
    l = [(table.set(k, col), k) for k in table.get_children('')]
    l.sort(reverse=reverse)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        table.move(k, '', index)

    # reverse sort next time
    table.heading(col, command=lambda _col=col: sort_column(table, _col, not reverse))

def view_all():
    for i in table.get_children():
        table.delete(i)
    for row in backend.view():
        table.insert("", END, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    

def insert_sub():
    if service_text.get() == "Enter service name..." or type_option.get() == "Type" or amount_text.get() == "Enter amount..." or status_option.get() == "Status" or start_date.get() == "Sub start name..." or renewal_date.get()=="Sub renewal date...":
        showinfo("Error", "Please fill in all entries.")
    elif service_text.get() == "" or type_option.get() == "Type" or status_option.get() == "Status":
        showinfo("Error", "Please fill in all relevant entries.")
    elif service_text.get() == item["values"][1]:
        showinfo("Error", "Service already exists.")
    else:
        backend.insert(service_text.get(), type_option.get(), amount_text.get(), status_option.get(), start_date.get(), renewal_date.get())
        for i in table.get_children():
            table.delete(i)
        table.insert("", END, values=(item["values"][0], service_text.get(), type_option.get(), amount_text.get(), status_option.get(), start_date.get(), renewal_date.get()))


def search_sub():
    for i in table.get_children():
        table.delete(i)
    for row in backend.search(service_text.get(), type_option.get(), amount_text.get(), status_option.get(), start_date.get(), renewal_date.get()):
        table.insert("", END, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))


def update_sub():
    if status_option.get()=="Inactive":
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        backend.update(item["values"][0], service_text.get(), type_option.get(), amount_text.get(), status_option.get(), start_date.get(), renewal_date.get())
        for i in table.get_children():
            table.delete(i)
        table.insert("", END, values=(item["values"][0], service_text.get(), type_option.get(), amount_text.get(), status_option.get(), start_date.get(), renewal_date.get()))
    
    elif status_option.get()=="Active" and type_option.get()=="Status" or amount_text.get()=="" or start_date.get()=="" or renewal_date.get()=="":
        showinfo("Error", "Please fill in all entries.")
    else:
        backend.update(item["values"][0], service_text.get(), type_option.get(), amount_text.get(), status_option.get(), start_date.get(), renewal_date.get())
        for i in table.get_children():
            table.delete(i)
        table.insert("", END, values=(item["values"][0], service_text.get(), type_option.get(), amount_text.get(), status_option.get(), start_date.get(), renewal_date.get()))


def delete_sub():
    backend.delete(item["values"][0])
    view_all()

def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    
    e1.insert(0, "Service name...")
    e2.insert(0, "Enter amount...")
    e3.insert(0, "Sub start date...")
    e4.insert(0, "Sub renewal date...")

    type_option.current(0)
    status_option.current(0)



# Create left and right frames
left_frame = Frame(top, width=650, height=400, bg='grey')
left_frame.pack(side='left', fill='both', padx=10, pady=5, expand=True)
 
right_frame = Frame(top, width=200, height=400, bg='grey')
right_frame.pack(side='right', fill='both', padx=10, pady=5, expand=True)


#Buttons
b0=Button(right_frame, text="Clear", width=10, command=clear).grid(row=4, column=6, padx=5, pady=5)
b1=Button(right_frame, text="View All", width=10, command=view_all).grid(row=6, column=5, padx=5, pady=5)
b2=Button(right_frame, text="Add New", width=10, command=insert_sub).grid(row=4, column=5, padx=5, pady=5)
b3=Button(right_frame, text="Search", width=10, command=search_sub).grid(row=6, column=6, padx=5, pady=5)
b4=Button(right_frame, text="Update", width=10, command=update_sub).grid(row=7, column=5, padx=5, pady=5)
b5=Button(right_frame, text="Delete", width=10, command=delete_sub).grid(row=7, column=6, padx=5, pady=5)
b6=Button(right_frame, text="Close", width=10, command=top.destroy).grid(row=8, column=6, padx=5, pady=5)

#Labels
l1=Label(right_frame)
l1.grid(row=5, column=5, padx=5, pady=5)
l1.config(bg="grey")


def e1_click(event):
    """function that gets called whenever entry is clicked"""
    if e1.get() == 'Service name...':
       e1.delete(0, "end") # delete all the text in the entry
       e1.insert(0, '') #Insert blank for user input
       e1.config(fg = 'black')
def e1_focusout(event):
    if e1.get() == '':
        e1.insert(0, 'Service name...')


def e2_click(event):
    """function that gets called whenever entry is clicked"""
    if e2.get() == 'Amount...':
       e2.delete(0, "end") # delete all the text in the entry
       e2.insert(0, '') #Insert blank for user input
       e2.config(fg = 'black')
def e2_focusout(event):
    if e2.get() == '':
        e2.insert(0, 'Amount...')


def e3_click(event):
    """function that gets called whenever entry is clicked"""
    if e3.get() == 'Sub start date...':
       e3.delete(0, "end") # delete all the text in the entry
       e3.insert(0, '') #Insert blank for user input
       e3.config(fg = 'black')
def e3_focusout(event):
    if e3.get() == '':
        e3.insert(0, 'Sub start date...')


def e4_click(event):
    """function that gets called whenever entry is clicked"""
    if e4.get() == 'Sub renewal date...':
       e4.delete(0, "end") # delete all the text in the entry
       e4.insert(0, '') #Insert blank for user input
       e4.config(fg = 'black')
def e4_focusout(event):
    if e4.get() == '':
        e4.insert(0, 'Sub renewal date...')


#Entry boxes
service_text=StringVar()
e1=Entry(right_frame, textvariable=service_text, width=17)
e1.grid(row=1, column=5, padx=5, pady=5)
e1.insert(0, 'Service name...')
e1.bind('<FocusIn>', e1_click)
e1.bind('<FocusOut>', e1_focusout)


amount_text=StringVar()
e2=Entry(right_frame, textvariable=amount_text, width=17)
e2.grid(row=1, column=6, padx=5, pady=5)
e2.insert(0, 'Amount...')
e2.bind('<FocusIn>', e2_click)
e2.bind('<FocusOut>', e2_focusout)

start_date=StringVar()
e3=Entry(right_frame, textvariable=start_date, width=17)
e3.grid(row=3, column=5, padx=5, pady=5)
e3.insert(0, 'Sub start date...')
e3.bind('<FocusIn>', e3_click)
e3.bind('<FocusOut>', e3_focusout)

renewal_date=StringVar()
e4=Entry(right_frame, textvariable=renewal_date, width=17)
e4.grid(row=3, column=6, padx=5, pady=5)
e4.insert(0, 'Sub renewal date...')
e4.bind('<FocusIn>', e4_click)
e4.bind('<FocusOut>', e4_focusout)


#Dropdown Boxes
type_option=ttk.Combobox(right_frame, values=["Type", "Monthly", "Daily", "Yearly"], width=14)
type_option.grid(row=2, column=5, padx=5, pady=5)
type_option.current(0) #default value

status_option=ttk.Combobox(right_frame, values=["Status", "Active", "Inactive"], width=14)
status_option.grid(row=2, column=6, padx=5, pady=5)
status_option.current(0) #default value

#Table
cols="ID","Service","Type","Amount","Status","Start Date","Renewal"
table=ttk.Treeview(left_frame, columns=cols, show="headings")
table.column("ID", minwidth=0, width=35, stretch=False)
table.heading("ID", text="ID")
for col in cols[1:]:
    table.column(col, minwidth=0, width=80, stretch=False)
    table.heading(col, text=col)
table.pack(side='left', fill='both', padx=5, pady=5, expand=True)

table.bind("<<TreeviewSelect>>", get_selected_row)


for col in cols:
    table.heading(col, text=col,command=lambda _col=col: sort_column(table, _col, False))



#Scrollbar
sb1=Scrollbar(top)
sb1.pack(side="right")
table.configure(yscrollcommand=sb1.set)
sb1.configure(command=table.yview)


top.mainloop()