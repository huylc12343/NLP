# lstm for time series forecasting
from numpy import sqrt
from numpy import asarray
import numpy as np
from pandas import read_csv
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import f1_score

# split a univariate sequence into samples
def split_sequence(sequence, n_steps, n_pred, pred_col):
    X, y = list(), list()
    for i in range(len(sequence) - (n_steps + n_pred) +1):
        # gather input and output parts of the pattern
        seq_x = sequence[i: i+n_steps, :]
        seq_y = sequence[i+n_steps+n_pred -1, pred_col]
        X.append(seq_x)
        y.append(seq_y)
    return asarray(X), asarray(y)

# load the dataset
filename = './LSTM/LSTM-Multivariate_pollution.csv'
all_attributes = ['dew', 'temp', 'press', 'wnd_dir', 'wnd_spd', 'snow', 'rain', 'pollution']
data = read_csv(filename, index_col=False, usecols=all_attributes, encoding='utf-8')[all_attributes]
print(data)
#Chuyển dữ liệu chuỗi sang số nguyên
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
data = data.apply(le.fit_transform)
print(data)
# retrieve the values
values = data.values.astype('float32')
# print(values)
# specify the window size
n_steps = 3
n_pred = 2
# split into samples
X, y = split_sequence(values, n_steps, n_pred, -3)
# print(X)
# print(y)
# reshape into [samples, timesteps, features]
X = X.reshape((X.shape[0], X.shape[1], len(all_attributes)))
# split into train/test
n_test = 1000
X_train, X_test, y_train, y_test = X[:-n_test], X[-n_test:], y[:-n_test], y[-n_test:]
#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, shuffle=false)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# convert labels to categorical
num_classes = 28
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

# define model
model = Sequential()
model.add(LSTM(100, activation='relu', kernel_initializer='he_normal', input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(50, activation='relu', kernel_initializer='he_normal'))
model.add(Dense(50, activation='relu', kernel_initializer='he_normal'))
model.add(Dense(28, activation='softmax'))
# compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# fit the model
model.fit(X_train, y_train, epochs=5, batch_size=32, verbose=2, validation_data=(X_test, y_test))
# evaluate the model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print('Loss: %.3f, Accuracy: %.3f' % (loss, accuracy))

# make predictions

y_pred = model.predict(X_test)
y_pred = np.argmax(y_pred, axis=1)
y_true = np.argmax(y_test, axis=1)

# calculate F1 score
#f1 = f1_score(y_true, y_pred, average='weighted')
#print('F1 Score:', f1)