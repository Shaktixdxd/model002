import streamlit as st

# Set page title
st.title("ML Disease Model")

# List of diseases (replace with your 132 diseases)
diseases = [
    "Disease 1", "Disease 2", "Disease 3",  # Add all 132 diseases here
]

# Dictionary to store disease selections
disease_selections = {disease: 0 for disease in diseases}

# Display disease checkboxes and buttons
for disease in diseases:
    disease_selections[disease] = st.number_input(f"{disease}", min_value=0, max_value=1, value=0, step=1, format="%d")

# Save button to display selected diseases
if st.button("Save"):
    selected_diseases = [disease for disease, value in disease_selections.items() if value == 1]
    selected_diseases.sort()  # Sort diseases alphabetically
    selected_diseases_str = ", ".join(selected_diseases)
    st.text_area("Selected Diseases:", value=selected_diseases_str, height=100)

    # Save selected diseases as a string
    selected_diseases_code = ", ".join([f'"{disease}"' for disease in selected_diseases])
    st.text_area("Selected Diseases (Code):", value=selected_diseases_code, height=100)

# Predict button
if st.button("Predict"):
    # Placeholder for prediction code (not implemented in this example)
    st.write("Prediction functionality will be implemented here.")
