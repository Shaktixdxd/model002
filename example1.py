import streamlit as st

# Set page title
st.title("ML Disease Model")

# List of diseases (replace with your 132 diseases)
diseases = [
    "Disease 1", "Disease 2", "Disease 3",  # Add all 132 diseases here
]

# Dictionary to store checkbox values
checkbox_values = {disease: False for disease in diseases}

# Display checkboxes for each disease
for disease in diseases:
    checkbox_values[disease] = st.checkbox(disease)

# Reset button to clear all checkboxes
if st.button("Reset"):
    checkbox_values = {disease: False for disease in diseases}

# Button to save selections
if st.button("Predict"):
    # Perform prediction or save selections here
    st.write("Selections saved!")

# You can add any additional content or functionality here
