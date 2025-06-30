import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load data
df = pd.read_csv("music.csv")

# Prepare input and output
X = df.drop(columns=['genre'])
y = df['genre']

# Train model
model = DecisionTreeClassifier()
# model.fit(X, y)
model.fit(X, y)  # where X is a DataFrame with column names like 'age' and 'gender'
# Feature names: ['age', 'gender']
# input_data = pd.DataFrame([[21, 1]], columns=['age', 'gender'])
# model.predict(input_data)
# [[21, 1]]  # ⚠️ Warning — no feature names

prediction =model.predict([[21,1],[22,0]])
prediction
