class BankAccount:
    def __init__(self, bank, name, balance):
        self.name = name
        self.bank = bank
        self.balance = float(balance)

    def __str__(self):
        return f"{self.name} -> {self.balance:.2f} ({self.bank})"


bank_accounts = []

while True:
    line = input()
    if "end" == line:
        break

    tokens = line.split(" | ")
    bank_accounts.append(BankAccount(*tokens))


def sort_accounts(array):
    return sorted(array, key=lambda account: (-account.balance, len(account.bank)))


print("\n".join(map(str, sort_accounts(bank_accounts))))
