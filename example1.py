
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

--------------------------------------------------------------------------
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Reading the train.csv by removing the 
# last column since it's an empty column
data = pd.read_csv('Training.csv').dropna(axis=1)

# Encoding the target value into numerical
# value using LabelEncoder
encoder = LabelEncoder()
data["prognosis"] = encoder.fit_transform(data["prognosis"])

# Splitting data into features and target
X = data.drop(columns=["prognosis"])
y = data["prognosis"]

# Creating a symptom index dictionary to encode the
# input symptoms into numerical form
symptom_index = {}
for index, value in enumerate(X.columns):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_index[symptom] = index

# Training the SVM model
svm_model = SVC()
svm_model.fit(X, y)

# Input symptoms from the user
input_symptoms = input("Enter the symptoms separated by commas: ")

# Preprocess the input symptoms and make predictions
input_data = [0] * len(symptom_index)
for symptom in input_symptoms.split(","):
    index = symptom_index.get(symptom.strip().capitalize())
    if index is not None:
        input_data[index] = 1

# Reshape the input data and make predictions
input_data = np.array(input_data).reshape(1, -1)
predicted_disease = encoder.inverse_transform(svm_model.predict(input_data))[0]

# Print the predicted disease
print("Predicted Disease:", predicted_disease)



--------------------------------------------------------------------------

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

MODEL = pickle.load(open('svm_modelDDDD', 'rb'))

# Predict button for stored input
if st.button("Predict from Stored Input"):
   
    # Display the predicted disease
    st.text("Predicted Disease from Stored Input:")
    #st.write(predict_disease(User))
    #st.write(svm_model.predict(Itching,Skin Rash,Nodal Skin Eruptions))
    st.write(MODEL.predict("Itching,Skin Rash,Nodal Skin Eruptions"))
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


