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
for disease in diseases:
    if st.button(disease):
        # Add disease name to the text box
        if text_input:
            text_input += ", " + disease
        else:
            text_input += disease

# Sort the disease names alphabetically
disease_list = text_input.split(", ")
disease_list.sort()

# Display the sorted disease names in the text box
sorted_text = ", ".join(disease_list)
st.text_area("Selected Diseases:", value=sorted_text, height=200)
