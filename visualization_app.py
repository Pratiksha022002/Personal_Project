# visualization_app.py
import streamlit as st
import pandas as pd

# Load your data
data = pd.read_csv("Cleaned_data.csv")


def main():
    st.title("House Price Prediction")

    # Allow user to optionally enter location
    location_options = data['location'].unique()
    location_input = st.selectbox("Select Area Type", location_options)

    # Allow user to optionally select number of bedrooms (BHK)
    bhk_options = sorted(data['bhk'].unique())
    bhk_input = st.selectbox("Select Number of Bedrooms (BHK)", bhk_options)

    # Filter data based on user's inputs
    filtered_data = data.copy()
    if location_input:
        filtered_data = filtered_data[filtered_data['location'] == location_input]
    if bhk_input:
        bhk_input = int(bhk_input)  # Convert input to integer
        filtered_data = filtered_data[filtered_data['bhk'] == bhk_input]

    # Display the filtered data
    st.write("Filtered Data Overview:")
    st.dataframe(filtered_data)

    # Add more visualizations or analysis as needed
    # Example:
    # st.bar_chart(filtered_data['price'])


if __name__ == "__main__":
    main()
