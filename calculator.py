import tkinter as tk
from tkinter import messagebox

mainWindow = tk.Tk()
mainWindow.title("Calculator")

label1 = tk.Label(mainWindow,text="Enter First Number",pady=(10))
label1.pack()

name_field1 = tk.Entry(mainWindow)
name_field1.pack()

label2 = tk.Label(mainWindow,text="Enter Second Number",pady=(10))
label2.pack()

name_field2 = tk.Entry(mainWindow)
name_field2.pack()


label3 = tk.Label(mainWindow,text="Operations")
label3.pack()


def sum():
    first,second = takeValueInput()
    result = first + second
    result_label.config(text="Operation result is:" + str(result))




def subtract():
    first, second = takeValueInput()
    result = first - second
    result_label.config(text="Operation result is:" + str(result))



def multiply():
    first, second = takeValueInput()
    result = first * second
    result_label.config(text="Operation result is:" + str(result))


def divide():
    first, second = takeValueInput()

    if second == 0:
        messagebox.showerror("Error","Cannot divide the value by 0.")
    else:
        result = first/second
        result = round(result,2)
    result_label.config(text="Operation result is:" + str(result))


def takeValueInput():
    first = name_field1.get()
    second = name_field2.get()

    try:
        first = int(first)
        second = int(second)

        return first,second
    except ValueError:
        if(((len(name_field1.get()) == 0) | (len(name_field2.get())== 0))):
            messagebox.showerror("Error","Please enter a value")
        else:
            messagebox.showerror("Error","Enter only integer value")
        quit(0)

addition_button = tk.Button(mainWindow,text="+",command=lambda:sum())
addition_button.pack()

minus_button = tk.Button(mainWindow,text="-",command=lambda:subtract())
minus_button.pack()

multiply_button = tk.Button(mainWindow,text="*",command=lambda:multiply())
multiply_button.pack()

division_button = tk.Button(mainWindow,text="/",command=lambda:divide())
division_button.pack()

result_label = tk.Label(mainWindow,text="Operation Result is:")
result_label.pack()

mainWindow.mainloop()
