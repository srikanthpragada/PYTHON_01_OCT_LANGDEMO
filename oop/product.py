class Product:
    # Class attribute
    taxrate = 12

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
        return (self.price * Product.taxrate / 100) + self.price

    def purchase(self, qty):
        self.qoh += qty

    def sell(self, qty):
        if self.qoh >= qty:
            self.qoh -= qty
        else:
            raise ValueError("Insufficient Quantity On Hand!")

    @staticmethod
    def set_taxrate(taxrate):
        if taxrate < 1 or taxrate > 50:
            raise ValueError("Invalid Tax Rate")

        Product.taxrate = taxrate

    @classmethod
    def create_dummy(cls):
        return cls("Dummy")


# Testing
p1 = Product("MacBook Air", 70000)  # Create an object
print(p1.net_price())
Product.set_taxrate(10)
print(p1.net_price())

d = Product.create_dummy()
d.print_details()

print(d)  # Name:Price:Qoh
