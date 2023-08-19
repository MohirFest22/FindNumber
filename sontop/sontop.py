"""
19-08-2023
Mavzu: Kompyuter o'ylagan sonnni topish dasturi
Muallif: Arslonov Sunnat
"""
import random
from tkinter import *
t = Tk()
t.title("SON TOP o'yini")
t.geometry("350x500")
t.configure(bg="#FF7349")
title = Label(text="SON TOP",fg="yellow",font="Stencil 26",bg="limegreen")
title.pack()
sonVar = IntVar()
inputt = Entry(font="Arial 10",textvariable=sonVar)
inputt.place(relx=0.3,rely=0.2)

oyla = random.randint(1,100)
oyla_l = Label(text="1 dan 100 gacha son o'yladim, toping!",font="Arial 13",fg="blue",bg="#FF7349")
oyla_l.place(relx=0.08,rely=0.3)


def clear():
 inputt.delete(0,END)
 results.config(text="")
def num7():
 inputt.insert(len(inputt.get()),"7")
def num8():
 inputt.insert(len(inputt.get()),"8")
def num9():
 inputt.insert(len(inputt.get()),"9")
def num4():
 inputt.insert(len(inputt.get()),"4")
def num5():
 inputt.insert(len(inputt.get()),"5")
def num6():
 inputt.insert(len(inputt.get()),"6")
def num1():
 inputt.insert(len(inputt.get()),"1")
def num2():
 inputt.insert(len(inputt.get()),"2")
def num3():
 inputt.insert(len(inputt.get()),"3")
def zero():
 inputt.insert(len(inputt.get()),"0")
def equal():
    if sonVar.get()<oyla:
        results.config(text=f"O'ylangan son {sonVar.get()} dan katta")
        print(oyla)
    elif sonVar.get()>oyla:
        results.config(text=f"O'ylangan son {sonVar.get()} dan kichik")
        print(oyla)
    else:
        results.config(text="O'ylangan sonni topdingiz🎉🎉🎉")
        print(oyla)
        


num7_btn = Button(text="7",width="5",height="2",fg="limegreen",bg="#28231d",command=num7)
num7_btn.place(relx=0.18,rely=0.4)

num8_btn = Button(text="8",width="5",height="2",fg="limegreen",bg="#28231d",command=num8)
num8_btn.place(relx=0.43,rely=0.4)

num9_btn = Button(text="9",width="5",height="2",fg="limegreen",bg="#28231d",command=num9)
num9_btn.place(relx=0.7,rely=0.4)


num4_btn = Button(text="4",width="5",height="2",fg="limegreen",bg="#28231d",command=num4)
num4_btn.place(relx=0.18,rely=0.5)

num5_btn = Button(text="5",width="5",height="2",fg="limegreen",bg="#28231d",command=num5)
num5_btn.place(relx=0.43,rely=0.5)

num6_btn = Button(text="6",width="5",height="2",fg="limegreen",bg="#28231d",command=num6)
num6_btn.place(relx=0.7,rely=0.5)


num1_btn = Button(text="1",width="5",height="2",fg="limegreen",bg="#28231d",command=num1)
num1_btn.place(relx=0.18,rely=0.6)

num2_btn = Button(text="2",width="5",height="2",fg="limegreen",bg="#28231d",command=num2)
num2_btn.place(relx=0.43,rely=0.6)

num3_btn = Button(text="3",width="5",height="2",fg="limegreen",bg="#28231d",command=num3)
num3_btn.place(relx=0.7,rely=0.6)

c_btn = Button(text="C",width="5",height="2",fg="red",bg="#28231d",command=clear)
c_btn.place(relx=0.18,rely=0.7)

zero_btn = Button(text="0",width="5",height="2",fg="limegreen",bg="#28231d",command=zero)
zero_btn.place(relx=0.43,rely=0.7)


equal_btn = Button(text="=",width="5",height="2",fg="white",bg="limegreen",command=equal)
equal_btn.place(relx=0.7,rely=0.7)

results= Label(text="",font="Arial 15",width="30",bg="#FF7349",fg="limegreen")
results.place(relx=0.05,rely=0.8)

tryy = Label(text="Urunishlar: ")

t.mainloop()
