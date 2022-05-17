import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from IPython.display import Image
data = pd.read_csv("data.csv")
# data
le=LabelEncoder();
x=data.iloc[:,:-1]
print(type(x))
x=x.apply(le.fit_transform)
print(type(x))
print("Age:",list( zip(data.iloc[:,0], x.iloc[:,0])))
print("\nIncome:",list( zip(data.iloc[:,1], x.iloc[:,1])))
print("\nGender:",list( zip(data.iloc[:,2], x.iloc[:,2])))
print("\nmaritialStatus:",list( zip(data.iloc[:,3], x.iloc[:,3])))
print(x)
y=data.iloc[:,-1]
dt=DecisionTreeClassifier()
dt.fit(x,y)
#[Age < 21, Income = Low,Gender = Female, Marital Status = Married]
query=np.array([1,1,0,0])
pred=dt.predict([query])
pred[0]
# export_graphviz(dt,out_file="data.dot",feature_names=x.columns,class_names=["No","Yes"])
# # !dot -Tpng data.dot -o tree.png
# Image("tree.png")
