class Product:
    # Klassen är skriven för att kapsla in all logik kring en produkt
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.set_name(name)
        self.set_price(price)
        self.quantity = quantity

    def get_product_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        if not name.strip():
            raise ValueError("Namn får inte vara tomt")
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        if price <= 0:
            raise ValueError("Pris måste vara större än 0")
        self.price = price

    def get_quantity(self):
        return self.quantity

    def add_stock(self, amount):
        if amount <= 0:
            raise ValueError("Amount måste vara > 0")
        self.quantity += amount

    def remove_stock(self, amount):
        if amount <= 0 or amount > self.quantity:
            raise ValueError("Ogiltigt antal")
        self.quantity -= amount

    def calculate_total_value(self):
        return self.price * self.quantity

    def is_in_stock(self):
        return self.quantity > 0

    def __str__(self):
        return f"{self.name} ({self.quantity} st)"
