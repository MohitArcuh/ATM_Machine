# Write a Program to find the prices of Pizza via getting inputs from the user.
size = input("Enter Size of Pizza as S, M, L : ")
bill = 0

if size == 'S' or size == 's':
    bill = 100
    print("Small Pizza Price is Rs 100")
elif size == 'M' or size == 'm':
    bill = 250
    print("Medium Pizza Price is Rs 250")
else:
    bill = 400
    print("Large Pizza Price is Rs 400")

add_pepperoni = input("Do you want to add pepperoni? Y/N :")
if add_pepperoni == 'Y' or add_pepperoni == 'y':
    if size == 'S' or size == 's':
        bill = bill + 30
    else:
        bill = bill + 50
else:
    bill = bill

extra_cheese = input("Do you want extra cheese? Y/N : ")
if extra_cheese == 'Y' or extra_cheese == 'y':
    if size == 'S' or size == 's':
        bill = bill + 20
    else:
        bill = bill + 50
else:
    bill = bill

print(f"Your final bill is Rs {bill}.")