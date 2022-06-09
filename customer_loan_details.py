from tkinter import *
import tkinter as tk

root=tk.Tk()

anual=tk.Label(root,text='Annual Rate')
anual.grid(row=0)

anual_inp=tk.Entry(root)
anual_inp.grid(row=0,column=1)

no_inp=tk.Label(root,text='Number of payments')
no_inp.grid(row=1)

no=tk.Entry(root)
no.grid(row=1,column=1)

loan=tk.Label(root,text='Loan principle')
loan.grid(row=2)

loan_inp=tk.Entry(root)
loan_inp.grid(row=2,column=1)

monthly=tk.Label(root,text='Monthly Payment')
monthly.grid(row=3)

monthly_inp=tk.Entry(root)
monthly_inp.grid(row=3,column=1)

rem=tk.Label(root,text='Remaining Loan')
rem.grid(row=4)

rem_inp=tk.Entry(root)
rem_inp.grid(row=4,column=1)

final=tk.Button(root,text='Final Balance',command=root.destroy)
final.grid(row=5)

monthbut=tk.Button(root,text='Monthly Payment',command=root.destroy)
monthbut.grid(row=5,column=1)
quit=tk.Button(root,text='Quit',command=root.destroy)
quit.grid(row=5,column=2)
root.mainloop()
