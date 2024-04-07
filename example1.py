import streamlit as st

# Set page title
st.title("ML Disease Model")

# List of diseases (replace with your 132 diseases)
diseases = [
    "Disease 1", "Disease 2", "Disease 3",  # Add all 132 diseases here
]

# Dictionary to store disease values
disease_values = {disease: 0 for disease in diseases}

# Display disease checkboxes
for disease in diseases:
    disease_values[disease] = st.number_input(f"{disease}:", min_value=0, max_value=1, value=0, step=1)

# Save button
if st.button("Save"):
    selected_diseases = [disease for disease, value in disease_values.items() if value == 1]
    selected_diseases.sort()  # Sort diseases alphabetically
    selected_diseases_string = ", ".join(selected_diseases)
    st.text_area("Selected Diseases:", value=selected_diseases_string, height=100)

# Convert selected diseases to a string
selected_diseases_string = ", ".join(selected_diseases)
st.write("Output String:", selected_diseases_string)
