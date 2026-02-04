class Customer:
    # Klassen säkerställer att kunddata alltid är giltig
    def __init__(self, id, name, email):
        self.id = id
        self.set_name(name)
        self.set_email(email)

    def get_customer_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        if not name or len(name) < 3:
            raise ValueError("Namnet måste vara minst 3 tecken")
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        if email.count("@") != 1 or "." not in email:
            raise ValueError("Ogiltig email")
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"
