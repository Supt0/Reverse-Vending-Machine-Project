from tkinter import *
from PIL import ImageTk, Image
def Gogreen():
    root = Tk()
    root.title("Vending Machine")
    root.geometry("350x300")
    root.configure(background='light cyan')

    def returnamount(bottle):
        amount  =  str(bottle * 5)
        secondLabel = Label (root,bg='light cyan',text = " You will get "+amount+" Taka",fg='forest green',font=(None,12))
        secondLabel.place(x=70, y=103)

    recycle = ImageTk.PhotoImage(Image.open("recycleblack.png"))

    firstLabel = Label(root,text = "How many Bottle you do you have??? ",fg='gray30',bg='light cyan',font=(None,12)).grid(row = 1,column = 1,pady = 20)
    EntryBox = Entry(root,width = 16,bg='light green')
    EntryBox.grid(row=2 , column = 1)
    recyclebutton = Button(root,text='RECYCLE',compound=TOP,image=recycle,bg='light cyan',command= lambda : returnamount(int(EntryBox.get())))
    recyclebutton.place(x=90, y=140)




    root.mainloop()