import pandas as pd

df = pd.read_csv("Pokemon.csv", index_col=0)

# df.set_index("Tittle")
print(df.iloc[:5])
Attack = df.loc[df.Attack == 50]
print(Attack.head())

pd.Series()

pd.values_count
