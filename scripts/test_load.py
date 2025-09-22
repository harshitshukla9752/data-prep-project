import pandas as pd

# CSV load
df = pd.read_csv(r"C:\Users\harsh\data-prep-project\data\titanic.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
