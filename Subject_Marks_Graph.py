import matplotlib.pyplot as plt
import pyttsx3
import speech_recognition
subjects = ["M1", "M2", "Chem", "Physics"]
marks = ["15", "10", "11", "16"]

plt.bar(subjects, marks)
plt.title("Subjects V/s Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)
plt.savefig("My Matplotlib.png")
plt.show()



