import streamlit as st

# Set page title
st.title('Disease Prediction using ML')

# Create a text display box
text_input = st.text_area("Selected Diseases", height=100, max_chars=500)

# List of 132 diseases
disease_list = [
    "Acute bronchitis",
    "Acute sinusitis",
    "Acute sinusitis caused by allergy",
    # Add all 132 diseases here...
]

# Function to handle button click event
def button_click(disease_name):
    global text_input
    if text_input:
        text_input += f", {disease_name}"
    else:
        text_input = disease_name

# Create buttons for each disease
for disease in disease_list:
    if st.button(disease):
        button_click(disease)

# Display selected diseases
st.write("Selected Diseases:", text_input)
