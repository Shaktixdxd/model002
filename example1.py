import streamlit as st
import pickle

# Load the saved models
svm_model = pickle.load(open('final_svm.sav', 'rb'))
#rf_model = pickle.load(open('final_rf.sav', 'rb'))
nb_model = pickle.load(open('final_nb.sav', 'rb'))

# Function to predict diseases based on selected symptoms
def predict_diseases(selected_symptoms):
    # Create input vector
    input_vector = [0] * len(diseases)
    for symptom, value in selected_symptoms.items():
        input_vector[diseases.index(symptom)] = value
    
    # Make predictions using loaded models
    svm_prediction = svm_model.predict([input_vector])[0]
    #rf_prediction = rf_model.predict([input_vector])[0]
    nb_prediction = nb_model.predict([input_vector])[0]
    
    # Combine predictions and return
    predictions = [svm_prediction, nb_prediction]
    return predictions

# Set page title
st.title("ML Disease Model")

# List of diseases (replace with your 132 diseases)
diseases = [
    "Disease 1", "Disease 2", "Disease 3",  # Add all 132 diseases here
]

# Dictionary to store symptom values
symptom_values = {}

# Display checkboxes for each disease
for disease in diseases:
    st.write(disease)
    symptom_values[disease] = st.number_input(f"{disease}:", min_value=0, max_value=1, value=0, step=1, key=disease)

# Save button
if st.button("Save"):
    # Get selected diseases with value 1
    selected_diseases = [disease for disease, value in symptom_values.items() if value == 1]
    selected_diseases.sort()  # Sort alphabetically
    output_string = ", ".join(selected_diseases)
    st.text_area("Selected Diseases (Alphabetical Order):", value=output_string, height=100)

# Load the .sav files
st.sidebar.title("Load Models")

# Load SVM model
if st.sidebar.button("Load SVM Model"):
    svm_model = pickle.load(open('final_svm.sav', 'rb'))
    st.sidebar.success("SVM Model Loaded Successfully!")

# Load Random Forest model
if st.sidebar.button("Load Random Forest Model"):
    rf_model = pickle.load(open('final_rf.sav', 'rb'))
    st.sidebar.success("Random Forest Model Loaded Successfully!")

# Load Naive Bayes model
if st.sidebar.button("Load Naive Bayes Model"):
    nb_model = pickle.load(open('final_nb.sav', 'rb'))
    st.sidebar.success("Naive Bayes Model Loaded Successfully!")
