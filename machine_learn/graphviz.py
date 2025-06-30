import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Load data
df = pd.read_csv("music.csv")  # Ensure this file exists and has 'genre', 'age', 'gender' columns

# Prepare input and output
X = df.drop(columns=['genre'])  # Input features
y = df['genre']                 # Output label

# Create and train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Export the decision tree to a .dot file (used for visualization)
tree.export_graphviz(
    model,
    out_file='music-recommendation.dot',
    feature_names=['age', 'gender'],       # ✅ Corrected: feature_names (not feature_name)
    class_names=sorted(y.unique()),        # ✅ Corrected: class_names (not class_name)
    label='all',
    rounded=True,
    filled=True
)
