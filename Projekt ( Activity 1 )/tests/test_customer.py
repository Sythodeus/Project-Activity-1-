import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    # VARFÖR: Namn måste vara minst 3 tecken
    # EXEMPEL: För korta namn är inte realistiska
    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Customer(1, "Al", "al@test.se")

    # VARFÖR: Email måste innehålla exakt ett @
    # EXEMPEL: Felaktiga mejladresser går inte att kontakta
    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            Customer(1, "Anna", "annatest.se")

    # VARFÖR: Strängrepresentation ska fungera
    # EXEMPEL: Visas i gränssnitt/loggar
    def test_str(self):
        c = Customer(1, "Anna", "anna@test.se")
        self.assertIn("Anna", str(c))

    # (lägg till fler tester → minst 8 totalt)
