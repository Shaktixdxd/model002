
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

symptoms = X.columns.values

# Creating a symptom index dictionary to encode the
# input symptoms into numerical form
symptom_index = {}
for index, value in enumerate(symptoms):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_index[symptom] = index

data_dict = {
    "symptom_index": symptom_index,
    "predictions_classes": encoder.classes_
}

def predict_disease(symptoms):
    symptoms = symptoms.split(",")
    
    # Create input data for the model
    input_data = [0] * len(symptoms)
    for symptom in symptoms:
        if symptom.strip() in data_dict["symptom_index"]:
            index = data_dict["symptom_index"][symptom.strip()]
            input_data[index] = 1
        else:
            st.error(f"Invalid symptom: {symptom.strip()}")
            return None
    
    # Reshape the input data and make prediction
    input_data = np.array(input_data).reshape(1, -1)
    prediction = svm_model.predict(input_data)[0]
    disease = encoder.classes_[prediction]
    return disease

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


