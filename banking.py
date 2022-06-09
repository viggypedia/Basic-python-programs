import tkinter as tk
from tkinter import *

#Creating the main root window


root=tk.Tk()

my_identity=tk.Label(root, text='Name: S Vignesh Nelakantan\nReg.no=530')

custid=tk.Label(root,text='Custid')
custid.grid(row=0)

custid_inp=tk.Entry(root)
custid_inp.grid(row=0,column=1)

custname=tk.Label(root,text='Customer Name')
custname.grid(row=1)

custname_inp=tk.Entry(root)
custname_inp.grid(row=1,column=1)

branch=tk.Label(root,text='Branch')
branch.grid(row=2)

branch_inp=tk.Entry(root,text='adyar')
branch_inp.grid(row=2,column=1)

acc_type=tk.IntVar()
def gen():
    print(acc_type.get())

acc_type_var=tk.Label(root,text='Account type')
acc_type_var.grid(row=3)

acc_type_button1=tk.Radiobutton(root,text='A',value=1,variable=acc_type,command=gen)
acc_type_button1.grid(row=3,column=1)

acc_type_button2=tk.Radiobutton(root,text='B',value=2,variable=acc_type,command=gen)
acc_type_button2.grid(row=3,column=2)

amt=tk.Label(root,text='Amount')
amt.grid(row=4)

amt_scale=tk.Scale(root,from_=15 ,to=100, orient=HORIZONTAL)
amt_scale.grid(row=4,column=1)

insert=tk.Button(root,text='Insert',command=root.destroy)
insert.grid(row=5,column=0)

update=tk.Button(root,text='Update',command=root.destroy)
update.grid(row=5, column=1)

delete=tk.Button(root,text='Delete',command=root.destroy)
delete.grid(row=6,column=0)

select=tk.Button(root,text='Select',command=root.destroy)
select.grid(row=6,column=1)

me=tk.Label(root,text='Name: S Vignesh Nelakantan\nReg.no:RA2011003010530',fg='red')
me.grid(row=7)




root.mainloop()
