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

    lbl015.config(text=Alist[0], bg="yellow")
    lbl014.config(text=Alist[1], bg="yellow")
    lbl013.config(text=Alist[2], bg="yellow")
    lbl012.config(text=Alist[3], bg="yellow")
    lbl011.config(text=Alist[4], bg="yellow")

    lbl010.config(text=Alist[5], bg="green")
    lbl09.config(text=Alist[6], bg="green")
    lbl08.config(text=Alist[7], bg="green")
    lbl07.config(text=Alist[8], bg="green")
    lbl06.config(text=Alist[9], bg="green")
    lbl05.config(text=Alist[10], bg="green")

    lbl04.config(text=Alist[11], bg="blue")
    lbl03.config(text=Alist[12], bg="blue")
    lbl02.config(text=Alist[13], bg="blue")
    lbl01.config(text=Alist[14], bg="blue")
    lbl00.config(text=Alist[15], bg="blue")
    select(color=colors, sel1=sel1, sel2=sel3, sel3=sel2)


top = Tk()
top.title("Плотность тока")
top.resizable(False, False)
top.config(bg="black")

lbl0 = Label(top, bg="cadet blue", text="Номер дачика", width=60)
lbl0.grid(row=0, column=0, columnspan=16, pady=5, padx=5)

var = IntVar()
var.set(1)
spin = Spinbox(top, from_=1, to=4, width=60, textvariable=var)

spin.grid(row=1, column=0, columnspan=16, pady=5, padx=5)

v = DoubleVar()
scale = Scale(top, variable=v, from_=1, to=12, orient=HORIZONTAL,
              tickinterval=1, resolution=0.1, length=400
              )
scale.grid(row=2, column=0, columnspan=16, pady=5, padx=5)

btn = Button(top, text="Рассчитать", width=60, command=kodek)
btn.grid(row=3, column=0, columnspan=16, pady=5, padx=5)

lbl1 = Label(top, bg="CadetBlue3", text="Код устройства", width=30, height=1)
lbl1.grid(row=4, column=0, columnspan=6, pady=5, padx=5)

lbl2 = Label(top, bg="CadetBlue3", text="Код дачика", width=30, height=1)
lbl2.grid(row=4, column=8, columnspan=6, pady=5, padx=5)

lbl3 = Label(top, bg="black", width=30, height=1)
lbl3.grid(row=5, column=0, columnspan=6, pady=5, padx=5)

lbl4 = Label(top, bg="black", width=30, height=1)
lbl4.grid(row=5, column=8, columnspan=6, pady=5, padx=5)

# ----------------------------------------------------------

lbl00 = Label(top, bg="black", width=1, height=1)
lbl00.grid(row=6, column=0, pady=2, padx=2)

lbl01 = Label(top, bg="black", width=1, height=1)
lbl01.grid(row=6, column=1, pady=2, padx=2)

lbl02 = Label(top, bg="black", width=1, height=1)
lbl02.grid(row=6, column=2, pady=2, padx=2)

lbl03 = Label(top, bg="black", width=1, height=1)
lbl03.grid(row=6, column=3, pady=2, padx=2)

lbl04 = Label(top, bg="black", width=1, height=1)
lbl04.grid(row=6, column=4, pady=2, padx=2)

lbl05 = Label(top, bg="black", width=1, height=1)
lbl05.grid(row=6, column=5, pady=2, padx=2)

lbl06 = Label(top, bg="black", width=1, height=1)
lbl06.grid(row=6, column=6, pady=2, padx=2)

lbl07 = Label(top, bg="black", width=1, height=1)
lbl07.grid(row=6, column=7, pady=2, padx=2)

lbl08 = Label(top, bg="black", width=1, height=1)
lbl08.grid(row=6, column=8, pady=2, padx=2)

lbl09 = Label(top, bg="black", width=1, height=1)
lbl09.grid(row=6, column=9, pady=2, padx=2)

lbl010 = Label(top, bg="black", width=1, height=1)
lbl010.grid(row=6, column=10, pady=2, padx=2)

lbl011 = Label(top, bg="black", width=1, height=1)
lbl011.grid(row=6, column=11, pady=2, padx=2)

lbl012 = Label(top, bg="black", width=1, height=1)
lbl012.grid(row=6, column=12, pady=2, padx=2)

lbl013 = Label(top, bg="black", width=1, height=1)
lbl013.grid(row=6, column=13, pady=2, padx=2)

lbl014 = Label(top, bg="black", width=1, height=1)
lbl014.grid(row=6, column=14, pady=2, padx=2)

lbl015 = Label(top, bg="black", width=1, height=1)
lbl015.grid(row=6, column=15, pady=2, padx=2)

# ----------------------------------------------------------

lbl = Label(top, bg="black", width=71, height=4)
lbl.grid(row=7, column=0, columnspan=18, pady=5, padx=5)

top.mainloop()
