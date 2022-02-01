import tkinter
from tkinter import *
from tkinter import messagebox

#GLOBAL VAR:
val = ""
A = 0
operator = ""

#BUTTON FUNCTIONS:
def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)

def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

# OPERATOR FUNCTIONS():

def btn_plus_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_minus_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_mul_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_div_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "÷"
    data.set(val)

def btn_c_pressed():
    global A
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    data.set(val)

# def operator_functions():
def result():
    global A
    global val
    global operator
    val2 = val
    if operator == "+":
        temp = int((val2.split("+")[1]))
        res = A + temp
        data.set(res)
        val = str(res)
    
    elif operator == "-":
        temp = int((val2.split("-")[1]))
        res = A - temp
        data.set(res)
        val = str(res)
    
    elif operator == "*":
        temp = int((val2.split("*")[1]))
        res = A * temp
        data.set(res)
        val = str(res)

    elif operator == "/":
        #print(val2.split("÷"))
        temp = int((val2.split("÷")[1]))
        if temp == 0:
            messagebox.showerror("Error", " Division by 0 Not Supported!!")
            A = ""
            val = ""
            data.set(val)
        else:
            res = int(A / temp)
            data.set(res)        
            val = str(res)

# BASIC GEOMETRY:
root = tkinter.Tk()
root.geometry("400x500+500+200")
root.resizable(0,0)
root.title("Harxssh - Calculator")

data = StringVar()
# def_LABEL():
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Verdana", 20),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000"
)
lbl.pack(expand = True, fill = "both",)

# ROW (4) :
btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand = True, fill = "both", )

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both", )

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both", )

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both", )


#ROW (1) Buttons(4):
btn7 = Button(
    btnrow1,
    text = "7",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_7_isclicked,


)
btn7.pack(side = LEFT, expand = True, fill = "both")

btn8 = Button(
    btnrow1,
    text = "8",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0, 
    command = btn_8_isclicked,
)
btn8.pack(side = LEFT, expand = True, fill = "both")

btn9 = Button(
    btnrow1,
    text = "9",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_9_isclicked,
)
btn9.pack(side = LEFT, expand = True, fill = "both")

btndiv = Button(
    btnrow1,
    text = "/",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_div_isclicked,
    
)
btndiv.pack(side = LEFT, expand = True, fill = "both")


#ROW (2) Buttons(4):
btn4 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0, 
    command = btn_4_isclicked,
)
btn4.pack(side = LEFT, expand = True, fill = "both")

btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0, 
    command = btn_5_isclicked,
)
btn5.pack(side = LEFT, expand = True, fill = "both")

btn6 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_6_isclicked,
) 
btn6.pack(side = LEFT, expand = True, fill = "both")

btnmul = Button(
    btnrow2,
    text = "*",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_mul_isclicked,
)
btnmul.pack(side = LEFT, expand = True, fill = "both")

#ROW (3) Buttons(4):
btn1 = Button(
    btnrow3,
    text = "1",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_1_isclicked,
)
btn1.pack(side = LEFT, expand = True, fill = "both")

btn2 = Button(
    btnrow3,
    text = "2",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_2_isclicked,
)
btn2.pack(side = LEFT, expand = True, fill = "both")

btn3 = Button(
    btnrow3,
    text = "3",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_3_isclicked,
)
btn3.pack(side = LEFT, expand = True, fill = "both")

btnminus = Button(
    btnrow3,
    text = "-",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_minus_isclicked,
)
btnminus.pack(side = LEFT, expand = True, fill = "both")


#ROW (4) Buttons(4):
btnC = Button(
    btnrow4,
    text = "C",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_c_pressed,
)
btnC.pack(side = LEFT, expand = True, fill = "both")

btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_0_isclicked,
)
btn0.pack(side = LEFT, expand = True, fill = "both")


btnequal = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = result,
)
btnequal.pack(side = LEFT, expand = True, fill = "both")

btnplus = Button(
    btnrow4,
    text = "+",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_plus_isclicked,
)
btnplus.pack(side = LEFT, expand = True, fill = "both")


# MAINLOOP():
root.mainloop()