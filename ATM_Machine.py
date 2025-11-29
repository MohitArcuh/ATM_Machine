# ATM Cash Withdrawal System
balance = 5000
pin = 1234

print("Insert your Card please")
user_pin = int(input("Enter your pin: "))


if user_pin == pin:
    amount = int(input("Enter the Amount: "))
    if amount <= balance:
        balance -= amount
        print("Debited: ", amount)
        print("Remaining: ", balance)
    else:
        print("Insufficient Money \nFirst Deposit then, come again")
else:
    print("Wrong pin Entered by you!")
