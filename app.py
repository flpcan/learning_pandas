import pandas as pd


df = pd.read_csv("Pokemon.csv")

# print(df.head(3))

# If we have xlsx file we can read with:
# df_xlsx = pd.read_excel('pokemon_data.xlsx')


# Read headers
# print(df.columns)

# Read each columns
# print(df["Name"])
# print(df[["Name","Type 1", "HP"]])

# Read each row
# Print first row
# print(df.iloc[0])
# print(df.iloc[0:4])
# for index, row in df.iterrows():
#     print(index,row)
# print(df.loc[df["Type 1"] == "Grass"])


# Read a specific location (R,C)
# print(df.iloc[2,1])


# Add a new column like total
# df["Total"] = df["HP"] + df["Attack"] + df["Defense"] + df["Sp. Atk"] + df["Sp. Def"] + df["Speed"]
# df.head(5)

# Drop column
# df = df.drop(columns=["Total"])

# df['Total'] = df.iloc[:,4:10].sum(axis=1)
# print(df.head(5))


# Save files
# df.to_csv("modified.csv", index=False)
# df.to_excel("modified.xlsx", index=False)
# df.to_csv("modified.txt", index=False,sep="\t")


# Filtering Data
# new_df = df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison") & (df["HP"] > 70)]
# new_df.to_csv("filtered.csv")
# new_df = new_df.reset_index(drop=True, inplace=True)

# Conditionals changes
# df.loc[df["Type 1"] == "Fire", "Legendary"] = True

# aggregate stadistics
# x = df.groupby(["Type 1"]).mean().sort_values("Defense", ascending = False)
# print(x)

# df.groupby(["Type 1"]).sum()

# df["count"] = 1
# x = df.groupby(["Type 1", "Type 2"]).count()["count"]
# print(x)

# Working with large amounts of dataset
# df = read_csv("Pokemon", chunksize=5)
# Reduce the data size
