# Movie Ticket Calculator

print("=== Welcome to INOX ===")
print("Check the list of Movie")
print("\n 1. Jailer 2 \n 2. Kaantha \n 3. Game Changer \n 4. Vrusshabha \n 5. The Fantastic Four: First Steps")

movie = int(input("Enter your Movie Number: "))
ticket = 0

if movie == 1:
    ticket = 300
    print("You want to watch Jailer 2 \nThe ticket price is Rs 300.")
elif movie == 2:
    ticket = 300
    print("You want to watch Kaantha \nThe ticket price is Rs 300.")
elif movie == 3:
    ticket = 200
    print("You want to watch Game Changer \nThe ticket price is Rs 200.")
elif movie == 4:
    ticket = 250
    print("You want to watch Vrusshabha \nThe ticket price is Rs 250.")
elif movie == 5:
    ticket = 400
    print("You want to watch The Fantastic Four: First Steps \nThe ticket price is Rs 400.")

quantity = int(input("Enter Number of Tickets : "))
price = quantity * ticket
print(f"You have to pay: {price}")