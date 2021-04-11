import pandas as pd
import numpy
import csv

df = pd.read_csv('jeopardy_small.csv')

# print(df.head(5))
# print(df.info())

df['words in question'] = df.apply(lambda row : True if all(x in row.Question for x in ["Galileo","life"]) else False,axis=1)


df["Float Value"] = df["Value"].apply(lambda x: float(x[1:]) if x != "None" else 0)