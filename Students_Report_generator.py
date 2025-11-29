import streamlit as st
import pandas as pd

st.title("📘 Student Report Generator")

# Input fields
st.header("Enter Student Details")

name = st.text_input("Student Name")
roll = st.text_input("Roll Number")
cls = st.selectbox("Class", ["6", "7", "8", "9", "10", "11", "12"])

st.header("Enter Marks")

subjects = ["Math", "Science", "English", "Hindi", "Computer"]
marks = {}

for subject in subjects:
    marks[subject] = st.number_input(f"{subject} Marks (out of 100)", min_value=0, max_value=100)

if st.button("Generate Report"):
    total = sum(marks.values())
    percentage = total / len(subjects)

    # Result
    st.subheader("📄 Generated Report")

    st.write(f"**Name:** {name}")
    st.write(f"**Roll Number:** {roll}")
    st.write(f"**Class:** {cls}")

    # Show marks table
    df = pd.DataFrame({"Subject": subjects, "Marks": list(marks.values())})
    st.table(df)

    st.write(f"**Total Marks:** {total} / {len(subjects) * 100}")
    st.write(f"**Percentage:** {percentage:.2f}%")

    # Grade System
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 45:
        grade = "C"
    else:
        grade = "D"

    st.write(f"**Grade:** {grade}")

    # Pass/Fail
    if percentage >= 35:
        st.success("Result: PASS")
    else:
        st.error("Result: FAIL")
