
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

        if predicted_disease == 15:
            disease_name = "Fungal Infection"
        if predicted_disease == 1:
            disease_name = "Acne"
        if predicted_disease == 2:
            disease_name = "AIDS"
        if predicted_disease == 3:
            disease_name = "Alcoholic Hepatitis"
        if predicted_disease == 4:
            disease_name = "Allergy"
        if predicted_disease == 5:
            disease_name = "Arthritis"
        if predicted_disease == 6:
            disease_name = "Bronchial Asthma"
        if predicted_disease == 7:
            disease_name = "Cervical Spondylosis"
        if predicted_disease == 8:
            disease_name = "Chicken Pox"
        if predicted_disease == 9:
            disease_name = "Chronic Cholestasis"
        if predicted_disease == 10:
            disease_name = "Common Cold"
        if predicted_disease == 11:
            disease_name = "Dengue"
        if predicted_disease == 12:
            disease_name = "Diabetes"
        if predicted_disease == 13:
            disease_name = "Dimorphic Hemorrhoids (Piles)"
        if predicted_disease == 14:
            disease_name = "Drug Reaction"
        if predicted_disease == 15:
            disease_name = "Fungal Infection"
        if predicted_disease == 16:
            disease_name = "Gastroenteritis"
        if predicted_disease == 17:
            disease_name = "GERD"
        if predicted_disease == 18:
            disease_name = "Heart Attack"
        if predicted_disease == 19:
            disease_name = "Hepatitis A"
        if predicted_disease == 20:
            disease_name = "Hepatitis B"
        if predicted_disease == 21:
            disease_name = "Hepatitis C"
        if predicted_disease == 22:
            disease_name = "Hepatitis D"
        if predicted_disease == 23:
            disease_name = "Hepatitis E"
        if predicted_disease == 24:
            disease_name = "Hypertension"
        if predicted_disease == 25:
            disease_name = "Hyperthyroidism"
        if predicted_disease == 26:
            disease_name = "Hypoglycemia"
        if predicted_disease == 27:
            disease_name = "Hypothyroidism"
        if predicted_disease == 28:
            disease_name = "Impetigo"
        if predicted_disease == 29:
            disease_name = "Jaundice"
        if predicted_disease == 30:
            disease_name = "Malaria"
        if predicted_disease == 31:
            disease_name = "Migraine"
        if predicted_disease == 32:
            disease_name = "Osteoarthritis"
        if predicted_disease == 33:
            disease_name = "Paralysis (Brain Hemorrhage)"
        if predicted_disease == 34:
            disease_name = "Paroxysmal Positional Vertigo (Vertigo)"
        if predicted_disease == 35:
            disease_name = "Peptic Ulcer Disease"
        if predicted_disease == 36:
            disease_name = "Pneumonia"
        if predicted_disease == 37:
            disease_name = "Psoriasis"
        if predicted_disease == 38:
            disease_name = "Tuberculosis"
        if predicted_disease == 39:
            disease_name = "Typhoid"
        if predicted_disease == 40:
            disease_name = "Urinary Tract Infection"
        if predicted_disease == 41:
            disease_name = "Varicose Veins"
        
        # Display the predicted disease
        st.success(f"The predicted disease is: {disease_name}")
    else:
        st.warning("Please enter symptoms to predict the disease")


#--------------------------------------------------------------------------

