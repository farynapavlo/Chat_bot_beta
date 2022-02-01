from tkinter import *

root = Tk()
root["bg"] = "blue"
root.geometry("800x500")

#Функції для кнопок
def enter_1():
    entry_label["text"] += "1"
def enter_2():
    entry_label["text"] += "2"
def enter_3():
    entry_label["text"] += "3"
def enter_4():
    entry_label["text"] += "4"
def enter_5():
    entry_label["text"] += "5"
def enter_6():
    entry_label["text"] += "6"
def enter_7():
    entry_label["text"] += "7"
def enter_8():
    entry_label["text"] += "8"
def enter_9():
    entry_label["text"] += "9"
def enter_0():
    entry_label["text"] += "0"
def enter_plus():
    entry_label["text"] += "+"
def enter_minus():
    entry_label["text"] += "-"
def enter_mult():
    entry_label["text"] += "*"
def enter_dil():
    entry_label["text"] += ":"
def clear():
    entry_label["text"] = ""
def count():
    if "+" in entry_label["text"]:
        lst = entry_label["text"].split("+")
        res = int(lst[0])+int(lst[1])
    elif "-" in entry_label["text"]:
        lst = entry_label["text"].split("-")
        res = int(lst[0])-int(lst[1])
    elif "*" in entry_label["text"]:
        lst = entry_label["text"].split("*")
        res = int(lst[0])*int(lst[1])
    elif ":" in entry_label["text"]:
        lst = entry_label["text"].split(":")
        res = int(lst[0])/int(lst[1])
    entry_label["text"] = res

#Кнопки
button_1 = Button(root, text="1", width=3, height=2, command=enter_1)
button_2 = Button(root, text="2", width=3, height=2, command=enter_2)
button_3 = Button(root, text="3", width=3, height=2, command=enter_3)
button_4 = Button(root, text="4", width=3, height=2, command=enter_4)
button_5 = Button(root, text="5", width=3, height=2, command=enter_5)
button_6 = Button(root, text="6", width=3, height=2, command=enter_6)
button_7 = Button(root, text="7", width=3, height=2, command=enter_7)
button_8 = Button(root, text="8", width=3, height=2, command=enter_8)
button_9 = Button(root, text="9", width=3, height=2, command=enter_9)
button_0 = Button(root, text="0", width=3, height=2, command=enter_0)

button_plus = Button(root, text="+", width=3, height=2, command=enter_plus)
button_minus = Button(root, text="-", width=3, height=2, command=enter_minus)
button_dil = Button(root, text=":", width=3, height=2, command=enter_dil)
button_mult = Button(root, text="*", width=3, height=2, command=enter_mult)

button_count = Button(root, text="=", width=3, height=2, command=count)
button_clear = Button(root, text="CE", width=3, height=2, command=clear)
#Стрічка введення
entry_label = Label(root, text="", width=12, font=("Araial", 20))

#Розташування елементів
entry_label.place(x=300,y=150)

button_0.place(x=300,y=200)
button_1.place(x=350,y=200)
button_2.place(x=400,y=200)
button_3.place(x=300,y=250)
button_4.place(x=350,y=250)
button_5.place(x=400,y=250)
button_6.place(x=300,y=300)
button_7.place(x=350,y=300)
button_8.place(x=400,y=300)
button_9.place(x=350,y=350)

button_minus.place(x=467,y=200)
button_plus.place(x=467,y=250)
button_dil.place(x=467,y=300)
button_mult.place(x=467,y=350)

button_count.place(x=400,y=350)
button_clear.place(x=300,y=350)

root.mainloop()

