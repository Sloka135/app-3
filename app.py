import streamlit as st

# App title
st.title("Welcome to Streamlit")

# Text input
name = st.text_input("Enter your name")

# Display greeting if name is entered
if name:
    st.success(f"Hello {name}")

# Age slider
age = st.slider("Select your age", 1, 100)

# Show selected age
st.write("Age:", age)

# Button with balloons
if st.button("Celebrate"):
    st.balloons()