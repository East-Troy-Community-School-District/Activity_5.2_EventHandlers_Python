'''
GUI Calculator
Pawelski
5/16/2023
Python II
'''

import tkinter as tk
import tkinter.messagebox as msgbox

# -- Event Handlers --
def add():
    '''
    Adds the two numbers entered by the user.
    '''
    number1 = float(number1_entry.get())
    number2 = float(number2_entry.get())
    result = number1 + number2
    output = str(number1) + " + " + str(number2) + " = " + str(result)
    result_label.config(text=output)

def subtract():
    '''
    Subtracts the two numbers entered by the user.
    '''
    number1 = float(number1_entry.get())
    number2 = float(number2_entry.get())
    result = number1 - number2
    output = str(number1) + " - " + str(number2) + " = " + str(result)
    result_label.config(text=output)
    
def multiply():
    '''
    Multiplies the two numbers entered by the user.
    '''
    number1 = float(number1_entry.get())
    number2 = float(number2_entry.get())
    result = number1 * number2
    output = str(number1) + " * " + str(number2) + " = " + str(result)
    result_label.config(text=output)
    
def divide(event):
    '''
    Divides the two numbers entered by the user.
    '''
    number1 = float(number1_entry.get())
    number2 = float(number2_entry.get())
    if number2 != 0:
        result = number1 / number2
    else:
        result = "nan"
    output = str(number1) + " / " + str(number2) + " = " + str(result)
    result_label.config(text=output)

def reminder(event):
    '''
    Displays a reminder pop-up to enter only numbers.
    '''
    msgbox.showinfo("Number Warning", "Please enter only numbers!")

# -- GUI Setup --
window = tk.Tk()
window.title("Calculator")

number1_frame = tk.Frame(window)
number1_label = tk.Label(number1_frame, text="First number:")
number1_entry = tk.Entry(number1_frame)
number1_entry.bind("<Button-1>", reminder)
number1_label.pack(side=tk.LEFT, padx=2, pady=2)
number1_entry.pack(side=tk.LEFT, padx=2, pady=2)
number1_frame.pack()

number2_frame = tk.Frame(window)
number2_label = tk.Label(number2_frame, text="Second number:")
number2_entry = tk.Entry(number2_frame)
number2_entry.bind("<Button-1>", reminder)
number2_label.pack(side=tk.LEFT, padx=2, pady=2)
number2_entry.pack(side=tk.LEFT, padx=2, pady=2)
number2_frame.pack()

operations_frame = tk.Frame(window)
add_button = tk.Button(operations_frame, text="+", command=add)
subtract_button = tk.Button(operations_frame, text="-", command=subtract)
multiply_button = tk.Button(operations_frame, text="*", command=multiply)
divide_button = tk.Button(operations_frame, text="/", command=divide)
add_button.pack(side=tk.LEFT, padx=2, pady=2)
subtract_button.pack(side=tk.LEFT, padx=2, pady=2)
multiply_button.pack(side=tk.LEFT, padx=2, pady=2)
divide_button.pack(side=tk.LEFT, padx=2, pady=2)
operations_frame.pack()

result_label = tk.Label(window)
result_label.pack()

window.mainloop()