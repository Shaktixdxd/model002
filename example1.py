
import streamlit as st

# Set page title
st.title("ML Disease Prediction Model")

# List of symptoms (replace with your 132 symptoms)
symptoms = [
    "Abdominal Pain", "Abnormal Menstruation", "Acidity", "Acute Liver Failure", "Altered Sensorium", "Anxiety", 
    "Back Pain", "Belly Pain", "Blackheads", "Blister", "Blood in Sputum", "Bloody Stool", "Blurred and Distorted Vision", 
    "Breathlessness", "Brittle Nails", "Burning Micturition", "Chills", "Cold Hands and Feets", "coma", "Congestion", 
    "Constipation", "Continuous Feel of Urine", "Continuous Sneezing", "Cough", "Cramps", "Dark Urine", "Dehydration", 
    "Depression", "Diarrhoea", "Dischromic Patches", "Dizziness", "Drying and Tingling Lips", "Enlarged Thyroid", 
    "Excessive Hunger", "Extra Marital Contacts", "Family History", "Fast Heart Rate", "Fatigue", "Fluid Overload", 
    "Foul Smell of Urine", "Frequent Urination", "High Fever", "History of Alcohol Consumption", "Hip Joint Pain", 
    "Irritability", "Irritation in Anus", "Itching", "Joint Pain", "Knee Pain", "Lack of Concentration", "Lethargy", 
    "Loss of Appetite", "Loss of Balance", "Loss of Smell", "Malaise", "Mood Swings", "Movement Stiffness", "Muscle Pain", 
    "Muscle Weakness", "Muscle Wasting", "Mucoid Sputum", "Nausea", "Neck Pain", "Nodal Skin Eruptions", "Obesity", 
    "Pain Behind the Eyes", "Pain During Bowel Movements", "Pain in Anal Region", "Painful Walking", "Palpitations", 
    "Passage of Gases", "Phlegm", "Polyuria", "Prominent Veins on Calf", "Puffy Face and Eyes", "Pus Filled Pimples", 
    "Rapid Heart Rate", "Red Sore Around Nose", "Red Spots Over Body", "Receiving Blood Transfusion", 
    "Receiving Unsterile Injections", "Restlessness", "Rusty Sputum", "Runny Nose", "Scarring", "Shivering", 
    "Silver Like Dusting", "Sinus Pressure", "Skin Peeling", "Skin Rash", "Small Dents in Nails", "Spinning Movements", 
    "Spotting Urination", "Stiff Neck", "Stomach Bleeding", "Stomach Pain", "Sudden High Fever", "Sunken Eyes", "Sweating", 
    "Swelling Joints", "Swelling of Stomach", "Swollen Blood Vessels", "Swollen Extremities", "Swollen Legs", "Throat Irritation", 
    "Toxic Look (Typhos)", "Ulcers on Tongue", "Unsteadiness", "Visual Disturbances", "Vomiting", "Watering from Eyes", 
    "Weakness in Limbs", "Weakness of One Body Side", "Weight Gain", "Weight Loss", "Yellow Crust Ooze", "Yellowing of Eyes", "Yellowish Skin"
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


#--------------------------------------------------------------------------
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC

# Load the dataset
@st.cache(suppress_st_warning=True)
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

