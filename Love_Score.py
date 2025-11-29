# Write a Program to find the love of your love and you via getting input from the user.

name1 = input("Enter your Name: ")
name2 = input("Enter your Lover Name: ")
combine_string = name1 + name2
lower_case_string = combine_string.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')
true = t + r + u + e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')
love = l + o + v + e

love_score = int(str(true) + str(love))
if love_score <= 10 or love_score >= 90:
    print(f"Your love score is {love_score} and you will go like coke & mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score} and you will go alright together.")
else:
    print(f"Your love score is {love_score}.")

# Write a Program to print heads and tails.

import random

side = random.randint(0, 1)
if side == 1:
    print("Heads")
else:
    print("Tails")