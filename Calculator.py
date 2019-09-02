from tkinter import *


def equal():
    try:
        ans = eval(ent.get())
    except Exception:
        ans = "INVALID"
    finally:
        ent.delete(0, END)
        ent.insert(0, ans)
        equal.called = True
    return


def Values(text):
    if ent.get() == "INVALID":
        ent.delete(0, END)
    elif equal.called:
        if text not in [" + ", " - ", " * ", " / "]:
            ent.delete(0, END)
    equal.called = False
    if text == " ( " and ent.get()[-1] in "1234567890":
            ent.insert(END, " * ")
    ent.insert(END, text)
    return


def clear():
    ent.delete(0, END)
    return


def rid():
    ent.delete(len(ent.get())-1)
    return


top = Tk()
top.geometry("350x400")
top.configure(background = "grey")
ent = Entry(top, bd=0, bg= "light blue", font = "Calibri 16")
ent.pack(side=RIGHT)
ent.place(x=50, y=50, height=50, width=263)

equal.called = False

A = Button(top, text=1, command=lambda: Values(1), justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=50, y=150)
B = Button(top, text=2, command=lambda: Values(2), justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=103, y=150)
C = Button(top, text=3, command=lambda: Values(3), justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=156, y=150)
D = Button(top, text=4, command=lambda: Values(4), justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=50, y=206)
E = Button(top, text=5, command=lambda: Values(5), justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=103, y=206)
F = Button(top, text=6, command=lambda: Values(6), justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=156, y=206)
G = Button(top, text=7, command=lambda: Values(7), justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=50, y=262)
H = Button(top, text=8, command=lambda: Values(8), justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=103, y=262)
I = Button(top, text=9, command=lambda: Values(9), justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=156, y=262)
J = Button(top, text=0, command=lambda: Values(0), justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=103, y=318)
K = Button(top, text=" .", command=lambda: Values("."), justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=50, y=318)
L = Button(top, text="=", command=equal, justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=262, y=318)
M = Button(top, text="+", command=lambda: Values(" + "), justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=209, y=150)
N = Button(top, text="-", command=lambda: Values(" - "), justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=209, y=206)
O = Button(top, text="*", command=lambda: Values(" * "), justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=209, y=262)
P = Button(top, text="/", command=lambda: Values(" / "), justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=209, y=318)
Q = Button(top, text="mod", command=lambda: Values(" % "), justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=156, y=318)
R = Button(top, text="C", command=rid, justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=262, y=262)
S = Button(top, text="CE", command=clear, justify=CENTER, height=3, width=6, activebackground='light blue', relief="raised")\
   .place(x=262, y=206)
T= Button(top, text="(", command=lambda: Values(" ( "), justify=CENTER, height=3, width=2, activebackground='light blue', relief="raised")\
   .place(x=262, y=150)
U= Button(top, text=")", command=lambda: Values(" ) "), justify=CENTER, height=3, width=2, activebackground='light blue', relief="raised")\
   .place(x=290, y=150)

top.mainloop()
