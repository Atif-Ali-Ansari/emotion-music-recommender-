import streamlit as st
from model import train_model

model, vectorizer = train_model()

songs = {
    "happy": ["Happy - Pharrell Williams", "Good Life"],
    "sad": ["Someone Like You", "Fix You"],
    "angry": ["Believer", "Stronger"],
    "relaxed": ["Perfect", "Weightless"],
    "stressed": ["Let It Be", "Fix You"]
}

st.title("🎧 Mood Music Recommender")

user_input = st.text_area("How are you feeling?")

if st.button("Analyze"):
    X_input = vectorizer.transform([user_input])
    mood = model.predict(X_input)[0]

    st.subheader(f"Detected Mood: {mood}")

    st.write("### Recommended Songs:")
    for s in songs[mood]:
        st.write("-", s)