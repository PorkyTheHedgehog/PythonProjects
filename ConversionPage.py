from tkinter import *
from tkinter import messagebox
import Formulas

def back(root, cWindow):
    root.deiconify()
    cWindow.withdraw()

def ok(ccF, ccL, amt, ent2):
    try:
        amt = float(amt)
        ent2.delete(0, END)
        ent2.insert(0, Formulas.conv(ccF, ccL, amt))
    except ValueError:
        messagebox.showerror(title="Error", message="Invalid Input")
    except NameError:
        messagebox.showerror(title="Error", message="Missing Input")


def cPage(root):

    cWindow = Toplevel(root)
    root.withdraw()
    cWindow.geometry("400x400")
    cWindow.configure(background="Grey")

    Label(cWindow,
          text="Currency Conversion",
          background="grey",
          font="Arial 15").place(x=110, y=20)

    ent = Entry(cWindow, bd=0, bg="white", font="Calibri 16")
    ent.place(x=30, y=100, height=26, width=300)

    ent2 = Entry(cWindow, bd=0, bg="white", font="Calibri 16")
    ent2.place(x=30, y=220, height=26, width=300)

    ccL = Formulas.cc()
    ccSf = StringVar(cWindow)
    ccSf.set(ccL[0])
    oF = OptionMenu(cWindow,
                    ccSf,
                    *ccL)
    oF["highlightthickness"] = 0
    oF.place(x=250, y=100)

    Label(cWindow,
          text="=",
          background="grey",
          font="Arial 15").place(x=195, y=160)

    ccSl = StringVar(cWindow)
    ccSl.set(ccL[0])
    oL = OptionMenu(cWindow,
                    ccSl,
                    *ccL)
    oL["highlightthickness"] = 0
    oL.place(x=250, y=220)

    cButton = Button(cWindow,
                     text="Confirm",
                     command=lambda: ok(ccSf.get()[:3], ccSl.get()[:3], ent.get(), ent2),
                     justify=CENTER,
                     height=1,
                     width=10,
                     activebackground='light blue',
                     relief="raised").place(x=300, y=350)

    bButton = Button(cWindow,
                     text="←",
                     command=lambda: back(root, cWindow),
                     justify=CENTER,
                     height=1,
                     width=3,
                     bg = "grey",
                     activebackground='light blue',
                     relief="flat").place(x=20, y=20)

