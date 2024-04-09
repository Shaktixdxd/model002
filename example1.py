import numpy as np
import pandas as pd
from scipy.stats import mode
#import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#%matplotlib inline

# Reading the train.csv by removing the 
# last column since it's an empty column
DATA_PATH = "dataset/Training.csv"
data = pd.read_csv('Training.csv').dropna(axis=1)

# Checking whether the dataset is balanced or not
disease_counts = data["prognosis"].value_counts()
temp_df = pd.DataFrame({
    "Disease": disease_counts.index,
    "Counts": disease_counts.values
})

# Encoding the target value into numerical
# value using LabelEncoder
encoder = LabelEncoder()
data["prognosis"] = encoder.fit_transform(data["prognosis"])

# Training and testing SVM Classifier
svm_model = SVC()
svm_model.fit(X_train, y_train)
preds = svm_model.predict(X_test)

print(f"Accuracy on train data by SVM Classifier: {accuracy_score(y_train, svm_model.predict(X_train))*100}")
print(f"Accuracy on test data by SVM Classifier: {accuracy_score(y_test, preds)*100}")


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

# Defining the Function
# Input: string containing symptoms separated by commas
# Output: Generated predictions by models
def predict_Disease(symptoms):
    symptoms = symptoms.split(",")
    
    # creating input data for the models
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        index = data_dict["symptom_index"][symptom]
        input_data[index] = 1
        
    # reshaping the input data and converting it
    # into suitable format for model predictions
    input_data = np.array(input_data).reshape(1, -1)
    
    # generating individual outputs
    svm_prediction = data_dict["predictions_classes"][svm_model.predict(input_data)[0]]
    
    predictions = {
        "svm_model_prediction": svm_prediction,
        "final_prediction": svm_prediction
    }
    return predictions

# Testing the function
print(predict_Disease("Itching,Nodal Skin Eruptions,Skin Rash"))
print(predict_Disease("Bladder Discomfort,Continuous Feel Of Urine,Burning Micturition"))

_______________________________________________________________________________________


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
    st.write(Hello)
    st.write("Hello2")

#if st.button('Predict'):
 #       diabzxc = diabetes_model.predict([[DiseasesXYZ]])
        
       # if (diab_prediction[0] == 1):
        #  diab_diagnosis = 'The person is diabetic'
        # else:
         # diab_diagnosis = 'The person is not diabetic'
        
    #st.success(diab_diagnosis)


