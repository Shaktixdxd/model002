import streamlit as st

# Set page title
st.title("Disease Prediction using ML")

# Text display box
text_input = st.text_area("Enter your text here:")

# Button to copy text
if st.button("COPY"):
    st.text_area("Copied Text:", value=text_input, height=100)

# Button to clear text
if st.button("CLEAR"):
    text_input = ""

# List of diseases
diseases = [
    "Disease 1", "Disease 2", "Disease 3",  # Add all 132 diseases here
]

# Display buttons for each disease
for disease in diseases:
    if st.button(disease):
        # If text area is not empty, add a comma before adding new disease
        if text_input:
            text_input += ", "
        text_input += disease

# Display selected diseases
st.text_area("Selected Diseases:", value=text_input, height=200)
