from tkinter import *
import ConversionPage
import DataCharts

root = Tk()
root.geometry("400x400")
root.configure(background="grey")

fTitle = Label(text="Currency Tool",
               background="grey",
               font="Arial 15").place(x=140, y=50)

cButton = Button(root,
                 text="Conversion",
                 command=lambda: ConversionPage.cPage(root),
                 justify=CENTER,
                 height=3,
                 width=15,
                 activebackground='light blue',
                 relief="raised").place(x=145, y=100)

daButton = Button(root,
                 text="Data Charts",
                 command=lambda: DataCharts.dPage(root),
                 justify=CENTER,
                 height=3,
                 width=15,
                 activebackground='light blue',
                 relief="raised").place(x=145, y=190)

root.mainloop()
