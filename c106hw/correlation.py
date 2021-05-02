import plotly.express as px
import csv 
import numpy as np 

def getDataSource (data_path):
    RollNo = []
    Marks = []
    with open (data_path) as csv_file : 
        csv_reader  = csv.DictReader(csv_file)
        for row in csv_reader :
            RollNo.append (float(row["RollNo"]))
            Marks.append (float(row["Marks"]))

    return {"x":RollNo,"y":Marks}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print (correlation)

def setup():
    data_path ="C:\c106hw\Student Marks vs Days.csv"
    dataSource = getDataSource (data_path)
    findCorrelation (dataSource)

setup ()