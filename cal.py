from tkinter import *
import math

def click(event):
    global scvalue
    text = event.widget.cget("text")

    if text == "=":
        try:
            value = eval(scvalue.get())
            scvalue.set(value)
        except Exception:
            scvalue.set("Error")

    elif text == "C":
        scvalue.set("")

    elif text == "⌫":  
        scvalue.set(scvalue.get()[:-1])

    elif text == "x²": 
        try:
            value = float(scvalue.get()) ** 2
            scvalue.set(value)
        except Exception:
            scvalue.set("Error")

    elif text == "√x":  
        try:
            value = math.sqrt(float(scvalue.get()))
            scvalue.set(value)
        except Exception:
            scvalue.set("Error")

    elif text == "x³":  
        try:
            value = float(scvalue.get()) ** 3
            scvalue.set(value)
        except Exception:
            scvalue.set("Error")

    else:
        scvalue.set(scvalue.get() + text)

root = Tk()
root.title("Calculator")
root.geometry("400x600")
root.resizable(False, False)


root.iconbitmap("cal logo.ico")  


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 35 bold", bd=8, relief=SUNKEN, justify='right')
screen.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10, padx=10, sticky="news")


buttons = [
    ["9", "8", "7", "/"],
    ["6", "5", "4", "*"],
    ["3", "2", "1", "-"],
    ["C", "0", "⌫", "+"],
    [".", "%", "(", ")"],
    ["x²", "√x", "x³", "="]
]


for row_idx, row in enumerate(buttons, start=1):
    for col_idx, text in enumerate(row):
        button = Button(root, text=text, padx=20, pady=20, font="lucida 15 bold")
        button.grid(row=row_idx, column=col_idx, padx=5, pady=5, sticky="news")
        button.bind("<Button-1>", click)


for i in range(len(buttons) + 1):
    root.grid_rowconfigure(i, weight=1)

for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
