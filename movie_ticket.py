from tkinter import *
import tkinter as tk

root=tk.Tk()

booking=tk.Label(root,text='Movie Booking id')
booking.grid(row=0)

booking_inp=tk.Entry(root)
booking_inp.grid(row=0,column=1)

person=tk.Label(root,text='Person Name')
person.grid(row=1)

person_inp=tk.Entry(root)
person_inp.grid(row=1,column=1)

movie=tk.Label(root,text='Movie Name')
movie.grid(row=2)

movie_inp=tk.Entry(root,text='Avengers')
movie_inp.grid(row=2,column=1)

gender=IntVar()
def gen():
    print(gender.get())
g=tk.Label(root,text="Class")
g.grid(row=3,column=0)

g1=Radiobutton(root,text="A",variable=gender,width=25,value=1,command=gen)
g1.grid(row=3,column=1)

g2=Radiobutton(root,text="B",variable=gender,width=25,value=2,command=gen)
g2.grid(row=3,column=2)

g=tk.Label(root,text="Time of Show")
g.grid(row=3,column=3)

g1=Checkbutton(root, text='7:15 pm')
g1.grid(row=3,column=4)

g2=Checkbutton(root, text='9 am')
g2.grid(row=3,column=5)

age=tk.Label(root,text="No. of Tickets")
age.grid(row=4,column=0)

age=Scale(root, from_=1, to= 20, orient=HORIZONTAL)
age.grid(row=4,column=1)

insert=tk.Button(root,text="Insert",width=5,command=root.destroy)
insert.grid(row=5,column=0)

update=tk.Button(root,text="Update",width=5,command=root.destroy)
update.grid(row=5,column=1)

delete=tk.Button(root,text="Delete",width=5,command=root.destroy)
delete.grid(row=6,column=0)

select=tk.Button(root,text="Select",width=5,command=root.destroy)
select.grid(row=6,column=1)








root.mainloop()

