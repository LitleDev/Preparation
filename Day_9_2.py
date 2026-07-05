# Open-Closed Principle
# incorrect way 

class Discount:
    def calculator(self, price , customer_type):
        if customer_type == "regular":
            return price*0.9
        elif customer_type == "gold":
            return price*0.85
        elif customer_type == "vvip":
            return price*0.8

# correct method by implementing inhertitance

class Price_discout:
    def calculate_price(self, price):
        return price

class Regular_discount(Price_discout):
    def calculate_price(self,price):
        return price*0.90

class Gold_discount(Price_discout):
    def calculate_price(self,price):
        return price*0.85

class Vvip_discount(Price_discout):
    def calculate_price(self,price):
        return price*0.80

def get_final_price(discount_type , price):
    return discount_type.calculate_price(price)

# Client code 
#1st invoke the class 
regular = Regular_discount()
gold = Gold_discount()
vvip = Vvip_discount()

print( get_final_price(regular , 1000))
print( get_final_price(gold , 1000))
print( get_final_price(vvip , 1000))
