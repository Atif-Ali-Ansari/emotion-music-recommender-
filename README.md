# Emotion-Based Music Recommendation System

## Project Description

The *Emotion-Based Music Recommendation System* is a Python-based machine learning application that analyzes user text input to detect mood and recommend music 
accordingly. The system uses *Natural Language Processing (NLP)* techniques for emotion detection, with *TF-IDF vectorization* and *Logistic Regression* employed 
for mood classification. The detected moods include *happy, **sad, **angry, **relaxed, and **stressed*, and the system suggests music tracks that align with each 
mood.
The project features both a *command-line interface (CLI)* and an interactive *Streamlit web app*, providing flexibility for user interaction.
## Features

- Emotion classification from text input
- Music recommendations based on mood
- CLI and web app interfaces for interaction

## Technologies Used

- Python
- Scikit-learn (for machine learning and text classification)
- Streamlit (for web interface)
- TF-IDF Vectorization
- Logistic Regression

## Project Architecture
# emotion-music-recommender/ ├── app.py               
# Streamlit web app interface ├── main.py               
# Command-line interface (CLI) ├── model.py              
# Machine learning model (trained classifier) ├── requirements.txt      
# List of dependencies ├── README.md             
# Project documentation

## Installation
1. Clone the repository:
   git clone https://github.com/Atif-Ali-Ansari/emotion-music-recommender.git
2. Navigate to the project directory:
   cd emotion-music-recommender
3. install dependencies:
   cd emotion-music-recommender
4. run the application:
   For the CLI version:
   python main.py

   For the streamlit web app:
   streamlit run  app.py


## Example Input/Output
# Input:
I feel very happy today!
# Output:
Detected Mood: Happy
Recommended Songs:
- "Happy" by Pharrell Williams
- "Good Life" by OneRepublic
  

## Learning Outcomes
- Implemented TF-IDF vectorization for feature extraction from text.
- Applied Logistic Regression to classify emotions.
- Developed a user-friendly Streamlit web app for interaction.

## Future Improvements
- Expand the dataset for better classification accuracy.
- Add more moods and custom song recommendations.
- Enhance the user interface with additional features and styling.
