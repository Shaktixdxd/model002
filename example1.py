
import streamlit as st
import pickle
import numpy as np
import streamlit as st


#------------------------
# Set page title
st.title("ML Disease Model")

# List of symptoms (replace with your 132 symptoms)
symptoms = [
    "Itching", "Skin Rash", "Nodal Skin Eruptions",  # Add all 132 symptoms here
]

#--------------------------------------------------------------------------
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC

# Load the dataset
@st.cache
def load_data():
    data = pd.read_csv('Training.csv').dropna(axis=1)
    return data

data = load_data()

# Encode the target values
encoder = LabelEncoder()
data["prognosis"] = encoder.fit_transform(data["prognosis"])

# Split data into features and target
X = data.drop(columns=["prognosis"])
y = data["prognosis"]

# Create a symptom index dictionary
symptom_index = {}
for index, value in enumerate(X.columns):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_index[symptom] = index

# Train the SVM model
svm_model = SVC()
svm_model.fit(X, y)

# Streamlit app
st.title("Disease Prediction")

# Input text box for symptoms
symptoms_input = st.text_input("Enter symptoms separated by commas")

# Button to make prediction
if st.button("Predict"):
    if symptoms_input:
        # Preprocess the input symptoms
        input_data = [0] * len(symptom_index)
        for symptom in symptoms_input.split(","):
            index = symptom_index.get(symptom.strip().capitalize())
            if index is not None:
                input_data[index] = 1
        
        # Reshape the input data and make prediction
        input_data = np.array(input_data).reshape(1, -1)
        predicted_disease = encoder.inverse_transform(svm_model.predict(input_data))[0]
        
        # Display the predicted disease
        st.success(f"The predicted disease is: {predicted_disease}")
    else:
        st.warning("Please enter symptoms to predict the disease")


#--------------------------------------------------------------------------

