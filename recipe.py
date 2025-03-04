import streamlit as st
import requests
import json

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

st.title("AI Recipe Recommender")
st.write("Heloooooooo!")

cuisine = st.selectbox("What cuisine do you prefer?", ["Indian", "Chinese", "Mexican"])
veg = st.radio("Are you vegetarian?", [True, False])
allergies = st.text_input("What foods do you have allergy to?")
difficulty = st.radio("How would you describe your cooking skills?", ["Novice", "Somewhat Experienced", "Professional"])
main_item = st.text_input("Let us know some of the ingredients which you want to use.")


if st.button("Generate Recipe"):
    
    with st.spinner("Generating your recipe..."):
        recipe = ""
        header = {
            "Content-Type": "application/json"
        }
        query = f"Please recommend me a recipe of cuisine {cuisine}, that contains {main_item}. My cooking skills can be described as {difficulty}. I have allergies to {allergies}. Please give me only the name, ingredients and elaborate instructions in the response; do not write any other sentences."
        if (veg):
            query = query + " The recipe must be purely vegetarian."
        data = {
            "contents": [{
                "parts": [{
                    "text": query
                }]
            }]
        }
        response = requests.post(URL, headers=header, data=json.dumps(data))
    st.divider()
    st.write(response.json()["candidates"][0]["content"]["parts"][0]["text"])