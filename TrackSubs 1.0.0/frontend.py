from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from backend import backend

top=Tk()
top.geometry("720x300")

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
    if service_text.get() == "" or type_option.get() == "" or amount_text.get() == "" or status_option.get() == "":
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


def delete_sub():
    backend.delete(item["values"][0])
    view_all()

def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    type_option.current(0)
    status_option.current(0)

#Buttons
b0=Button(top, text="Clear", width=10, command=clear).grid(row=1, column=7)
b1=Button(top, text="View All", width=10, command=view_all).grid(row=4, column=7)
b2=Button(top, text="Add New", width=10, command=insert_sub).grid(row=5, column=7)
b3=Button(top, text="Search", width=10, command=search_sub).grid(row=6, column=7)
b4=Button(top, text="Update", width=10, command=update_sub).grid(row=7, column=7)
b5=Button(top, text="Delete", width=10, command=delete_sub).grid(row=8, column=7)
b6=Button(top, text="Close", width=10, command=top.destroy).grid(row=9, column=7)


#Labels
l1=Label(top, text="Service", width=10).grid(row=0,column=0)
l2=Label(top, text="Type").grid(row=1,column=0)
l3=Label(top, text="Amount", width=10).grid(row=0,column=2)
l4=Label(top, text="Status").grid(row=1,column=2)
l5=Label(top, text="Start Date", width=10).grid(row=0,column=4)
l6=Label(top, text="Renewal Date").grid(row=1,column=4)

l7=Label(top, text="").grid(row=2,column=0)
l8=Label(top, text="", width=1).grid(row=2,column=6)

#Entry boxes
service_text=StringVar()
e1=Entry(top, textvariable=service_text, width=17)
e1.grid(row=0, column=1)

amount_text=StringVar()
e2=Entry(top, textvariable=amount_text, width=17)
e2.grid(row=0, column=3)

start_date=StringVar()
e3=Entry(top, textvariable=start_date, width=17)
e3.grid(row=0, column=5)

renewal_date=StringVar()
e4=Entry(top, textvariable=renewal_date, width=17)
e4.grid(row=1, column=5)


#Dropdown Boxes
type_option=ttk.Combobox(top, values=["", "Monthly", "Daily", "Yearly"], width=14)
type_option.grid(row=1,column=1)
type_option.current(0) #default value

status_option=ttk.Combobox(top, values=["", "Active", "Inactive"], width=14)
status_option.grid(row=1,column=3)
status_option.current(0) #default value

#Table
cols="ID","Service","Type","Amount","Status","Start Date","Renewal"
table=ttk.Treeview(top, columns=cols, show="headings")
table.column("ID", minwidth=0, width=35, stretch=False)
table.heading("ID", text="ID")
for col in cols[1:]:
    table.column(col, minwidth=0, width=80, stretch=False)
    table.heading(col, text=col)
table.grid(row=4, column=0, rowspan=7,columnspan=5)

table.bind("<<TreeviewSelect>>", get_selected_row)


for col in cols:
    table.heading(col, text=col,command=lambda _col=col: sort_column(table, _col, False))



#Scrollbar
sb1=Scrollbar(top)
sb1.grid(row=5,column=5, rowspan=5)
table.configure(yscrollcommand=sb1.set)
sb1.configure(command=table.yview)


top.mainloop()