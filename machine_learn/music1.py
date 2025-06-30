import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 

# Load data
df = pd.read_csv("music.csv")

# Prepare input and output
X = df.drop(columns=['genre'])
y = df['genre']
# allocating 20% to train
# input data-set x_train,x_test
# output data-set y_train,y_test
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

# Train model
model = DecisionTreeClassifier()
#model.fit(X, y) # use the input and output
# use the this instead
model.fit(x_train,y_train)
# Predict with feature names use this 
# input_data = pd.DataFrame([[21,1],[22,0]], columns=X.columns)
 
# prediction = model.predict(input_data)
input_data = pd.DataFrame([x_test,], columns=X.columns)

prediction = model.predict(input_data)
score =accuracy_score(y_test,prediction)

print(score )
print(prediction)
