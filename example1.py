import streamlit as st

# Set page title
st.title("ML Disease Model")

# List of diseases (replace with your 132 diseases)
diseases = [
    "Disease 1", "Disease 2", "Disease 3",  # Add all 132 diseases here
]

# Display disease checkboxes and buttons
for disease in diseases:
    col1, col2 = st.columns([4, 1])
    with col1:
        st.write(disease)
    with col2:
        checkbox_value = st.number_input("", min_value=0, max_value=1, value=0, step=1)

# Save button
if st.button("Save"):
    selected_diseases = [disease for disease, value in zip(diseases, checkbox_values) if value == 1]
    selected_diseases.sort()  # Sort selected diseases alphabetically
    output_string = ", ".join(selected_diseases)
    st.text_area("Selected Diseases:", value=output_string)

# Copy button
if st.button("Predict"):
    # getting the input data from the user
    col1 = st.columns(1)
        Diseases = st.text_input('Number of Pregnancies')
