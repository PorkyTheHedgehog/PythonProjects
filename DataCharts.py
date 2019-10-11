from tkinter import *
from tkinter import messagebox
import Formulas
from matplotlib import pyplot as plt
import mplcursors

def back(root, chartsp):
    root.deiconify()
    chartsp.withdraw()


def timeperiod(A, B, period, start="NA", end="NA"):
    try:
        ds, ccp = Formulas.currencytrends(A, B, period, start, end)
    except Exception:
        messagebox.showerror(title="Error", message="Invalid Input")
    plt.plot_date(ds, ccp, linestyle='-', marker='o', color='black')
    plt.xlabel("Time (Days)")
    plt.xticks(rotation=45)
    plt.ylabel("Value ($)")

    mplcursors.cursor()
    plt.show()


def others(A, B):
    oWindow = Toplevel(chartsp)
    oWindow.geometry("380x80")
    Label(oWindow, text="Start Date (YYYY-MM-DD)").grid(row=0)
    Label(oWindow, text="End Date (YYYY-MM-DD)").grid(row=1)

    ys = Entry(oWindow, width=10, justify="center")
    ys.grid(row=0, column=1)
    Label(oWindow, text="-").grid(row=0, column=2)
    ms = Entry(oWindow, width=10, justify="center")
    ms.grid(row=0, column=3)
    Label(oWindow, text="-").grid(row=0, column=4)
    ds = Entry(oWindow, width=10, justify="center")
    ds.grid(row=0, column=5)

    ye = Entry(oWindow, width=10, justify="center")
    ye.grid(row=1, column=1)
    Label(oWindow, text="-", justify="center").grid(row=1, column=2)
    me = Entry(oWindow, width=10, justify="center")
    me.grid(row=1, column=3)
    Label(oWindow, text="-", justify="center").grid(row=1, column=4)
    de = Entry(oWindow, width=10, justify="center")
    de.grid(row=1, column=5)

    period = "o"

    Button(oWindow,
           text="Confirm",
           command=lambda: timeperiod(A,
                                      B,
                                      period,
                                      "{}-{}-{}".format(ys.get(), "{:02d}".format(int(ms.get())),"{:02d}".format(int(ds.get()))),
                                      "{}-{}-{}".format(ye.get(), "{:02d}".format(int(me.get())),"{:02d}".format(int(de.get())))),
           justify=CENTER,
           height=1,
           width=9,
           activebackground='light blue',
           relief="raised").place(x=300, y=50)


def dPage(root):
    chartsp = Toplevel(root)
    root.withdraw()
    chartsp.geometry("400x400")
    chartsp.configure(bg="grey")

    Label(chartsp,
          text="Forex Charts",
          background="grey",
          font="Arial 15").place(x=140, y=20)

    Label(chartsp,
          bg="grey",
          text="wrt",
          font="Arial 15").place(x=180, y=100)

    ccL = Formulas.cc()

    cA = StringVar(chartsp)
    cA.set(ccL[0])
    oA = OptionMenu(chartsp,
                    cA,
                    *ccL)
    oA["highlightthickness"] = 0
    oA.place(x=35, y=102)

    cB = StringVar(chartsp)
    cB.set(ccL[0])
    oB = OptionMenu(chartsp,
                    cB,
                    *ccL)
    oB["highlightthickness"] = 0
    oB.place(x=240, y=102)

    Label(chartsp,
          bg="grey",
          text="Time Frame",
          font="Arial 15").place(x=140, y=180)

    wButton = Button(chartsp,
                     text="1 Week",
                     command=lambda: timeperiod(cA.get()[:3], cB.get()[:3], "w"),
                     justify=CENTER,
                     height=1,
                     width=15,
                     activebackground='light blue',
                     relief="raised").place(x=140, y=220)

    mButton = Button(chartsp,
                     text="1 Month",
                     command=lambda: timeperiod(cA.get()[:3], cB.get()[:3], "m"),
                     justify=CENTER,
                     height=1,
                     width=15,
                     activebackground='light blue',
                     relief="raised").place(x=140, y=250)

    yButton = Button(chartsp,
                     text="1 Year",
                     command=lambda: timeperiod(cA.get()[:3], cB.get()[:3], "y"),
                     justify=CENTER,
                     height=1,
                     width=15,
                     activebackground='light blue',
                     relief="raised").place(x=140, y=280)

    oButton = Button(chartsp,
                     text="Others",
                     command=lambda: others(cA.get()[:3], cB.get()[:3]),
                     justify=CENTER,
                     height=1,
                     width=15,
                     activebackground='light blue',
                     relief="raised").place(x=140, y=310)

    bButton = Button(chartsp,
                     text="←",
                     command=lambda: back(root, chartsp),
                     justify=CENTER,
                     height=1,
                     width=3,
                     bg = "grey",
                     activebackground='light blue',
                     relief="flat").place(x=20, y=20)

    chartsp.mainloop()
