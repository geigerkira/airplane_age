import streamlit as st
import pandas as pd
import joblib

# Modell betöltése
model = joblib.load('model.pkl')

# Cím és leírás
st.title("Age Predictor App")
# Input mezők
st.header("Adatok bevitele:")
type_of_travel = st.selectbox("Type of Travel", [0, 1], format_func=lambda x: "Personal" if x == 0 else "Business")
leg_room_service = st.slider("Leg Room Service", 0, 5, 3)  # Csúszka 0-tól 5-ig
food_and_drink = st.slider("Food and Drink", 0, 5, 3)
online_boarding = st.slider("Online Boarding", 0, 5, 3)
inflight_entertainment = st.slider("Inflight Entertainment", 0, 5, 3)
cleanliness = st.slider("Cleanliness", 0, 5, 3)
class_business = st.selectbox("Business Class", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
inflight_service = st.slider("Inflight Service", 0, 5, 3)
on_board_service = st.slider("On-board Service", 0, 5, 3)

# Inputok dataframe-be alakítása
input_data = pd.DataFrame({
    'Type of Travel': [type_of_travel],
    'Leg room service': [leg_room_service],
    'Food and drink': [food_and_drink],
    'Online boarding': [online_boarding],
    'Inflight entertainment': [inflight_entertainment],
    'Cleanliness': [cleanliness],
    'Class_Business': [class_business],
    'Inflight service': [inflight_service],
    'On-board service': [on_board_service]
})

# Predikció futtatása
if st.button("Prediktálás"):
    prediction = model.predict(input_data)
    age_category = ["Fiatal", "Idősebb"]
    st.success(f"Prediktált életkor kategória: {age_category[prediction[0]]}")
