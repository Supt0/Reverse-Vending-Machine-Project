from tkinter import *
from PIL import ImageTk, Image
from FInal_Project import Alternate



def VendingMachine():
    root = Tk()
    root.title("Vending Machine")
    root.geometry("870x600")
    root.configure(background='light blue')
    root.iconbitmap('icon.ico')

    # To call multiple function
    def item_and_price(item):
        Alternate.selected_item(item)
        Alternate.update_price(item)
        Pay_Label = Label(root, text="Please pay: "+ str(Alternate.update_price(item))+" Taka",bg='light blue',fg='red4', font=(None, 13) ).place(x=15, y=320)



    def cashbackLabel(money):
        cashbackLabel = Label(root, text=Alternate.cashback(money), font=(None, 13))
        cashbackLabel.place(x=15, y=430)
        notesLabel = Label(root, fg='red4',bg='light blue',text=Alternate.number_of_notes(), font=(None, 15))
        notesLabel.place(x = 500,y = 320 )






    Lays = ImageTk.PhotoImage(Image.open("lays.png"))
    Cheetos = ImageTk.PhotoImage(Image.open("cheetos.png"))
    Pringles = ImageTk.PhotoImage(Image.open("pringles.png"))
    Coke = ImageTk.PhotoImage(Image.open("dietcoke.png"))
    Pepsi = ImageTk.PhotoImage(Image.open("pepsi.png"))
    Fanta = ImageTk.PhotoImage(Image.open("dfanta.png"))
    PotatoChips = ImageTk.PhotoImage(Image.open("potato.png"))
    Water = ImageTk.PhotoImage(Image.open("water.png"))
    Dietcoke = ImageTk.PhotoImage(Image.open("dietcoke.png"))

    LaysButton = Button(root, text='25/= ', image=Lays, font=(None, 15), bg= "white",compound=RIGHT, command=lambda: item_and_price(1)).grid(row=0, column=0, padx=10, pady=10)
    FantaButton = Button(root, image=Fanta, text='35/= ', bg= "white",font=(None, 15), compound=RIGHT, command=lambda: item_and_price(6)).grid(row=0, column=1, padx=10, pady=10)
    PotatoButton = Button(root, image=PotatoChips, text='10/= ',bg= "white", font=(None, 15), compound=RIGHT, command=lambda: item_and_price(7)).grid(row=0, column=2, padx=10, pady=10)
    DietcokeButton = Button(root, image=Dietcoke, text='35/= ', bg= "white",font=(None, 15), compound=RIGHT, command=lambda: item_and_price(4)).grid(row=0, column=3, padx=10, pady=10)
    WaterButton = Button(root, image=Water, text='10/= ',bg= "white", font=(None, 15), compound=RIGHT, command=lambda: item_and_price(8)).grid(row=1, column=0, padx=10, pady=10)
    PepsiButton = Button(root, image=Pepsi,text='30/= ', bg= "white",font=(None, 15), compound=RIGHT, command=lambda: item_and_price(5)).grid(row=1, column=1, padx=10, pady=10)
    PringlesButton = Button(root, image=Pringles, text='110/= ',bg= "white", font=(None, 15), compound=RIGHT, command=lambda: item_and_price(3)).grid(row=1, column=2, padx=10, pady=10)
    CheetosButton = Button(root, image=Cheetos,text='50/= ', bg= "white",font=(None, 15), compound=RIGHT, command=lambda: item_and_price(2)).grid(row=1, column=3, padx=10, pady=10)



    amount = Label(root,text = "Enter Amount: " ,bg='light blue',font=(None, 15)).place(x=15,y =370)
    Payment_entry = Entry(root)
    Payment_entry.place(x=200,y =377)
    pay_button= Button(root,text = "Pay",font=(None,10),bg="black",fg='white',width = 8, command =lambda :cashbackLabel(int(Payment_entry.get()))).place(x=400, y=373)



    root.mainloop()
