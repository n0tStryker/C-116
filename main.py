import plotly.graph_objects as go 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

salaries = df["EstimatedSalary"].tolist() 
ages = df["Age"].tolist() 
purchased = df["Purchased"].tolist() 

factors = df[["EstimatedSalary", "Age"]]
purchases = df["Purchased"]

salary_train, salary_test, purchase_train, purchase_test = train_test_split(factors, purchases, test_size = 0.25, random_state = 0)
print(salary_train[0:10])
sc_x =StandardScaler()
salary_train = sc_x.fit_transform(salary_train)
salary_test = sc_x.fit_transform(salary_test)
print(salary_train[0:10])
print()
clasifier = LogisticRegression(random_state=0)
clasifier.fit(salary_train, purchase_train)
purchase_pred = clasifier.predict(salary_test)
from sklearn.metrics import accuracy_score
print("accuracy =",   accuracy_score(purchase_test, purchase_pred))

colors=[] 
for data in purchased: 
  if data == 1: 
    colors.append("green") 
  else: 
    colors.append("red") 
    
fig = go.Figure(data=go.Scatter( x=salaries, y=ages, mode='markers', marker=dict(color=colors) )) 
fig.show()