import streamlit as st

# Set page title
st.title("ML Disease Model")

# List of diseases (replace with your 132 diseases)
diseases = [
    "Disease 1", "Disease 2", "Disease 3",  # Add all 132 diseases here
]

# Display disease checkboxes
for disease in diseases:
    st.checkbox(disease)

# Reset button to clear all checkboxes
if st.button("Reset"):
    st.session_state.checked_boxes = {}

# Predict button
if st.button("Predict"):
    checked_diseases = [disease for disease in diseases if st.session_state.get(disease)]
    st.write("Selected diseases:", checked_diseases)
