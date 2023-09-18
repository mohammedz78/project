import streamlit as st
import pickle

# Load the pickled model
with open('data.pickle', 'rb') as file:
    model = pickle.load(file)

# Define the weather categories
weather_categories = ['drizzle', 'rain', 'sun', 'snow', 'fog']

# Streamlit app
st.title('Weather Prediction App')

# User input for the features
st.header('Input Features')
precipitation = st.slider('Precipitation', 0.0, 100.0, 10.0)
temp_max = st.slider('Max Temperature', -10.0, 40.0, 20.0)
temp_min = st.slider('Min Temperature', -10.0, 40.0, 10.0)
wind = st.slider('Wind', 0.0, 30.0, 10.0)

# Button to trigger the prediction
if st.button('Predict Weather'):
    # Predict the weather based on the input features
    input_features = [[precipitation, temp_max, temp_min, wind]]
    predicted_weather_index = model.predict(input_features)[0]

    # Map the predicted index to the weather category
    predicted_weather = weather_categories[predicted_weather_index]

    # Display the predicted weather
    st.header('Predicted Weather')
    st.write('The predicted weather is:', predicted_weather)
