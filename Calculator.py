import tkinter as tk

calcu= ""

def add_to_Calculator(data):
    global calcu
    calcu += str(data)
    result_text.delete(1.0, "end")
    result_text.insert(1.0,calcu)



def evaluate():
    global calcu
    try:
        calcu= str(eval(calcu))
        result_text.delete(1.0, "end")
        result_text.insert(1.0,calcu)
    except:
        clear_calculator()
        result_text.insert(1.0, "Error")


def clear_calculator():
    global calcu
    calcu = ""
    result_text.delete(1.0,"end") 


root = tk.Tk()
root.geometry("300x300")
result_text = tk.Text(root, height=2.5,width=14,font=("Arial", 22))
result_text.grid(columnspan=5)


btn_1 = tk.Button(root,text="1", command=lambda: add_to_Calculator(1),width=5, font=("Arial", 14 ))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root,text="2", command=lambda: add_to_Calculator(2),width=5, font=("Arial", 14 ))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root,text="3", command=lambda: add_to_Calculator(3),width=5, font=("Arial", 14 ))
btn_3.grid(row=2, column=3)

btn_sum = tk.Button(root,text="+", command=lambda: add_to_Calculator("+"),width=5, font=("Arial", 14 ))
btn_sum.grid(row=2, column=4)


btn_4 = tk.Button(root,text="4", command=lambda: add_to_Calculator(4),width=5, font=("Arial", 14 ))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root,text="5", command=lambda: add_to_Calculator(5),width=5, font=("Arial", 14 ))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root,text="6", command=lambda: add_to_Calculator(6),width=5, font=("Arial", 14 ))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root,text="7", command=lambda: add_to_Calculator(7),width=5, font=("Arial", 14 ))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root,text="8", command=lambda: add_to_Calculator(8),width=5, font=("Arial", 14 ))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root,text="9", command=lambda: add_to_Calculator(9),width=5, font=("Arial", 14 ))
btn_9.grid(row=4, column=3)

btn_0= tk.Button(root,text="0", command=lambda: add_to_Calculator(0),width=5, font=("Ariel", 14))
btn_0.grid(row=5,column=1)

btn_sum = tk.Button(root,text="+", command=lambda: add_to_Calculator("+"),width=5, font=("Arial", 14 ))
btn_sum.grid(row=2, column=4)

btn_div = tk.Button(root,text="/", command=lambda: add_to_Calculator("/"),width=5, font=("Arial", 14 ))
btn_div.grid(row=4, column=4)

btn_sum = tk.Button(root,text="×", command=lambda: add_to_Calculator("*"),width=5, font=("Arial", 14 ))
btn_sum.grid(row=5, column=2)

btn_open = tk.Button(root,text="(", command=lambda: add_to_Calculator("("),width=5, font=("Arial", 14 ))
btn_open.grid(row=5, column=3)

btn_close = tk.Button(root,text=")", command=lambda: add_to_Calculator(")"),width=5, font=("Arial", 14 ))
btn_close.grid(row=5, column=4)

btn_diff = tk.Button(root,text="-", command=lambda: add_to_Calculator("-"),width=5, font=("Arial", 14 ))
btn_diff.grid(row=3, column=4)

btn_equal = tk.Button(root,text="=", command= evaluate,width=10, font=("Arial", 14 ))
btn_equal.grid(row=6, column=2, columnspan=2)


btn_clear = tk.Button(root,text="C", command=clear_calculator,width=5, font=("Arial", 14 ))
btn_clear.grid(row=3, column=4)
root.mainloop()