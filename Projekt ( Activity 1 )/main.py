from src.product import Product
from src.customer import Customer
from src.order import Order

# Skapa produkter
coffee = Product(1, "Espressobönor", 129, 20)
mug = Product(2, "Keramikkopp", 79, 15)

# Skapa en kund
customer = Customer(1, "Sofia Lind", "sofia@coffee.se")

# Skapa order och lägg till produkter
order = Order(1, customer)
order.add_product(coffee, 2)
order.add_product(mug, 1)

# Skriv ut order och totalpris
print(order)
print("Totalt pris:", order.calculate_total(), "kr")
