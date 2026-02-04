from src.product import Product

class Order:
    # Order hanterar relationen mellan kund och produkter
    def __init__(self, id, customer):
        self.id = id
        self.customer = customer
        self.products = {}

    def get_order_id(self):
        return self.id

    def get_customer(self):
        return self.customer

    def add_product(self, product, quantity):
        if not isinstance(product, Product) or quantity <= 0:
            raise ValueError("Ogiltig produkt eller kvantitet")
        self.products[product] = self.products.get(product, 0) + quantity

    def remove_product(self, product):
        if product not in self.products:
            raise ValueError("Produkten finns inte i ordern")
        del self.products[product]

    def get_total_quantity(self):
        return sum(self.products.values())

    def calculate_total(self):
        return sum(p.get_price() * q for p, q in self.products.items())

    def get_products(self):
        return self.products

    def __str__(self):
        return f"Order {self.id} - {self.customer}"
