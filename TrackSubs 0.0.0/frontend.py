from tkinter import * 
from tkinter import ttk
from backend import backend

top=Tk()

top.title("TrackSubs")


def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[3])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[5])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[6])
        if selected_tuple[2] == "Monthly":
            type_option.current(0)
        elif selected_tuple[2] == "Yearly":
            type_option.current(2)
        else:
            type_option.current(1)
        if selected_tuple[4] == "Active":
            status_option.current(0)
        else:
            status_option.current(1)
    except IndexError:
        pass




def view_all():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)
    

def insert_sub():
    backend.insert(service_text.get(), type_option.get(), amount_text.get(), status_option.get(), start_date.get(), renewal_date.get())
    list1.delete(0,END)
    list1.insert(END, (service_text.get(), type_option.get(), amount_text.get(), status_option.get(), start_date.get(), renewal_date.get()))


def search_sub():
    list1.delete(0,END)
    for row in backend.search(service_text.get(), type_option.get(), amount_text.get(), status_option.get(), start_date.get(), renewal_date.get()):
        list1.insert(END, row)


def update_sub():
    backend.update(selected_tuple[0], service_text.get(), type_option.get(), amount_text.get(), status_option.get(), start_date.get(), renewal_date.get())
    list1.delete(0,END)
    list1.insert(END, (selected_tuple[0], service_text.get(), type_option.get(), amount_text.get(), status_option.get(), start_date.get(), renewal_date.get()))

def delete_sub():
    backend.delete(selected_tuple[0])
    view_all()


#Buttons
b1=Button(top, text="View All", width=10, command=view_all).grid(row=4, column=5)
b2=Button(top, text="Add New", width=10, command=insert_sub).grid(row=5, column=5)
b3=Button(top, text="Search", width=10, command=search_sub).grid(row=6, column=5)
b4=Button(top, text="Update", width=10, command=update_sub).grid(row=7, column=5)
b5=Button(top, text="Delete", width=10, command=delete_sub).grid(row=8, column=5)
b6=Button(top, text="Close", width=10, command=top.destroy).grid(row=9, column=5)


#Labels
l1=Label(top, text="Service", width=10).grid(row=0,column=0)
l2=Label(top, text="Type").grid(row=1,column=0)
l3=Label(top, text="Amount", width=10).grid(row=0,column=2)
l4=Label(top, text="Status").grid(row=1,column=2)
l5=Label(top, text="Start Date", width=10).grid(row=0,column=4)
l6=Label(top, text="Renewal Date").grid(row=1,column=4)

l7=Label(top, text="").grid(row=2,column=0)

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




#Listbox
list1=Listbox(top, width=70)
list1.grid(row=4, column=0, rowspan=7, columnspan=4)
list1.bind("<<ListboxSelect>>", get_selected_row)

#Scrollbar configurations
sb1=Scrollbar(top)
sb1.grid(row=5, column=4, rowspan=4)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

top.mainloop()