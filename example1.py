import streamlit as st

# Set page title
st.title("Disease Prediction using ML")

# Text display box
text_input = st.text_area("Selected Diseases:")

# Button to clear text
if st.button("CLEAR"):
    text_input = ""

# List of diseases (replace with your 132 diseases)
diseases = [
    "Disease 1", "Disease 2", "Disease 3",  # Add all 132 diseases here
]

# Display buttons for each disease
for disease in diseases:
    if st.button(disease):
        # Append disease name to text input
        if text_input:
            text_input += ", "
        text_input += disease

# Sort and display selected diseases alphabetically
selected_diseases = sorted(text_input.split(", "))
output_string = ", ".join(selected_diseases)
st.write("Output:", output_string)
