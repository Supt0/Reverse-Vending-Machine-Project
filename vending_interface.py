from tkinter import *
from PIL import ImageTk, Image
from FInal_Project import basecode



def VendingMachine():
    root = Tk()
    root.title("Vending Machine")
    root.geometry("620x750")
    root.configure(background='light blue')
    root.iconbitmap('icon.ico')

    # To call multiple function
    def item_and_price(item):
        basecode.selected_item(item)
        basecode.update_price(item)
        Pay_Label = Label(root, text="Please pay: "+ str(basecode.update_price(item))+" Taka",bg='#626a77',fg='white', font=(None, 13) ).place(x=40, y=480)



    def cashbackLabel(money):
        cashbackLabel = Label(root, text=basecode.cashback(money),bg='#626a77',fg='white', font=(None, 13) )
        cashbackLabel.place(x=40, y=600)
       # notesLabel = Label(root, fg='red4',bg='light blue',text=basecode.number_of_notes(), font=(None, 15))
       # notesLabel.place(x = 600,y = 320 )

    BG = ImageTk.PhotoImage(Image.open("productcase.png"))
    bgimage = Label(root, image=BG, bg='light blue')
    bgimage.place(x=0, y=5)



    Lays = ImageTk.PhotoImage(Image.open("smalllays.png"))
    Cheetos = ImageTk.PhotoImage(Image.open("smallcheetos.png"))
    Pringles = ImageTk.PhotoImage(Image.open("smallpringles.png"))
    Coke = ImageTk.PhotoImage(Image.open("smalldietcoke.png"))
    Pepsi = ImageTk.PhotoImage(Image.open("smallpepsi.png"))
    Fanta = ImageTk.PhotoImage(Image.open("smalldfanta.png"))
    PotatoChips = ImageTk.PhotoImage(Image.open("smallpotato.png"))
    Water = ImageTk.PhotoImage(Image.open("smallwater.png"))
    Dietcoke = ImageTk.PhotoImage(Image.open("smalldietcoke.png"))
    Snickers = ImageTk.PhotoImage(Image.open("snickers.png"))



    WaterButton = Button(root, image=Water, text='10/= ',bg= "white", font=(None, 10), compound=TOP, command=lambda: item_and_price(8)).place(x=40,y=328)
    PringlesButton = Button(root, image=Pringles, text='110/= ',bg= "white", font=(None, 10), compound=TOP, command=lambda: item_and_price(3)).place(x=150,y=328)
    SnickersButton = Button(root, image=Snickers, text='35/= ',bg= "white", font=(None, 10), compound=TOP, command=lambda: item_and_price(9)).place(x=260,y=328)


    amount = Label(root,text = 'Enter Amount:' ,bg='#626a77',fg='white',font=(None, 9)).place(x=413,y =250)
    Payment_entry = Entry(root,width=10,)
    Payment_entry.place(x=420,y =280)
    pay_button= Button(root,text = "Pay",font=(None,10),bg="black",fg='white',width = 8, command =lambda :cashbackLabel(int(Payment_entry.get())))
    pay_button.place(x=420, y=320)


    root.mainloop()
