import streamlit as st

# Set page title
st.title("ML Disease Model")

# List of diseases (replace with your 132 diseases)
diseases = [
    "Disease 1", "Disease 2", "Disease 3",  # Add all 132 diseases here
]

# Display text boxes for each disease
selected_diseases = {}
for disease in diseases:
    selected_diseases[disease] = st.number_input(f"{disease}:", min_value=0, max_value=1, value=0, step=1)

# Save button
if st.button("Save"):
    # Get names of diseases with value 1
    selected_names = [disease for disease, value in selected_diseases.items() if value == 1]
    # Display selected disease names separated by commas
    output_string = ", ".join(selected_names)
    st.text_area("Selected Diseases:", value=output_string, height=100)
