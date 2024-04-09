import streamlit as st
import pickle
import numpy as np
import streamlit as st

# Set page title
st.title("ML Disease Model")

# List of symptoms (replace with your 132 symptoms)
symptoms = [
    "Symptom 1", "Symptom 2", "Symptom 3",  # Add all 132 symptoms here
]

# Dictionary to store checkbox values
checkbox_values = {}

# Display symptom checkboxes
for symptom in symptoms:
    checkbox_values[symptom] = st.number_input(f"{symptom}:", min_value=0, max_value=1, value=0, step=1, key=symptom)

# Save button for symptoms
if st.button("Save Symptoms"):
    selected_symptoms = [symptom for symptom, value in checkbox_values.items() if value == 1]
    selected_symptoms.sort()
    symptoms_output = ", ".join(selected_symptoms)
    st.text_area("Selected Symptoms:", value=symptoms_output, height=100)

# Text box for additional input
additional_input = st.text_input("Additional Input:")

# Predict button for additional input
if st.button("Predict"):
    st.write("Predicting with additional input:", additional_input)
    # You can add your prediction logic here based on the additional input
