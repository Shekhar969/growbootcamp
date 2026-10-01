userId=1
userName="Shekhar Rawal@"
balance=2000
itemsPrachased=("iceCream","iceCream","apple","tshirt","pants","shoes")
itemsInStock = {
    "iceCream": 100,
    "apple": 300,
    "tshirt": 800,
    "books": 500,
    "shoes": 1200
}

def checkItemInStock():
    for item in itemsPrachased:
        if item in itemsInStock:
            print("Item is in stock",item)
        else:
            print("Item is not in stock","Remove this item",item)

def calcTotal():
    total = 0

    for item in itemsPrachased:
        if item in itemsInStock:
            total = total + itemsInStock[item]

    return total


def suffentbalance():
    if(calcTotal()<=balance):
        return True
    else:
        return False

calcTotal();
checkItemInStock();

isSuffent=suffentbalance()
print("Balance is Suffent:",isSuffent)