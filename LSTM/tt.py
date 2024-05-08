from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd

# Load data
data = pd.read_csv('D:\\NLP\\DataCrawled.csv')

# Preparing the data
X = data['Comment']
y = data['Label'].apply(lambda x: 1 if x == 'Bad' else 0)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a pipeline with TF-IDF and SVM
pipeline = make_pipeline(TfidfVectorizer(), SVC(class_weight='balanced', probability=True))

# Define the parameter grid
param_grid = {
    'svc__C': [0.1, 1, 10],
    'svc__kernel': ['linear', 'rbf'],
    'svc__gamma': ['scale', 'auto']
}

# Grid search with cross-validation
grid_search = GridSearchCV(pipeline, param_grid, cv=5, verbose=2)
grid_search.fit(X_train, y_train)

# Best estimator
print("Best parameters:", grid_search.best_params_)

# Evaluate the model
y_pred = grid_search.predict(X_test)
print(classification_report(y_test, y_pred))
# print(y_test,y_pred)
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
