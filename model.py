import pickle as pk
from sklearn.linear_model import LogisticRegression
with open('model' , "rb") as f:
    md = pk.load(f)
a = [6.5, 3.2, 5.1, 2.0]

plant = ['setosa', 'versicolor', 'virginica']

def predict_it(f):
    f = [f]
    return plant[md.predict(f)[0]]


print(predict_it(a))
