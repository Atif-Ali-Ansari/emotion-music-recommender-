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
## emotion-music-recommender/ ├── app.py               
## Streamlit web app interface ├── main.py               
## Command-line interface (CLI) ├── model.py              
## Machine learning model (trained classifier) ├── requirements.txt      
## List of dependencies ├── README.md             
## Project documentation

## Installation and Usage

```bash
# Clone the repository
git clone https://github.com/AtifAliAnsari/emotion-music-recommender.git
cd emotion-music-recommender

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run CLI version
python main.py

# Run Streamlit app
streamlit run app.py
```
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
