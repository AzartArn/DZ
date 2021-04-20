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


def kodek():
    d = float(v.get())
    bit1 = destobin(int(var.get())+22)
    bit2 = destobin(int(var.get())+44)
    if d < 4.2 or d > 7.8:
        sel1 = "Аварийное состояние"
        sel2 = bit1
        sel3 = "00000"
        bit2 = "00000"
        colors = "red2"
    elif d > 5.3 and d < 6.7:
        sel1 = "В пределах нормы"
        sel2 = bit1
        sel3 = "00000"
        bit2 = "00000"
        colors = "SpringGreen2"
    elif d > 4.1 and d < 5.4:
        sel1 = "Напряжение увеличено \nИсполяющие устройство Блок питания №"\
            + str(var.get()) + "\nПоказатель ЦАП +" + str(d/10.0*A2+B2)
        sel2 = str(bit1)
        sel3 = str(bit2)
        colors = "dark orange"
    elif d > 6.6 and d < 7.9:
        sel1 = "Напряжение увеличено \nИсполяющие устройство Блок питания №"\
            + str(var.get()) + "\nПоказатель ЦАП -" + str(d/12.0*A2+B2)
        sel2 = str(bit1)
        sel3 = str(bit2)
        colors = "dark orange"
    Alist = lists(bit1, bit2)

    lbl015.config(text=Alist[0], bg="yellow")
    lbl014.config(text=Alist[1], bg="yellow")
    lbl013.config(text=Alist[2], bg="yellow")
    lbl012.config(text=Alist[3], bg="yellow")
    lbl011.config(text=Alist[4], bg="yellow")

    lbl010.config(text=Alist[5], bg="lightgreen")
    lbl09.config(text=Alist[6], bg="lightgreen")
    lbl08.config(text=Alist[7], bg="lightgreen")
    lbl07.config(text=Alist[8], bg="lightgreen")
    lbl06.config(text=Alist[9], bg="lightgreen")
    lbl05.config(text=Alist[10], bg="lightgreen")

    lbl04.config(text=Alist[11], bg="lightblue")
    lbl03.config(text=Alist[12], bg="lightblue")
    lbl02.config(text=Alist[13], bg="lightblue")
    lbl01.config(text=Alist[14], bg="lightblue")
    lbl00.config(text=Alist[15], bg="lightblue")

    lbl.config(text=sel1, bg=colors)
    lbl4.config(text=sel2, bg="dark orange")
    lbl3.config(text=sel3, bg="dark orange")


top = Tk()
top.title("Плотность тока")
top.resizable(False, False)
top.config(bg="black")

lbl0 = Label(top, bg="light coral", text="Номер дачика", width=46)
lbl0.grid(row=0, column=0, columnspan=2, pady=5, padx=5)

var = IntVar()
var.set(1)
spin = Spinbox(top, from_=1, to=4, width=52, textvariable=var)

spin.grid(row=1, column=0, columnspan=2, pady=5, padx=5)

v = DoubleVar()
scale = Scale(top, variable=v, from_=1, to=12, orient=HORIZONTAL,
              tickinterval=1, resolution=0.1, length=320
              )
scale.grid(row=2, column=0, columnspan=2, pady=5, padx=5)

btn = Button(top, bg="OliveDrab2", text="Рассчитать", width=46, command=kodek)
btn.grid(row=3, column=0, columnspan=2, pady=5, padx=5)

lbl1 = Label(top, bg="dark orange", text="Код устройства", width=20, height=1)
lbl1.grid(row=4, column=0, pady=5, padx=5)

lbl2 = Label(top, bg="dark orange", text="Код дачика", width=20, height=1)
lbl2.grid(row=4, column=1, pady=5, padx=5)

lbl3 = Label(top, bg="black", width=20, height=1)
lbl3.grid(row=5, column=0, pady=5, padx=5)

lbl4 = Label(top, bg="black", width=20, height=1)
lbl4.grid(row=5, column=1, pady=5, padx=5)

fr = Frame(top, bg="black")
fr.grid(row=6, column=0, columnspan=2, pady=2, padx=2)

# ----------------------------------------------------------

lbl00 = Label(fr, bg="black", width=1, height=1)
lbl00.pack(side=LEFT, padx=2, pady=2)

lbl01 = Label(fr, bg="black", width=1, height=1)
lbl01.pack(side=LEFT, padx=2, pady=2)

lbl02 = Label(fr, bg="black", width=1, height=1)
lbl02.pack(side=LEFT, padx=2, pady=2)

lbl03 = Label(fr, bg="black", width=1, height=1)
lbl03.pack(side=LEFT, padx=2, pady=2)

lbl04 = Label(fr, bg="black", width=1, height=1)
lbl04.pack(side=LEFT, padx=2, pady=2)

lbl05 = Label(fr, bg="black", width=1, height=1)
lbl05.pack(side=LEFT, padx=2, pady=2)

lbl06 = Label(fr, bg="black", width=1, height=1)
lbl06.pack(side=LEFT, padx=2, pady=2)

lbl07 = Label(fr, bg="black", width=1, height=1)
lbl07.pack(side=LEFT, padx=2, pady=2)

lbl08 = Label(fr, bg="black", width=1, height=1)
lbl08.pack(side=LEFT, padx=2, pady=2)

lbl09 = Label(fr, bg="black", width=1, height=1)
lbl09.pack(side=LEFT, padx=2, pady=2)

lbl010 = Label(fr, bg="black", width=1, height=1)
lbl010.pack(side=LEFT, padx=2, pady=2)

lbl011 = Label(fr, bg="black", width=1, height=1)
lbl011.pack(side=LEFT, padx=2, pady=2)

lbl012 = Label(fr, bg="black", width=1, height=1)
lbl012.pack(side=LEFT, padx=2, pady=2)

lbl013 = Label(fr, bg="black", width=1, height=1)
lbl013.pack(side=LEFT, padx=2, pady=2)

lbl014 = Label(fr, bg="black", width=1, height=1)
lbl014.pack(side=LEFT, padx=2, pady=2)

lbl015 = Label(fr, bg="black", width=1, height=1)
lbl015.pack(side=LEFT, padx=2, pady=2)

# ----------------------------------------------------------

lbl = Label(top, bg="black", width=46, height=4)
lbl.grid(row=7, column=0, columnspan=2, pady=5, padx=5)

top.mainloop()
