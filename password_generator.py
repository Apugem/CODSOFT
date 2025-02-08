from tkinter import *
from random import randint

root = Tk()

root.title('Password_Generator')

password = chr(randint(33, 100))

def new_rand():
    pw_entry.delete(0,END)
    
    pw_length = int(my_entry.get())
    password = ' '
    
    for i in range(pw_length):
        password+= chr(randint(33,100))
        
    pw_entry.insert(0,password)


user_input = LabelFrame(root, text= "Length of the Password")
user_input.pack(pady= 15)

my_entry = Entry(user_input, font=("Helvetica", 22))
my_entry.pack(pady=15, padx=15)


pw_entry = Entry(root,text = '', font=("Helvetica", 22), bd=0, bg="systembuttonface")
pw_entry.pack(pady=15)

my_frame = Frame(root)
my_frame.pack(pady=15)

my_btn = Button(my_frame, text = "Generate", command = new_rand)
my_btn.grid(row= 0, column=0, padx = 10)

# my_clip = Button(my_frame, text = "Copy to Clipboard", command = clip)
# my_clip.grid(row= 0, column=2, padx = 10)

my_exit = Button(my_frame, text = "Exit", command = exit)
my_exit.grid(row= 0, column=3, padx = 10)

root.mainloop()