from math import floor


item_list = {"Lays": 25,
             "Cheetos": 50,
             "Pringles": 110,
             "Coca Cola": 35,
             "Pepsi": 30,
             "Fanta": 35,
             "Potato Chips": 10}
print(".........WELCOME........")
print("What do you want to buy??? ")
print("Please select your option.")

i = 1
for item in item_list:
    print("For ", item, " press: ", i)
    i += 1

print('\n')

while True:
    selected_item = int(input("Please Select: "))
    if 1 <= selected_item <= 7:
        if selected_item == 1:
            Choice = "Lays"
            break
        if selected_item == 2:
            Choice = "Cheetos"
            break
        if selected_item == 3:
            Choice = "Pringles"
            break
        if selected_item == 4:
            Choice = "Coca Cola"
            break
        if selected_item == 5:
            Choice = "Pepsi"
            break
        if selected_item == 6:
            Choice = "Fanta"
            break
        if selected_item == 7:
            Choice = "Potato Chips"
            break
    else:
        print("Wrong choice ")

print("Please play ", item_list.get(Choice), " Taka...: ", end=" ")
paid = int(input())
print("You have paid ", paid, " Taka")

while paid < item_list.get(Choice):
    print("Sorry... Insufficient Payment....")
    left_to_pay = item_list.get(Choice) - paid
    print("Please pay ", left_to_pay, " Taka more: ", end=" ")
    more = int(input())
    paid = paid + more

if paid >= item_list.get(Choice):
    notes_of_1000 = 0
    notes_of_500 = 0
    notes_of_100 = 0
    notes_of_50 = 0
    notes_of_20 = 0
    notes_of_10 = 0
    notes_of_5 = 0
    notes_of_2 = 0
    notes_of_1 = 0
    cash_back = paid - item_list.get(Choice)

    print("\n\nYou have purchased ", Choice, " with ", item_list.get(Choice), " Taka")
    print("In return you will receive ", cash_back, " Taka")

    notes = 0
    print("\n")
    if cash_back > 0:
        if cash_back >= 1000:
            notes = cash_back / 1000
            cash_back = cash_back - 1000 * floor(notes)
            notes_of_1000 = floor(notes)
        if 1000 > cash_back >= 500:
            notes = cash_back / 500
            cash_back = cash_back - 500 * floor(notes)
            notes_of_500 = floor(notes)
        if 500 > cash_back >= 100:
            notes = cash_back / 100
            cash_back = cash_back - 100 * floor(notes)
            notes_of_100 = floor(notes)
        if 100 > cash_back >= 50:
            notes = cash_back / 50
            cash_back = cash_back - 50 * floor(notes)
            notes_of_50 = floor(notes)
        if 50 > cash_back >= 20:
            notes = cash_back / 20
            cash_back = cash_back - 20 * floor(notes)
            notes_of_20 = floor(notes)
        if 20 > cash_back >= 10:
            notes = cash_back / 10
            cash_back = cash_back - 10 * floor(notes)
            notes_of_10 = floor(notes)
        if 10 > cash_back >= 5:
            notes = cash_back / 5
            cash_back = cash_back - 5 * floor(notes)
            notes_of_5 = floor(notes)
        if 5 > cash_back >= 2:
            notes = cash_back / 2
            cash_back = cash_back - 2 * floor(notes)
            notes_of_2 = floor(notes)
        if 2 > cash_back >= 1:
            notes = cash_back / 1
            cash_back = cash_back - 1 * floor(notes)
            notes_of_1 = floor(notes)

    print("Changes will be: ")
    print("Note of 1000: ", notes_of_1000, "\nNote of 500: ", notes_of_500, "\nNote of 100: ", notes_of_100,
          "\nNote of 50: ", notes_of_50,
          "\nNote of 20: ", notes_of_20, "\nNote of 10: ", notes_of_10, "\nNote of 5: ", notes_of_5,
          "\nNote of 2: ",
          notes_of_2,
          "\nNote of 1: ", notes_of_1)
