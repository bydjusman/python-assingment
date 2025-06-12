class Bank:
    bank_name = "Default Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name: {Bank.bank_name}")

b1 = Bank("Usman")
b2 = Bank("Ali")

b1.show_details()
b2.show_details()

Bank.change_bank_name("Meezan Bank | The Premier Islamic Bank")
b1.show_details()
b2.show_details()
