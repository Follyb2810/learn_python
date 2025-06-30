import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load data
df = pd.read_csv("music.csv")

# Prepare input and output
X = df.drop(columns=['genre'])
y = df['genre']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict with feature names
input_data = pd.DataFrame([[21,1],[22,0]], columns=X.columns)
prediction = model.predict(input_data)

print(prediction)
