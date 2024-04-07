import pickle
import streamlit as st

svm_model = pickle.load(open('final_svm.sav', 'rb'))
nb_model = pickle.load(open('final_nb.sav', 'rb'))
rf_model = pickle.load(open('final_rf.sav', 'rb'))

import streamlit as st

# Set page title
st.title("ML Disease Model")

# List of diseases (replace with your 132 diseases)
diseases = [
    "Disease 1", "Disease 2", "Disease 3",  # Add all 132 diseases here
]

# Create dictionary to store checkbox values
checkbox_values = {}

# Display disease checkboxes
for disease in diseases:
    st.write(disease)
    checkbox_values[disease] = st.number_input(f"Enter 0 or 1 for {disease}", min_value=0, max_value=1, value=0, step=1, key=disease)

# Save button
if st.button("Save"):
    # Filter diseases with checkbox value of 1
    selected_diseases = [disease for disease, value in checkbox_values.items() if value == 1]
    # Sort selected diseases alphabetically
    selected_diseases.sort()
    # Display selected diseases as string in alphabetical order
    selected_diseases_str = ", ".join(selected_diseases)
    st.text_area("Selected Diseases:", value=selected_diseases_str, height=100)

    # Save selected diseases as string in code
    selected_diseases_code = f'selected_diseases = "{selected_diseases_str}"'
    st.text_area("Selected Diseases Code:", value=selected_diseases_code, height=100)
