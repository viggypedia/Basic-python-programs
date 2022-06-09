import tkinter as tk
import sqlite3

#By: S Vignesh Nelakantan
# Reg.no: RA2011003010530

connection=sqlite3.connect('student.db')
cursor=connection.cursor()
#cursor.execute("""create table details (reg_no integer,name text,department test);""")



root=tk.Tk()
#root.geometry('500x500')
regno=tk.Label(root,text='Regno')
regno.grid(row=0)

reg_inp=tk.Entry(root)
reg_inp.grid(row=0,column=1)


name=tk.Label(root,text='Name')
name.grid(row=1)

name_inp=tk.Entry(root)
name_inp.grid(row=1,column=1)

dept=tk.Label(root,text='Dept')
dept.grid(row=2)

dept_inp=tk.Entry(root)
dept_inp.grid(row=2,column=1)

gender=tk.IntVar()
def gen():
    print(gender.get())

g=tk.Label(root,text="Gender")
g.grid(row=3,column=0)
g1=tk.Radiobutton(root,text="Male",variable=gender,width=25,value=1,command=gen)
g1.grid(row=3,column=1)
g2=tk.Radiobutton(root,text="Female",variable=gender,width=25,value=2,command=gen)
g2.grid(row=3,column=2)
age=tk.Label(root,text="Age")
age.grid(row=4,column=0)
age=tk.Spinbox(root,from_=0, to = 30)
age.grid(row=4,column=1)

reg=reg_inp.get()
nam=name_inp.get()
dep=dept_inp.get()

def insert_func(reg,nam,dep):
    det=[
            (530,"S Vignesh Nelakantan",'CSE'),
            (494,"Shibashish Chanda",'CSE'),
            (1086,"Priyanshu Sharma",'CSE'),
     ]
    cursor.executemany('insert into details values (?,?,?)',det)

insert=tk.Button(root,text="Insert",width=5,command=insert_func(reg,nam,dep))
insert.grid(row=5,column=0)

update=tk.Button(root,text="Update",width=5,command=root.destroy)
update.grid(row=5,column=1)

delete=tk.Button(root,text="Delete",width=5,command=root.destroy)
delete.grid(row=6,column=0)

select=tk.Button(root,text="Select",width=5,command=root.destroy)
select.grid(row=6,column=1)

cursor.execute('select *from details')
d=cursor.fetchall
print((d))

root.mainloop()
connection.commit()
connection.close()
