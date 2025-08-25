import streamlit as st
import pickle
import pandas as pd


cpipeline = pickle.load(open('svm_classification_model.pkl', 'rb'))

import os
import streamlit as st

st.write("Current folder:", os.getcwd())
st.write("Files here:", os.listdir())


st.title('🚢 Titanic Survival Prediction: Dead or Alive')
st.write("Enter the details below to predict survival:")

Pclass = st.number_input("Pclass (1 = 1st, 2 = 2nd, 3 = 3rd): ", min_value=1, max_value=3, step=1)
Sex = st.selectbox("Sex", ["male", "female"])
Age = st.number_input("Age: ", min_value=0, max_value=100, step=1)
SibSp = st.number_input("Siblings/Spouses aboard (SibSp): ", min_value=0, step=1)
Parch = st.number_input("Parents/Children aboard (Parch): ", min_value=0, step=1)
Fare = st.number_input("Fare: ", min_value=0.0, step=0.1)
Embarked = st.selectbox("Embarked", ["C", "Q", "S"])
CabinDeck = st.text_input("Cabin Deck (e.g., A, B, C, D, E): ")
FamilySize = st.number_input("Family Size: ", min_value=0, step=1)

features = pd.DataFrame([{
    "Pclass": Pclass,
    "Sex": Sex,
    "Age": Age,
    "SibSp": SibSp,
    "Parch": Parch,
    "Fare": Fare,
    "Embarked": Embarked,
    "CabinDeck": CabinDeck,
    "FamilySize": FamilySize
}])

if st.button("Predict: Dead or Alive"):
    prediction = cpipeline.predict(features)
    st.success("✅ Survived" if prediction[0] == 1 else "❌ Did not survive")
