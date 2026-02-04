import unittest
from src.product import Product

class TestProduct(unittest.TestCase):

    # VARFÖR DETTA TEST BEHÖVS: Säkerställer att produkt-ID lagras korrekt
    # EXEMPEL FRÅN VERKLIGHETEN: Varje vara i en butik har ett unikt ID
    def test_get_product_id(self):
        p = Product(1, "Kaffe", 50, 10)
        self.assertEqual(p.get_product_id(), 1)

    # VARFÖR: Namn får inte vara tomt
    # EXEMPEL: En produkt utan namn kan inte säljas
    def test_set_name_invalid(self):
        p = Product(1, "Kaffe", 50, 10)
        with self.assertRaises(ValueError):
            p.set_name(" ")

    # VARFÖR: Priset måste vara > 0
    # EXEMPEL: Gratis produkter förstör intäktsberäkning
    def test_set_price_invalid(self):
        p = Product(1, "Kaffe", 50, 10)
        with self.assertRaises(ValueError):
            p.set_price(0)

    # VARFÖR: Lager kan inte fyllas på med negativa värden
    # EXEMPEL: Man kan inte ta emot -5 varor
    def test_add_stock_invalid(self):
        p = Product(1, "Kaffe", 50, 10)
        with self.assertRaises(ValueError):
            p.add_stock(-1)

    # VARFÖR: Man kan inte ta bort fler produkter än finns
    # EXEMPEL: Man kan inte sälja slut på något som inte finns
    def test_remove_stock_too_much(self):
        p = Product(1, "Kaffe", 50, 5)
        with self.assertRaises(ValueError):
            p.remove_stock(10)

    # VARFÖR: Kontroll av lagervärde
    # EXEMPEL: Butiker behöver veta värdet på sitt lager
    def test_calculate_total_value(self):
        p = Product(1, "Kaffe", 50, 2)
        self.assertEqual(p.calculate_total_value(), 100)

    # (lägg till fler tester → minst 12 totalt)
