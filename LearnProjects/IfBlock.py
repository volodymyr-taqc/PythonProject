#! Program
 
usd = 27
euro = 30
 
money = int(input("Enter sum: "))
currency = int(input("Enter maney code (dolars - 400, euro - 401): "))
 
if currency == 400:
    cash = round(money / usd, 2)
    print("Dolars")
elif currency == 401:
    cash = round(money / euro, 2)
    print("Euro")
else:
    cash = 0
    print("Error")
 
print("You will get:", cash)