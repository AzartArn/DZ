from tkinter import *


A2 = -0.125
B2 = 2


def lists(bit1, bit2):
    Alist = []
    b1 = list(bit1)
    b2 = list(bit2)
    b1.reverse()
    b2.reverse()
    for i in range(16):
        Alist.append(0)
    for i in range(len(b1)):
        Alist[i] = b1[i]
    for i in range(len(b2)):
        Alist[i+5] = b2[i]
    Alist.reverse()
    return Alist


def destobin(x):
    if x == 0:
        return '0'
    res = ''
    while x > 0:
        res = ('0' if x % 2 == 0 else '1') + res
        x //= 2
    return res


def select(color, sel1, sel2, sel3):
    lbl.config(text=sel1, bg=color)
    lbl3.config(text=sel2, bg="CadetBlue3")
    lbl4.config(text=sel3, bg="CadetBlue3")


def kodek():
    d = v.get()
    bit1 = destobin(int(var.get())+22)
    bit2 = destobin(int(var.get())+44)
    if d < 4.2 or d > 7.8:
        sel1 = "Аварийное состояние"
        sel2 = bit1
        sel3 = "00000"
        bit2 = "00000"
        colors = "red3"
    elif d > 5.3 and d < 6.7:
        sel1 = "В пределах нормы"
        sel2 = bit1
        sel3 = "00000"
        bit2 = "00000"
        colors = "green4"
    elif d > 4.1 and d < 5.4:
        sel1 = "Напряжение увеличено \nИсполяющие устройство Блок питания №"\
            + str(var.get()) + "\nПоказатель ЦАП +" + str(d/10.0*A2+B2)
        sel2 = str(bit1)
        sel3 = str(bit2)
        colors = "CadetBlue3"
    elif d > 6.6 and d < 7.9:
        sel1 = "Напряжение увеличено \nИсполяющие устройство Блок питания №"\
            + str(var.get()) + "\nПоказатель ЦАП -" + str(d/12.0*A2+B2)
        sel2 = str(bit1)
        sel3 = str(bit2)
        colors = "CadetBlue3"
    Alist = lists(bit1, bit2)
    print(Alist)
    lbl5.config(text='')
    lbl5.config(text=Alist, bg="CadetBlue3")
    select(color=colors, sel1=sel1, sel2=sel3, sel3=sel2)


top = Tk()
top.title("Плотность тока")
top.resizable(False, False)
top.config(bg="black")

lbl0 = Label(top, bg="cadet blue", text="Номер дачика", width=51)
lbl0.grid(row=0, column=0, columnspan=2, pady=5, padx=5)

var = IntVar()
var.set(1)
spin = Spinbox(top, from_=1, to=4, width=57, textvariable=var)

spin.grid(row=1, column=0, columnspan=2, pady=5, padx=5)

v = DoubleVar()
scale = Scale(top, variable=v, from_=1, to=12, orient=HORIZONTAL,
              tickinterval=1, resolution=0.1, length=350
              )
scale.grid(row=2, column=0, columnspan=2, pady=5, padx=5)

btn = Button(top, text="Рассчитать", width=50, command=kodek)
btn.grid(row=3, column=0, columnspan=2, pady=5, padx=5)

lbl1 = Label(top, bg="CadetBlue3", text="Код устройства", width=20, height=1)
lbl1.grid(row=4, column=0, pady=5, padx=5)

lbl2 = Label(top, bg="CadetBlue3", text="Код дачика", width=20, height=1)
lbl2.grid(row=4, column=1, pady=5, padx=5)

lbl3 = Label(top, bg="black", width=20, height=1)
lbl3.grid(row=5, column=0, pady=5, padx=5)

lbl4 = Label(top, bg="black", width=20, height=1)
lbl4.grid(row=5, column=1, pady=5, padx=5)

lbl5 = Label(top, bg="black", width=51, height=4)
lbl5.grid(row=6, column=0, columnspan=2, pady=5, padx=5)

lbl = Label(top, bg="black", width=51, height=4)
lbl.grid(row=7, column=0, columnspan=2, pady=5, padx=5)

top.mainloop()
