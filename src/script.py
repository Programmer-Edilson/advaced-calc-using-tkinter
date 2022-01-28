from tkinter import *
from math import sqrt

def percent():
    first_number = entry.get()
    f_num.set(float(first_number))
    delete_entry()
    label_value.set(str(first_number) + " % of ")
    signal.set(1)

def type_number(number):
    first_number = entry.get()

    if ("." in first_number) and (number == "."):
        pass
    else:
        entry.delete(0, END)
        current_number = str(first_number) + str(number)
        entry.insert(END, current_number)
    operation.set("DIG")

def calc_perc():
    l_n = float(entry.get())
    f_n = f_num.get()

    result = ((l_n * f_n) / 100)
    delete_entry()
    entry.insert(0, result)
    last_label_value = label_value.get()
    label_value.set(last_label_value + str(l_n))

def iqual():
    if signal.get() == 1:
        calc_perc()
        signal.set(0)
    else:
        brute_terms = entry.get()

        try:
            terms = brute_terms.replace("x", "*")
            terms = brute_terms.replace("÷", "/")
        except:
            print("Replace Exception")
            pass
        
        try:
            result = str(eval(terms))
            entry.delete(0, END)
            entry.insert(0, result)
            label_value.set(brute_terms)
            operation.set("IQU")
        except:
            label_value.set(brute_terms + " ERROR")
            operation.set("ERR")
            pass
    
def sqroot():
    term = float(entry.get())
    result = sqrt(term)
    delete_entry()
    entry.insert(0, result)
    label_value.set("√ of "+str(term))

def delete_entry():
    entry.delete(0, END)
    operation.set("DEL")

def clean():
    entry.delete(0, END)
    label_value.set("")
    operation.set("CLE")

root = Tk()
root.title("Calculadora")
root['bg'] = "cyan"

f_num = DoubleVar()
l_num = DoubleVar()
operation = StringVar()
label_value = StringVar()

signal = IntVar()
signal.set(0)
# declaring widgets

label = Label(root, textvariable = label_value, bg = "cyan", font = ("anonymous", 10))
entry = Entry(root, font = ('Arial', 16), bg = "cyan")

sqrbtn = Button(root, text= "√",relief = FLAT, bg = "lightgreen", command = sqroot)
blopenbtn = Button(root, text= "(",relief = FLAT, bg = "light coral", command = lambda: type_number("("))
blclosebtn = Button(root, text= ")",relief = FLAT, bg = "light coral", command = lambda: type_number(")"))
percetbtn = Button(root, text= "%",relief = FLAT, bg = "lightgray", command = percent)

delbtn = Button(root, text= "DEL", relief = FLAT, bg = "lightpink", command = delete_entry)
clrbtn = Button(root, text= "CLR", relief = FLAT, bg = "tomato", command = clean)

btn0 = Button(root, text= "0", relief = FLAT, bg = "lightblue", command = lambda: type_number(0))
btn1 = Button(root, text= "1", relief = FLAT, bg = "lightblue", command = lambda: type_number(1))
btn2 = Button(root, text= "2", relief = FLAT, bg = "lightblue", command = lambda: type_number(2))
btn3 = Button(root, text= "3", relief = FLAT, bg = "lightblue", command = lambda: type_number(3))
btn4 = Button(root, text= "4", relief = FLAT, bg = "lightblue", command = lambda: type_number(4))
btn5 = Button(root, text= "5", relief = FLAT, bg = "lightblue", command = lambda: type_number(5))
btn6 = Button(root, text= "6", relief = FLAT, bg = "lightblue", command = lambda: type_number(6))
btn7 = Button(root, text= "7", relief = FLAT, bg = "lightblue", command = lambda: type_number(7))
btn8 = Button(root, text= "8", relief = FLAT, bg = "lightblue", command = lambda: type_number(8))
btn9 = Button(root, text= "9", relief = FLAT, bg = "lightblue", command = lambda: type_number(9))
spotbtn = Button(root, text= ".", relief = FLAT, bg = "lightblue", command = lambda: type_number("."))

devbtn = Button(root, text= "÷", relief = FLAT, bg = "lightgray", command = lambda: type_number("÷"))
multbtn = Button(root, text= "x", relief = FLAT, bg = "lightgray", command = lambda: type_number("x"))
addbtn = Button(root, text= "+", relief = FLAT, bg = "lightgray", command = lambda: type_number("+"))
subbtn = Button(root, text= "-", relief = FLAT, bg = "lightgray", command = lambda: type_number("-"))
iqualbtn = Button(root, text= "=", relief = FLAT, bg = "lightgreen", command = iqual)

# give position for widgets

label.grid(row = 0, column = 0,columnspan = 4, sticky = W)
entry.grid(row = 1, column = 0, columnspan = 4, sticky = W+E, ipady = 30)

btn7.grid(row = 3, column = 0, sticky = W+E, ipadx = 20, ipady = 30)
btn8.grid(row = 3, column = 1, sticky = W+E, ipadx = 20, ipady = 30)
btn9.grid(row =3, column = 2, sticky = W+E, ipadx = 20, ipady = 30)
clrbtn.grid(row =3, column = 3, sticky = W+E+N, ipadx = 20, ipady = 8)
delbtn.grid(row =3, column = 3, sticky = W+E+S, ipadx = 20, ipady = 8)
devbtn.grid(row =4, column = 3, sticky = W+E+N, ipadx = 20, ipady = 8)

btn4.grid(row = 4, column = 0, sticky = W+E, ipadx = 20, ipady = 30)
btn5.grid(row = 4, column = 1, sticky = W+E, ipadx = 20, ipady = 30)
btn6.grid(row =4, column = 2, sticky = W+E, ipadx = 20, ipady = 30)
multbtn.grid(row =4, column = 3, sticky = W+E+S, ipadx = 20, ipady = 8)
subbtn.grid(row =5, column = 3, sticky = W+E+N, ipadx = 20, ipady = 8)

btn1.grid(row = 5, column = 0, sticky = W+E, ipadx = 20, ipady = 30)
btn2.grid(row = 5, column = 1, sticky = W+E, ipadx = 20, ipady = 30)
btn3.grid(row = 5, column = 2, sticky = W+E, ipadx = 20, ipady = 30)
addbtn.grid(row =5, column = 3, sticky = W+E+S, ipadx = 20, ipady = 8)

btn0.grid(row = 6, column = 1, sticky = W+E, ipadx = 20, ipady = 15)
spotbtn.grid(row = 6, column = 0, sticky = W+E, ipadx = 20, ipady = 15)
iqualbtn.grid(row =6, columnspan = 2, column = 2, sticky = W+E, ipadx = 20, ipady = 15)

sqrbtn.grid(row =2, column = 2, sticky = W+E, ipadx = 20, ipady = 8)
blopenbtn.grid(row =2, column = 0, sticky = W+E, ipadx = 20, ipady = 8)
blclosebtn.grid(row =2, column = 1, sticky = W+E, ipadx = 20, ipady = 8)
percetbtn.grid(row =2, column = 3, sticky = W+E, ipadx = 20, ipady = 8)

root.mainloop()
