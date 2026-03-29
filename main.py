from model import train_model

model, vectorizer = train_model()

songs = {
    "happy": ["Happy - Pharrell Williams", "Good Life"],
    "sad": ["Someone Like You", "Fix You"],
    "angry": ["Believer", "Stronger"],
    "relaxed": ["Perfect", "Weightless"],
    "stressed": ["Let It Be", "Fix You"]
}

print("\n🎧 Mood Music Recommender")

user_input = input("\nHow are you feeling?\n> ")

X_input = vectorizer.transform([user_input])
mood = model.predict(X_input)[0]

print("\n🎭 Mood:", mood.upper())
print("\n🎶 Songs:")
for s in songs[mood]:
    print("-", s)