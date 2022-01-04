from tkinter import *
import math
def Perm():
    try:
        value = math.perm(int(scvalue.get()), int(scvalue1.get()))
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def deg():
    try:
        value = math.degrees(float(scvalue.get()))
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def rad():
    try:
        value = math.radians(float(scvalue.get()))
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def Bin():
    try:
        value = bin(int(scvalue.get()))
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def Oct():
    try:
        value = oct(int(scvalue.get()))
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def Hex():
    try:
        value = hex(int(scvalue.get()))
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def sin():
    try:
        value = math.sin(math.radians(float(scvalue.get())))
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def Isin():
    try:
        value = math.degrees(math.asin(float(scvalue.get())))
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def cos():
    try:
        value = math.cos(math.radians(float(scvalue.get())))
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def Icos():
    try:
        value = math.degrees(math.acos(float(scvalue.get())))
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def tan():
    try:
        value = math.tan(math.radians(float(scvalue.get())))
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def Itan():
    try:
        value = math.degrees(math.atan(float(scvalue.get())))
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def RNPr():
    try:
        z1 = []
        for i in range(int(scvalue.get()), int(scvalue1.get())):
            z = []
            for j in range(1, i):
                if i % j == 0:
                    z.append(j)
            m = sum(z)
            if i > 1:
                if m == i:
                    z1.append(i)
                else:
                    pass
            if i <= 1:
                pass
        value=len(z1)
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def RLPr():
    try:
        z1 = []
        for i in range(int(scvalue.get()), int(scvalue1.get())):
            z = []
            for j in range(1, i):
                if i % j == 0:
                    z.append(j)
            m = sum(z)
            if i > 1:
                if m == i:
                    z1.append(i)
                else:
                    pass
            if i <= 1:
                pass
        value= z1[:]
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def ISPr():
    try:
        z = []
        for i in range(1, int(scvalue.get())):
            if int(scvalue.get()) % i == 0:
                z.append(i)
        y = sum(z)
        if int(scvalue.get()) > 1:
            if y == int(scvalue.get()):
                value="yes"
            else:
                value="No"
        if int(scvalue.get()) <= 1:
                value="No"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def RNO():
    try:
        z=[]
        for i in range(int(scvalue.get()), int(scvalue1.get())+1):
            if i%2!=0:
                z.append(i)
        value=len(z)
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def RNE():
    try:
        z=[]
        for i in range(int(scvalue.get()), int(scvalue1.get())+1):
            if i%2==0:
                z.append(i)
        value=len(z)
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def logXb():
    try:
        value = math.log(int(scvalue.get()), int(scvalue1.get()))
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def log():
    try:
        value = math.log(int(scvalue.get()), 10)
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def p():
    try:
        value = float(scvalue.get())/100
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def inv():
    try:
        value = 1 / float(scvalue.get())
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value="Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def isp():
    try:
        if int(scvalue.get()) > 1:
            for i in range(2, int(scvalue.get())):
                if int(scvalue.get()) % i == 0:
                    value = "No"
                    break
            else:
                value = "yes"

        else:
            value = "No"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def np():
    try:
        z = []
        for i in range(int(scvalue.get()), int(scvalue1.get()) + 1):
            if i > 1:
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    z.append(i)
        value = z[:]
        scvalue.set(len(value))
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def hcf():
    try:
        value=math.gcd(int(scvalue.get()), int(scvalue1.get()))
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def lcm():
    try:
        value=math.lcm(int(scvalue.get()), int(scvalue1.get()))
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def pow():
    try:
        value=math.pow(int(scvalue.get()), int(scvalue1.get()))
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def fct():
    try:
        value = math.factorial(int(scvalue.get()))
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def sqr():
    try:
        value = float(scvalue.get()) ** 2
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def cb():
    try:
        value = float(scvalue.get()) ** 3
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value= "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def cbrt():
    try:
        value = float(scvalue.get()) ** (1 / 3)
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value= "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def sqrt():
    try:
        value = float(scvalue.get()) ** (1 / 2)
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value= "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def lrp():
    try:
        z = []
        for i in range(int(scvalue.get()), int(scvalue1.get()) + 1):
            if i > 1:
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    z.append(i)
        value = z[:]
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
    except:
        value = "Syntex Error"
        scvalue.set(value)
        screen.update()
        scvalue1.set("")
def click(event):
    global scvalue
    global scvalue1
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except:
                value="Syntax Error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        scvalue1.set("")
        screen.update()
        screen1.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
root = Tk()
root.geometry("365x410")
root.maxsize(1040, 410)
root.minsize(365, 410)
root.title("CALCULATOR BY ANKUSH")
root.wm_iconbitmap("icons8-calculator-64.ico")
root.configure(background="gray")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar = scvalue,font="lucida 30 bold")
screen.pack(fill="both", ipadx=5,pady=8, padx=10)

scvalue1 = StringVar()
scvalue1.set("")
screen1 = Entry(root,textvar = scvalue1,font="lucida 30 bold")
screen1.pack(fill="both", ipadx=5,pady=8,  padx=10)

