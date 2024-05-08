import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline

# Load data
data = pd.read_csv('D:\\NLP\\DataCrawled.csv')
data['Label'] = data['Label'].apply(lambda x: 'Good' if x == 'Good' else 'Bad')

# Prepare data
X = data['Comment']
y = data['Label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a pipeline with TF-IDF and SVM
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('svm', SVC(kernel='linear', class_weight='balanced', probability=True))
])

# Train the model
pipeline.fit(X_train, y_train)

# Function to predict the sentiment of a sentence
def predict_sentiment(sentence):
    prediction = pipeline.predict([sentence])
    return prediction[0]

# Example usage
sentence ="Đỉnh ơi là đỉnh"
result = predict_sentiment(sentence)
print(f"The sentiment of the sentence is: {result}")
