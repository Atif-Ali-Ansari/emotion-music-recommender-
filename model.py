from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def train_model():
    texts = [
        "I am very happy and excited",
        "I feel amazing and joyful",
        "This is the best day ever",
        "I am feeling great",

        "I feel sad and lonely",
        "I am depressed",
        "I feel bad today",
        "I am unhappy",

        "I am angry and frustrated",
        "This makes me mad",
        "I am irritated",
        "I feel rage",

        "I feel calm and relaxed",
        "I am peaceful",
        "I feel relaxed",
        "I enjoy quiet time",

        "I am stressed and tired",
        "I feel overwhelmed",
        "I am exhausted",
        "I feel anxious"
    ]

    labels = [
        "happy","happy","happy","happy",
        "sad","sad","sad","sad",
        "angry","angry","angry","angry",
        "relaxed","relaxed","relaxed","relaxed",
        "stressed","stressed","stressed","stressed"
    ]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    model = LogisticRegression()
    model.fit(X, labels)

    return model, vectorizer