import streamlit as st

# Set page title
st.title("ML Disease Model")

# List of diseases (replace with your 132 diseases)
diseases = [
    "Disease 1", "Disease 2", "Disease 3",  # Add all 132 diseases here
]

# Display disease checkboxes
for disease in diseases:
    st.checkbox(disease)

# Reset button
if st.button("Reset"):
    # Reload the page
    st.experimental_rerun()

# Predict button
if st.button("Predict"):
    # Add prediction logic here
    st.write("Prediction result will appear here...")
