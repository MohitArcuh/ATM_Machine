import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("📊 Simple Streamlit Dashboard")

# Sidebar
st.sidebar.header("User Input")
option = st.sidebar.selectbox("Select a Chart Type:", ["Line Chart", "Bar Chart", "Area Chart"])

# Create random data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.subheader("Sample Data")
st.write(data)

# Plot based on user selection
st.subheader(f"{option}")
if option == "Line Chart":
    st.line_chart(data)
elif option == "Bar Chart":
    st.bar_chart(data)
else:
    st.area_chart(data)

# Matplotlib example
st.subheader("Matplotlib Example Plot")
fig, ax = plt.subplots()
ax.plot(data['A'], data['B'], 'o-')
ax.set_title("A vs B Plot")
st.pyplot(fig)

# Footer
st.markdown("Created with ❤️ using Streamlit")
