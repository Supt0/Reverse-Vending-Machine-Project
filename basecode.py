from math import floor


items = ["Lays", "Cheetos", "Pringles", "Coca Cola", "Pepsi", "Fanta", "Potato Chips","Water","Snickers"]
price = [25,50,110,35,30,35,10,10,35]
notes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
changes = []

Lays = 0
Cheetos = 0
Pringles = 0
CocaCola = 0
Pepsi = 0
Fanta = 0
PotatoChips = 0
Water = 0
Snickers = 0
total_price = 0
total_amount = 0
cash_back = 0


def selected_item(item):
    if item == 1:
        global Lays
        Lays = Lays + 1

    if item==2:
        global Cheetos
        Cheetos +=1
    if items ==3:
        global Pringles
        Pringles += 1
    if items ==4:
        global CocaCola
        CocaCola += 1
    if items ==5:
        global Pepsi
        Pepsi += 1
    if items ==6:
        global Fanta
        Fanta += 1
    if items ==7:
        global PotatoChips
        PotatoChips += 1
    if items ==8:
        global Water
        Water += 1
    if  items == 9:
        global Snickers
        Snickers += 1


def update_price(item):
    global total_price
    total_price = total_price + price[item-1]
    return total_price/2


def number_of_items(item):
    itemlist = " "
    if item==1 and Lays>0:
        itemlist


def total_price_update():
    global total_price
    total_price =0


def cashback(amount):
    global total_amount
    global cash_back
    total_amount = total_amount + amount
    price = total_price/2
    if total_amount >= price:
        cash_back = amount - price
        total_price_update()
        return "You will receive "+str(cash_back)
    elif  total_amount < price:
        cash_back =  price - total_amount
        return "Please pay "+str(cash_back)+" Taka more."




def number_of_notes():
    global cash_back
    for note in range(len(notes)):
        changes.append(floor(cash_back / notes[note]))
        cash_back = cash_back % notes[note]

    numberofnotes = " "

    for i in range(len(changes)):
        if changes[i] != 0:
            numberofnotes = numberofnotes + "Notes of "+str(notes[i])+" = "+str(changes[i])+"\n\n"
    changes.clear()
    return numberofnotes
