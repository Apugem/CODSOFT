import tkinter as tkinter
import random

root = tkinter.Tk()

root.geometry()

task = []
#task = ["hey","hello"]
def update_task():
    clear_list()
    for tasks in task:
        lbl_task.insert("end",tasks)

def clear_list():
    lbl_task.delete(0,"end")

def add_task():
    tasks  = txt.get()
    if tasks !="":
        task.append(tasks)
        update_task() 
    else:
        display["text"]= "Enter your task"
    txt.delete(0,"end")

def clear_task():
    global task
    task = []
    update_task()
    
def del_task():
    tasks = lbl_task.get("active")
    if tasks in task:
        task.remove(tasks)
    update_task()


     

lbl_title = tkinter.Label(root,text="to-Do-List")
lbl_title.pack()


txt = tkinter.Entry(root, width = 15)
txt.pack()

btn_add_task= tkinter.Button(root, text="Add task",command= add_task)
btn_add_task.pack()

btn_delete= tkinter.Button(root, text="Delete task",command= del_task)
btn_delete.pack()

btn_clear= tkinter.Button(root, text="Clear task",command= clear_task)
btn_clear.pack()

btn_exit= tkinter.Button(root, text="EXIT",command=exit)
btn_exit.pack()

display= tkinter.Label(root,text="")
display.pack()

lbl_task= tkinter.Listbox(root)
lbl_task.pack()

root.mainloop()