f=Frame(root, bg="gray")
b=Button(f,text="1", padx=18, pady=12, font="lucida 10 bold", bg="gray")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text="2", padx=18, pady=12, font="lucida 10 bold", bg="gray")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text="3", padx=18, pady=12, font="lucida 10 bold", bg="gray")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text="+", padx=18, pady=12, font="lucida 10 bold", bg="gray")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text="C", padx=18, pady=12, font="lucida 10 bold", bg="red")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text="cbrt", padx=15, pady=12, font="lucida 8 bold", bg="gray",fg="green", command=cbrt)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="HCF", padx=15, pady=12, font="lucida 8 bold", bg="gray", command=hcf)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="INV", padx=15, pady=12, font="lucida 10 bold", bg="gray", command=inv)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="RNE", padx=15, pady=12, font="lucida 10 bold", bg="gray", command=RNE)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="ISP", padx=15, pady=12, font="lucida 10 bold", bg="gray", command=isp)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="sin", padx=15, pady=12, font="lucida 10 bold", bg="gray", command=sin)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="Icos", padx=15, pady=12, font="lucida 10 bold", bg="gray", command=Icos)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="hex", padx=15, pady=12, font="lucida 10 bold", bg="gray", command=Hex)
b.pack(side=LEFT, padx=10, pady=8)
f.pack()

f=Frame(root, bg="gray")
b=Button(f,text="4", padx=18, pady=12, font="lucida 10 bold", bg="gray")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text="5", padx=18, pady=12, font="lucida 10 bold", bg="gray")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text="6", padx=18, pady=12, font="lucida 10 bold", bg="gray")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text="-", padx=18, pady=12, font="lucida 10 bold", bg="gray")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text="(", padx=18, pady=12, font="lucida 11 bold", bg="gray")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text="cb", padx=18, pady=12, font="lucida 10 bold", bg="gray", command=cb)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="LCM", padx=15, pady=12, font="lucida 8 bold", bg="gray", command=lcm)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="%", padx=18, pady=12, font="lucida 12 bold", bg="gray", command=p)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="RNO", padx=15, pady=12, font="lucida 9 bold", bg="gray", command=RNO)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="ISPr", padx=15, pady=12, font="lucida 9 bold", bg="gray", command=ISPr)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="cos", padx=15, pady=12, font="lucida 10 bold", bg="gray", command=cos)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="Itan", padx=15, pady=12, font="lucida 10 bold", bg="gray", command=Itan)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="rad", padx=15, pady=12, font="lucida 10 bold", bg="gray", command=rad)
b.pack(side=LEFT, padx=10, pady=8)
f.pack()

f=Frame(root, bg="gray")
b=Button(f,text="7", padx=18, pady=12, font="lucida 10 bold", bg="gray")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text="8", padx=18, pady=12, font="lucida 10 bold", bg="gray")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text="9", padx=18, pady=12, font="lucida 10 bold", bg="gray")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text="*", padx=18, pady=12, font="lucida 10 bold", bg="gray")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text=")", padx=18, pady=12, font="lucida 10 bold", bg="gray")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text="sqrt", padx=15, pady=12, font="lucida 8 bold", bg="gray", command=sqrt)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="POW", padx=15, pady=12, font="lucida 8 bold", bg="gray", command=pow)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="log()", padx=15, pady=12, font="lucida 10 bold", bg="gray", command=log)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="RNP", padx=15, pady=12, font="lucida 9 bold", bg="gray", command=np)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="RLP", padx=15, pady=12, font="lucida 9 bold", bg="gray", command=lrp)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="tan", padx=15, pady=12, font="lucida 10 bold", bg="gray", command=tan)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="bin", padx=15, pady=12, font="lucida 10 bold", bg="gray", command=Bin)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="deg", padx=15, pady=12, font="lucida 10 bold", bg="gray", command=deg)
b.pack(side=LEFT, padx=10, pady=8)
f.pack()

f=Frame(root, bg="gray")
b=Button(f,text="0", padx=18, pady=12, font="lucida 10 bold", bg="gray")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text=".", padx=18, pady=12, font="lucida 10 bold", bg="gray")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text="00", padx=15, pady=12, font="lucida 10 bold", bg="yellow")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text="/", padx=18, pady=12, font="lucida 10 bold", bg="gray")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text="=", padx=18, pady=12, font="lucida 10 bold", bg="gray")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)

b=Button(f,text="sqr", padx=18, pady=12, font="lucida 10 bold", bg="gray", command=sqr)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="FCT", padx=15, pady=12, font="lucida 10 bold", bg="gray", command=fct)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="logXb", padx=10, pady=12, font="lucida 10 bold", bg="gray", command=logXb)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="RNPr", padx=10, pady=12, font="lucida 10 bold", bg="gray", command=RNPr)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="RLPr", padx=10, pady=12, font="lucida 10 bold", bg="gray", command=RLPr)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="Isin", padx=15, pady=12, font="lucida 10 bold", bg="gray", command=Isin)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="oct", padx=15, pady=12, font="lucida 10 bold", bg="gray", command=Oct)
b.pack(side=LEFT, padx=10, pady=8)

b=Button(f,text="perm", padx=12, pady=12, font="lucida 8 bold", bg="gray", command=Perm)
b.pack(side=LEFT, padx=10, pady=8)
f.pack()
root.mainloop()