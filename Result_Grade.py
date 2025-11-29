# Telling Grade of Students
name = input("Enter your Name: ")
marks_1 = int(input("Enter your English Marks: "))
marks_2 = int(input("Enter your Science Marks: "))
marks_3 = int(input("Enter your Social Science Marks: "))
marks_4 = int(input("Enter your Hindi Marks: "))
marks_5 = int(input("Enter your Maths Marks: "))

result = (float(marks_1 + marks_2 + marks_3 + marks_4 + marks_5) / 5)

if result >= 90:
    print("Grade A")
elif result >= 75:
    print("Grade B")
elif result >= 50:
    print("Grade C")
else:
    print("Fail")