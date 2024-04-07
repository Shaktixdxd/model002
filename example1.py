import streamlit as st

# Set page title
st.title("Disease Prediction using ML")

# Text display box
text_input = st.text_area("Selected Diseases:")

# Button to clear text
if st.button("CLEAR"):
    text_input = ""

# List of diseases (replace with your list of 132 diseases)
diseases = [
    "Disease 1", "Disease 2", "Disease 3",  # Add all 132 diseases here
]

# Display buttons for each disease
for disease in sorted(diseases):  # Sort diseases alphabetically
    if st.button(disease):
        # If text area is not empty, add a comma before adding new disease
        if text_input:
            text_input += ", "
        text_input += disease

# Output the selected diseases as a comma-separated string
st.write("Output:", text_input)
