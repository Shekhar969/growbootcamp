userId = 1

userName = "Shekhar Rawal@!"

balance = 2000

itemsPrachased = (
    "iceCream",
    "iceCream",
    "apple",
    "tshirt",
    "pants",
    "shoes"
)

itemsInStock = {
    "iceCream": 100,
    "apple": 300,
    "tshirt": 800,
    "books": 500,
    "shoes": 1200
}


def checkItemInStock():
    available_items = []

    for item in itemsPrachased:
        if item in itemsInStock:
            available_items.append(item)

    return available_items



def calcTotal():
    total = 0

    for item in itemsPrachased:
        if item in itemsInStock:
            total = total + itemsInStock[item]

    return total


def suffentbalance():
    return calcTotal() <= balance
