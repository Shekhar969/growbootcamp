productCost=100

class weekly:
    def price(self):
        print("the price for the week is",100*7)

class monthly:
    def price(self):
        print("the price for the month",100*30)

WeeklyPrice=weekly()
MonthlyPrice=monthly()

WeeklyPrice.price()
MonthlyPrice.price()