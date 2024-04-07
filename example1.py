import pickle
import streamlit as st

svm_model = pickle.load(open('final_svm.sav', 'rb'))
nb_model = pickle.load(open('final_nb.sav', 'rb'))
#rf_model = pickle.load(open('final_rf.sav', 'rb'))

# Set page title
st.title("ML Disease Model")

# List of diseases (replace with your 132 diseases)
diseases = [
    "Disease 1", "Disease 2", "Disease 3",  # Add all 132 diseases here
]

# Dictionary to store checkbox values
checkbox_values = {}

# Display disease checkboxes
for disease in diseases:
    checkbox_values[disease] = st.number_input(f"{disease}:", min_value=0, max_value=1, value=0, step=1, key=disease)

# Save button
if st.button("Save"):
    selected_diseases = [disease for disease, value in checkbox_values.items() if value == 1]
    selected_diseases.sort()
    output_string = ", ".join(selected_diseases)
    st.text_area("Selected Diseases:", value=output_string, height=100)


if st.button("Diabetes Test Result"):
    result = svm_model.predict("Itching,Skin Rash,Nodal Skin Eruptions")
    st.text_area("Selected xxxxxs:", value=result, height=100)
    
st.success(result)
