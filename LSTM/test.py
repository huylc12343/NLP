import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import preprocessing

# Load your dataset
df = pd.read_csv('D:\\NLP\\DataCrawled.csv')

# Encode labels
le = preprocessing.LabelEncoder()
df = df.apply(le.fit_transform)
df = np.array(df)

# Splitting the dataset into training and test sets
dt_Train, dt_Test = train_test_split(df, test_size=0.3, shuffle=True)

# Extract features and labels correctly
X_train = dt_Train[:, :-1]  # Assuming the last column is the label
y_train = dt_Train[:, -1]
X_test = dt_Test[:, :-1]  # Same assumption
y_test = dt_Test[:, -1]

# Initialize and fit the SVM
svm = SVC(max_iter=-1, kernel='linear', class_weight={0: 0.1, 1: 0.99}, gamma='auto', shrinking=True, tol=0.001, cache_size=200)
svm.fit(X_train, y_train)  # Fit the model
y_predict = svm.predict(X_test)  # Predict using the test set

# Calculate the accuracy
count = np.sum(y_test == y_predict)
print('Ty le du doan dung:', count / len(y_predict))
print(y_test,y_predict)
