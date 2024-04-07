import streamlit as st
import pickle
import numpy as np

# Set page title
st.title("ML Disease Model")

# List of symptoms (replace with your 132 symptoms)
symptoms = [
    "Itching","Skin Rash","Nodal Skin Eruptions",  # Add all 132 symptoms here
]

# Dictionary to store checkbox values
checkbox_values = {}

# Display symptom checkboxes
for symptom in symptoms:
    checkbox_values[symptom] = st.number_input(f"{symptom}:", min_value=0, max_value=1, value=0, step=1, key=symptom)

# Save button
if st.button("Save"):
    selected_symptoms = [symptom for symptom, value in checkbox_values.items() if value == 1]
    selected_symptoms.sort()
    output_string = ", ".join(selected_symptoms)
    st.text_area("Selected Symptoms:", value=output_string, height=100)

# Load the trained models
@st.cache
def load_models():
    svm_model = pickle.load(open("final_svm.sav", "rb"))
    #rf_model = pickle.load(open("final_rf.sav", "rb"))
    nb_model = pickle.load(open("final_nb.sav", "rb"))
    return svm_model, nb_model

svm_model, nb_model = load_models()

# Function to predict disease based on selected symptoms
def predict_disease(symptoms):
    input_data = np.array([int(symptom in symptoms) for symptom in symptoms]).reshape(1, -1)
    svm_pred = svm_model.predict(input_data)[0]
    #rf_pred = rf_model.predict(input_data)[0]
    nb_pred = nb_model.predict(input_data)[0]
    return svm_pred, nb_pred

# Example usage of predict_disease function
# svm_pred, nb_pred = predict_disease(selected_symptoms)
