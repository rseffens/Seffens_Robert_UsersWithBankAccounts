from bank import User, BankAccount

robert = User("Robert", "Seffens", "rs@dojo.com")
jennifer = User("Jennifer", "Anniston", "ja@dojo.com")

# robert = BankAccount(.10, 50)
# robert.deposit(100).deposit(200).deposit(50).withdrawl(60).yield_interest().display_account_info()

# veronica = BankAccount(.10, 500)
# veronica.deposit(1500).deposit(5000).withdrawl(800).withdrawl(500).withdrawl(100).withdrawl(50).yield_interest().display_account_info()

robert.deposit(100).withdrawl(50).display_account_info()
jennifer.deposit(5000).withdrawl(1000).display_account_info()