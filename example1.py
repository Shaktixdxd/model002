import streamlit as st

# Set page title
st.title("ML Disease Model")

# List of diseases (replace with your 132 diseases)
diseases = [
    "Disease 1", "Disease 2", "Disease 3",  # Add all 132 diseases here
]

# Display disease checkboxes
selected_diseases_code = []

for disease in diseases:
    st.write(disease)
    checkbox_value = st.number_input(f"Enter 0 or 1 for {disease}", min_value=0, max_value=1, value=0, step=1)
    if checkbox_value == 1:
        selected_diseases_code.append(disease)

# Save button
if st.button("Save"):
    selected_diseases_code.sort()  # Sort selected diseases alphabetically
    selected_diseases_string = ", ".join(selected_diseases_code)
    st.text_area("Selected Diseases:", value=selected_diseases_string, height=100)

# Predict button
if st.button("Predict"):
    code_string = 'print(predictDisease("{}"))'.format(selected_diseases_string)
    st.text_area("Python Code:", value=code_string, height=100)
