import pandas as ps 
import plotly.express as px
with open ("C:\c106hw\cups of coffee vs hours of sleep.csv")as csv_file:
    df = csv.dictReader(csv_file)
    fig =px.scatter (df,x= "coffee",y= "sleep")
    fig.show ()