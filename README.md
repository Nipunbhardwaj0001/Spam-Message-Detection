# SMS Spam Detection using NLP

This project uses Natural Language Processing (NLP) and Machine Learning to classify SMS messages as Spam or Not Spam. The model is built using Naive Bayes classifiers, and the project includes a real-time prediction web app built with Streamlit.

## Project Overview
The goal of this project is to predict whether an SMS message is spam or not by leveraging NLP techniques, data preprocessing, and machine learning algorithms. It includes:

- **Data Preprocessing**: Cleaning, tokenization, stemming, and feature extraction.
- **Model Training**: Evaluation of different Naive Bayes models (GaussianNB, MultinomialNB, BernoulliNB).
- **Deployment**: Streamlit web app for real-time predictions.

## Features
- **Text Preprocessing**: Convert text to lowercase, tokenization, stopwords removal, punctuation removal, and stemming.
- **Visualizations**: WordCloud and histograms to explore the dataset.
- **SMS Classification**: Using CountVectorizer and TF-IDF Vectorizer to convert text data into features for machine learning models.
- **Model Evaluation**: Comparison of various classifiers' performance based on accuracy and precision.
- **Real-time Prediction**: A web app using Streamlit where users can enter an SMS message and get an instant spam classification.

## Tech Stack
- **Python**: For data processing, model building, and deployment.
- **NLP Libraries**: NLTK (Natural Language Toolkit).
- **Machine Learning**: Scikit-learn (for model building and evaluation).
- **Web App**: Streamlit (for real-time predictions).
- **Vectorization**: CountVectorizer, TfidfVectorizer.

## Conclusion
This project demonstrates the application of NLP techniques and machine learning models to solve real-world problems like SMS spam detection. You can extend this project to improve classification accuracy or integrate it with other messaging platforms for real-time spam filtering.