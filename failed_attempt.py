import plotly.express as px
import csv
import numpy as np
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("logistics_data.csv")
salary_list = df["EstimatedSalary"].tolist()
purchased_list = df["Purchased"].tolist()
ages_list = df["Age"].tolist()
colors = []
for data in purchased_list:
  if data == 1:
    colors.append('green')
  else:
    colors.append('red')
fig = go.Figure(data = go.Scatter(
    x = salary_list, y = ages_list, 
    mode = 'marker', marker = dict(color = colors)
))
fig.show()
