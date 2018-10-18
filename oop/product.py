class Product:
    # Constructor
    def __init__(self, name, price=None):
        # Object attributes
        self.name = name
        self.price = price
        self.qoh = 0

    def print_details(self):
        print("Name  : ", self.name)
        print("Price : ", "Unknown" if self.price is None else self.price)
        print("QOH   : ", self.qoh)

    def net_price(self):
        return self.price * 1.12

    def purchase(self, qty):
        self.qoh += qty

    def sell(self, qty):
        if self.qoh >= qty:
            self.qoh -= qty
        else:
            raise ValueError("Insufficient Quantity On Hand!")


# Testing
p1 = Product("MacBook Air", 70000)  # Create an object
p1.purchase(10)
p1.sell(5)
p1.print_details()
print(p1.net_price())
