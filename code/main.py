# imports
import pandas as pd
import numpy as np
import matplotlib as mp
import seaborn as sb
import sklearn as sk

# opening and reading data from excel file (or) CSV file
df = pd.read_excel("datasets/bf3_data_2022_01_07.xlsx")
print(df)
d =  pd.read_csv("datasets/bf3_data_2022_01_07.csv")
print(d)
d.head()