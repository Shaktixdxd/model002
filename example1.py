import streamlit as st

# Set page title
st.title("ML Disease Model")

# List of diseases (replace with your 132 diseases)
diseases = [
    "Disease 1", "Disease 2", "Disease 3",  # Add all 132 diseases here
]

# Dictionary to store checkbox values
checkbox_values = {}

# Display disease checkboxes and buttons
for disease in diseases:
    checkbox_values[disease] = st.number_input(f"Enter 0 or 1 for {disease}", min_value=0, max_value=1, value=0, step=1, key=disease)

# Buttons to set checkbox values
for disease, value in checkbox_values.items():
    if st.button(f"Set {disease} to 0"):
        checkbox_values[disease] = 0
    if st.button(f"Set {disease} to 1"):
        checkbox_values[disease] = 1

# Save button to display selected diseases
if st.button("Save"):
    selected_diseases = [disease for disease, value in checkbox_values.items() if value == 1]
    selected_diseases_text = ", ".join(selected_diseases)
    st.write("Selected Diseases:", selected_diseases_text)
