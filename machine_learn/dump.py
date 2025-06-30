import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split # for test
from sklearn.metrics import accuracy_score  # for metric
# from sklearn.externals import joblib
import joblib


# Load data
df = pd.read_csv("music.csv")  # Must contain 'genre' column and features like age, gender

# Prepare input and output
X = df.drop(columns=['genre'])  # Input features
y = df['genre']                 # Output label

# Split into training and testing sets
# 80% for training, 20% for testing
# input data-set x_train,x_test
# output data-set y_train,y_test
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the model on training data
model = DecisionTreeClassifier()
# use the input and output
# model.fit(X, y)
model.fit(x_train, y_train)


# Optional: Load the model and use it again
# model = joblib.load('music-recommendation.joblib')
# prediction = model.predict(x_test)
# score = accuracy_score(y_test, prediction)
# print("Accuracy:", score)
# Predict with feature names use this 
# input_data = pd.DataFrame([[21,1],[22,0]], columns=X.columns)
# prediction = model.predict(input_data)
# save dump

joblib.dump(model, 'music-recommendation.joblib')
# load the model
# joblib.load(model,' music-recommendation.joblib')
# Predict using the test data
# prediction = model.predict(x_test)

# Evaluate accuracy of prediction compared to true labels
# score = accuracy_score(y_test, prediction)

# print("Accuracy:", score)
# print("Predictions:", prediction)
