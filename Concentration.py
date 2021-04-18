from tkinter import *


def destobin(x):
    if x == 0:
        return '0'
    res = ''
    while x > 0:
        res = ('0' if x % 2 == 0 else '1') + res
        x //= 2
    return res


def select(sel, color):
    lbl.config(text=sel, bg=color)


def kodek():
    d = v.get()
    bit1 = destobin(int(var.get())+14)
    bit2 = destobin((int(var.get())+14)*2)
    if d < 4.2 or d > 7.8:
        sels = "Аварийное состояние \nКод дачика = " + str(bit1)
        colors = "red3"
    elif d > 5.3 and d < 6.7:
        sels = "В пределах нормы \nКод дачика = " + str(bit1)
        colors = "green4"
    elif d > 4.1 and d < 5.4:
        sels = "Начата подача раствора \nКод дачика = " + str(bit1) + \
            "\nИсполяющие устройство подачик концентрата №" + \
            str(var.get()) + "\nКод устройства = " \
            + destobin((int(var.get())+14)*2-1)
        colors = "CadetBlue3"
    elif d > 6.6 and d < 7.9:
        sels = "Напряжение уменьшено \nКод дачика = " + str(bit1) + \
            "\nИсполяющие устройство Блок питания №" + str(var.get()) \
            + "\nКод устройства = " + str(bit2)
        colors = "CadetBlue3"
    select(sel=sels, color=colors)


top = Tk()
top.title("Концентрация")
top.resizable(False, False)
top.config(bg="black")

lbl1 = Label(top, bg="cadet blue", text="Номер дачика", width=51)
lbl1.grid(row=0, column=0, pady=5, padx=5)

var = IntVar()
var.set(1)
spin = Spinbox(top, from_=1, to=8, width=57, textvariable=var)

spin.grid(row=1, column=0, pady=5, padx=5)

v = DoubleVar()
scale = Scale(top, variable=v, from_=1, to=12, orient=HORIZONTAL,
              tickinterval=1, resolution=0.1, length=350
              )
scale.grid(row=2, column=0, pady=5, padx=5)

btn = Button(top, text="Рассчитать", width=50, command=kodek)
btn.grid(row=3, column=0, pady=5, padx=5)

lbl = Label(top, bg="cadet blue", width=51, height=4)
lbl.grid(row=4, column=0, rowspan=2, pady=5, padx=5)

top.mainloop()
