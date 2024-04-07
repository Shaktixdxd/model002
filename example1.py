import streamlit as st

# Set page title
st.title("ML Disease Model")

# List of diseases (replace with your 132 diseases)
diseases = [
    "Disease 1", "Disease 2", "Disease 3",  # Add all 132 diseases here
]

# Display disease checkboxes and buttons
for disease in diseases:
    st.write(disease)
    checkbox_value = st.number_input(f"Enter 0 or 1 for {disease}", min_value=0, max_value=1, value=0, step=1)
    

# You can add any additional content or functionality here
