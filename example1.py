
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
User = DiseasesXYZ

import streamlit as st
import pandas as pd
from sklearn.svm import SVC
import numpy as np
import pickle

# Load the label-encoded dataset
data = pd.read_csv('encoded_data.csv')

# Load the trained SVM model
with open("svm_model.pkl", "rb") as f:
    svm_model = pickle.load(f)

# Define a function to preprocess input symptoms and make predictions
def predict_disease(symptoms):
    # Preprocess the input symptoms (you may need to adapt this based on your data)
    input_data = pd.DataFrame(columns=data.columns[:-1])
    input_data.loc[0] = 0  # Initialize all values to 0
    for symptom in symptoms.split(","):
        input_data[symptom.strip()] = 1  # Set the value to 1 for each symptom present

    # Make predictions using the loaded model
    prediction = svm_model.predict(input_data)
    predicted_disease = label_encoder.inverse_transform(prediction)[0]  # Decode the predicted disease
    return predicted_disease

# Streamlit web app
st.title("Disease Prediction")

# Input text box for symptoms
symptoms_input = st.text_input("Enter symptoms separated by commas")

# Button to make prediction
if st.button("Predict"):
    if symptoms_input:
        predicted_disease = predict_disease(symptoms_input)
        st.success(f"The predicted disease is: {predicted_disease}")
    else:
        st.warning("Please enter symptoms to predict the disease")


# Predict button for stored input
if st.button("Predict from Stored Input"):
    # Split stored input into symptoms
    selected_symptoms = DiseasesXYZ.split(",")
    
    # Make prediction using the SVM model
    #prediction = svm_model.predict([selected_symptoms])
    
    # Display the predicted disease
    st.text("Predicted Disease from Stored Input:")
    st.write(predict_disease(User))
    #st.write(svm_model.predict(Itching,Skin Rash,Nodal Skin Eruptions))
    st.write(svm_model.predict("Itching,Skin Rash,Nodal Skin Eruptions"))
    st.write(predict_disease("Itching,Skin Rash,Nodal Skin Eruptions"))
    st.write("1")
    #st.write(Hello)
    st.write("2")
    st.write("Hello2")
    st.write("3")
    st.write(DiseasesXYZ)
    st.write("4")
    st.write("DiseasesXYZ")
    st.write("5")
    st.write(User)
    st.write("6")
    st.write("User")
    st.write("7")
    st.write(predict_Disease("DiseasesXYZ"))
    st.write("8")
    st.write(predict_Disease(DiseasesXYZ))
    st.write("9")
    st.write(predict_Disease("Itching,Skin Rash,Nodal Skin Eruptions"))

if st.button("Predict"):
    st.write("You clicked the predict button!")


    #st.success(diab_diagnosis)


