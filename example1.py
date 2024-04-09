import streamlit as st
import pickle
import numpy as np
import streamlit as st

# Set page title
st.title("ML Disease Model")

# List of symptoms (replace with your 132 symptoms)
symptoms = [
    "Itching", "Skin Rash", "Nodal Skin Eruptions",  # Add all 132 symptoms here
]

# Load the SVM model
with open('svm_modelxx.sav', 'rb') as f:
    svm_model = pickle.load(f)

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

DiseasesXYZ = st.text_input('Number of Pregnancies')

# Predict button for stored input
if st.button("Predict from Stored Input"):
    # Split stored input into symptoms
    selected_symptoms = DiseasesXYZ.split(",")
    
    # Make prediction using the SVM model
    prediction = svm_model.predict([selected_symptoms])
    
    # Display the predicted disease
    st.text("Predicted Disease from Stored Input:")
    st.write(prediction[0])


#if st.button('Predict'):
 #       diabzxc = diabetes_model.predict([[DiseasesXYZ]])
        
       # if (diab_prediction[0] == 1):
        #  diab_diagnosis = 'The person is diabetic'
        # else:
         # diab_diagnosis = 'The person is not diabetic'
        
    #st.success(diab_diagnosis)

#print(diabzxc)
print('diabzxc')
print("diabzxc")
