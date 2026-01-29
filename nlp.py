import pandas as pd
import numpy as np
import nltk
import re
import matplotlib.pyplot as plt

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

nltk.download('stopwords')

# Load Dataset
data = pd.read_csv("dataset.csv")

# Text Preprocessing
stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))

def preprocess(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower().split()
    text = [stemmer.stem(word) for word in text if word not in stop_words]
    return " ".join(text)

data['clean_text'] = data['text'].apply(preprocess)

# Features & Labels
X = data['clean_text']
y = data['sentiment']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Vectorization
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model Training
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Prediction
y_pred = model.predict(X_test_vec)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.colorbar()
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Custom Prediction
def predict_sentiment(text):
    text = preprocess(text)
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]

print("\nSample Prediction:")
print("I love this product →", predict_sentiment("I love this product"))
print("This is terrible →", predict_sentiment("This is terrible"))
