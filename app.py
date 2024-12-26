import nltk
nltk.download('punkt')
nltk.download('stopwords')

import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Initialize PorterStemmer
ps = PorterStemmer()

# Text transformation function
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load models
tk = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("model.pkl", 'rb'))

# Custom CSS
st.markdown("""
    <style>
    .main {background-color: #f5f5f5;}
    .title {color: #2F4F4F; text-align: center; font-size: 2.5em; font-weight: bold;}
    .footer {color: gray; text-align: center; font-size: 0.9em; margin-top: 20px;}
    .header {color: white; background-color: #4CAF50; padding: 10px; text-align: center; border-radius: 10px;}
    .spam {color: white; background-color: #ff4d4d; padding: 10px; text-align: center; border-radius: 10px;}
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<div class='title'>SMS Spam Detection Model 📱</div>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("About the App")
st.sidebar.write("This app detects whether an SMS message is Spam or Not Spam using an NLP model.")
st.sidebar.write("🔍 **Instructions:** Enter a message and click 'Predict'.")

# Input Section
input_sms = st.text_area("Enter the SMS below", placeholder="Type your SMS message here...")

if st.button('Predict'):
    if input_sms.strip():
        # Preprocess
        transformed_sms = transform_text(input_sms)
        # Vectorize
        vector_input = tk.transform([transformed_sms])
        # Predict
        result = model.predict(vector_input)[0]
        # Display result
        if result == 1:
            st.markdown("<div class='spam'>🚫 Spam</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='header'>✅ Not Spam</div>", unsafe_allow_html=True)
    else:
        st.error("⚠️ Please enter a valid SMS message.")

# Footer
st.markdown("<div class='footer'>Made with by Nipun Bhardwaj</div>", unsafe_allow_html=True)
