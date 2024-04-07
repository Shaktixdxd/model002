import streamlit as st

# Set page title
st.title("ML Disease Model")

# List of diseases (replace with your 132 diseases)
diseases = [
    "Disease 1", "Disease 2", "Disease 3",  # Add all 132 diseases here
]

# Display disease checkboxes
for disease in diseases:
    checkbox_value = st.checkbox(disease)

# You can add any additional content or functionality here
