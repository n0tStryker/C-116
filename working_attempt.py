import plotly.graph_objects as go 
salaries = df["EstimatedSalary"].tolist() 
ages = df["Age"].tolist() 
purchased = df["Purchased"].tolist() 
colors=[] 
for data in purchased: 
  if data == 1: 
    colors.append("green") 
  else: 
    colors.append("red") 
    
fig = go.Figure(data=go.Scatter( x=salaries, y=ages, mode='markers', marker=dict(color=colors) )) 
fig.show()