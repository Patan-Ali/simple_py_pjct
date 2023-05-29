# Tkinter is a standard GUI library in Python
from tkinter import *  # Here we are importing all the packages of Tkinter using '*'

win = Tk()  # Here we are replacing 'tkinter' with the variable 'win'
win.title('Calculator')  # This is used for Title
win.geometry('515x365')  # Here we are describing the Resolution of our Calculator
win.resizable(0,0)   # if we use this then it will stop our Calculator to minimize or maximize

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# Function to clear a input field
def btn_clr():
    global expression
    expression = ""
    input_text.set("")

# Function to Equal button
def btn_eql():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""
input_text = StringVar()

# input field Frame
input_frame = Frame(win, width=312, height=50)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial',18,'bold'),width=38, justify=RIGHT, textvariable=input_text)
input_field.grid(row=0, column=0)

# Increase the Height of the input Field
input_field.pack(ipady=5)

# Button Frame
btns_frame = Frame(win, width=310, height=270)
btns_frame.pack()

clear = Button(btns_frame, text='C', width=38, height=3, command=lambda: btn_clr()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divie = Button(btns_frame, text='/', width=10, height=3, command=lambda: btn_click('/')).grid(row=0, column=3, padx=1, pady=1)

# Buttons for Second Row
seven = Button(btns_frame, text ='7', width=10, height=3, command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text ='8', width=10, height=3, command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text ='9', width=10, height=3, command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text ='*', width=10, height=3, command=lambda: btn_click('*')).grid(row=1, column=3, padx=1, pady=1)

# Buttons For Third Row
four = Button(btns_frame, text ='4', width=10, height=3, command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text ='5', width=10, height=3, command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text ='6', width=10, height=3, command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
subtraction = Button(btns_frame, text ='-', width=10, height=3, command=lambda: btn_click('-')).grid(row=2, column=3, padx=1, pady=1)

# Buttons for Fourth Row
one = Button(btns_frame, text ='1', width=10, height=3, command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text ='2', width=10, height=3, command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text ='3', width=10, height=3, command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
addition = Button(btns_frame, text='+', width=10, height=3, command=lambda: btn_click('+')).grid(row=3, column=3, padx=1, pady=1)

# Buttons for fifth Row
zero = Button(btns_frame, text='0', width=23, height=3, command=lambda: btn_click(0)).grid(row=4, column=0,columnspan=2, padx=1, pady=1)
dot = Button(btns_frame, text='.', width=10, height=3, command=lambda: btn_click('.')).grid(row=4, column=2, padx=1, pady=1)
equal = Button(btns_frame, text='=', width=10, height=3, command=lambda: btn_eql()).grid(row=4, column=3, padx=1, pady=1)



win.mainloop()
