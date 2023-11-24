from tkinter import *
from PIL import ImageTk, Image
from FInal_Project import vending_interface
from FInal_Project import GoGreen_Window



root = Tk()
root.title("Vending Machine")
root.geometry("900x630")

root.iconbitmap('icon.ico')

###################   COLOR VERSION 1   ##########

root.configure(background='#461942')

def Call_Vending_Machine():
    root.destroy()
    vending_interface.VendingMachine()
def Call_Gogreen():
    root.destroy()
    GoGreen_Window.Gogreen()

welcome= ImageTk.PhotoImage(Image.open("welcome.png"))
BG = ImageTk.PhotoImage(Image.open("dvendingcolor2.png"))
bangla = ImageTk.PhotoImage(Image.open("dhi.png"))
purchase = ImageTk.PhotoImage(Image.open("insertgrey.png"))
gogreen = ImageTk.PhotoImage(Image.open("greengrey.png"))

bgimage = Label(root,image=BG,bg='#461942')
bgimage.place(x=450, y=100)
welcomelabel = Label(root,bg='#461942', image=welcome)
welcomelabel.place(x=250, y=0)
banglatext = Label(root,image=bangla,bg='#461942')
banglatext.place(x=0, y=100)

emptylabel = Label(root,bg='#461942').grid(row=0,column=0,padx=10,pady=10)
PurchaseItem = Button(root,bg='#626a77',text='PURCHASE',fg='white',compound=TOP,image=purchase,command = Call_Vending_Machine)
PurchaseItem.place(x=740,y=180)
GoGreen = Button(root,bg='#626a77',text='RECYCLE',fg='white',compound=TOP,image=gogreen,command = Call_Gogreen)
GoGreen.place(x=740,y=320)



### COLOR VERSION 2  ###########

# root.configure(background='light blue')
#
# def Call_Vending_Machine():
#     #root.destroy()
#     Graphical_Interface.VendingMachine()
#
#
# def Call_Gogreen():
#     root.destroy()
#     GoGreen_Window.Gogreen()
#
# welcome= ImageTk.PhotoImage(Image.open("welcome.png"))
# BG = ImageTk.PhotoImage(Image.open("dvendingcolor.png"))
# bangla = ImageTk.PhotoImage(Image.open("dbangla.png"))
# purchase = ImageTk.PhotoImage(Image.open("insertgrey.png"))
# gogreen = ImageTk.PhotoImage(Image.open("greengrey.png"))
#
# bgimage = Label(root,image=BG,bg='light blue')
# bgimage.place(x=450, y=100)
# welcomelabel = Label(root,bg='light blue', image=welcome)
# welcomelabel.place(x=250, y=0)
# banglatext = Label(root,image=bangla,bg='light blue')
# banglatext.place(x=0, y=100)
#
# emptylabel = Label(root,bg='light blue').grid(row=0,column=0,padx=10,pady=10)
# PurchaseItem = Button(root,bg='#626a77',text='PURCHASE',fg='white',compound=TOP,image=purchase,command = Call_Vending_Machine)
# PurchaseItem.place(x=740,y=180)
# GoGreen = Button(root,bg='#626a77',text='RECYCLE',fg='white',compound=TOP,image=gogreen,command = Call_Gogreen)
# GoGreen.place(x=740,y=320)


root.mainloop()