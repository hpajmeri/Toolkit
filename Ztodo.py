#importing

from tkinter import *
import tkinter.messagebox as tkm
import os
from tkinter.simpledialog import askstring

#main window

root= Tk()
root.title("To-do list maker")
root.configure(bg='white')
root.geometry('200x260')

#functions creation

def update_listbox():
    oo=1
    clear_listbox()
    for task in tasks:
        lb_tasks.insert('end','%i) %s' % (oo,task))
        oo+=1

def clear_listbox():
    lb_tasks.delete(0,'end')

def add_task():
    task= txt_input.get()
    if task!='':
        tasks.append(task)
        update_listbox()
    else:
        tkm.showwarning('Notice','You need to enter a task.')
    txt_input.delete(0, 'end')

    
def delete():
    task = lb_tasks.get('active')[3:]
    if task in tasks:
        tasks.remove(task)
    update_listbox()


def deleteall():
    j=tkm.askyesno("Confirm: Delete All","Do you really want to delete all?")
    if j==True:
        global tasks
        tasks=[]
        update_listbox()

def export():
    s=askstring('Enter Title','Enter a title for the tasks list export: ')
    f=open(s+'.txt','w+')
    f.write(s+': \n\n')
    oo=1
    for i in tasks:
        f.write(str(oo)+') '+i+'\n')
        oo+=1
    j=tkm.askyesno("Export Complete","Export complete\n Do you want to clear the current tasks?")
    if j==True:
        deleteall()
        
tasks=[]

#display elements

lbl_title = Label(root, text='To-do List', bg='White')
lbl_title.grid(row=0,column=0,columnspan=2)

txt_input = Entry(root, width=15)
txt_input.grid(row=1,column=1)

btn_add_task = Button(root, text='Add task', fg='black', bg='white', command=add_task)
btn_add_task.grid(row=1,column=0)

btn_delete = Button(root, text='Delete', fg='black', bg='white', command=delete)
btn_delete.grid(row=2,column=0)

btn_delete_all = Button(root, text='Delete all', fg='black', bg='white', command=deleteall)
btn_delete_all.grid(row=3,column=0)

btn_export = Button(root, text='Export', fg='black', bg='white', command=export)
btn_export.grid(row=4,column=0)

btn_exit = Button(root, text='Exit', fg='black', bg='white', command=exit)
btn_exit.grid(row=5,column=0)

lb_tasks = Listbox(root)
lb_tasks.grid(row=2,column=1,rowspan=4)

root.mainloop()
