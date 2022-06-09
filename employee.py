import tkinter as tk
from tkinter import *

root=tk.Tk()

empid=Label(root,text='Empid')
empid.grid(row=0)

empid_inp=Entry(root)
empid_inp.grid(row=0,column=1)

emp_name=tk.Label(root,text='Employee Name')
emp_name.grid(row=1)

emp_name_inp=Entry(root)
emp_name_inp.grid(row=1,column=1)

job=Label(root, text='Job')
job.grid(row=2)

job_inp=Entry(root,text='Manager')
job_inp.grid(row=2,column=1)

emp_type=IntVar()
def gen():
    print(emp_type.get())

emp_label=Label(root,text='Employee Type')
emp_label.grid(row=3)

emp_butt1=Radiobutton(root,text='Regular',value=1,variable=emp_type,command=gen)
emp_butt1.grid(row=3,column=1)

emp_butt2=Radiobutton(root,text='Temporary',value=2,variable=emp_type,command=gen)
emp_butt2.grid(row=3,column=2)


insert=Button(root,text='Insert',command=root.destroy)
insert.grid(row=4)

update=Button(root,text='Update',command=root.destroy)
update.grid(row=4,column=1)

delete=Button(root,text='Delete',command=root.destroy)
delete.grid(row=5)

select=Button(root,text='Select',command=root.destroy)
select.grid(row=5,column=1)
me=tk.Label(root,text='Name: S Vignesh Nelakantan\nReg.no:RA2011003010530',fg='red')
me.grid(row=7)



root.mainloop()
