import pandas as pd

CrimeData = pd.read_csv("crimedata.csv", header = none)
values = CrimeData.values.tolist()
print(values)

