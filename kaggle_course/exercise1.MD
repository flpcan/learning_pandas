1.

In the cell below, create a DataFrame fruits that looks like this:

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruits = pd.DataFrame({ "Apples" : [30], "Bananas" : [21]})

# Check your answer
q1.check()
fruits


2.¶

Create a dataframe fruit_sales that matches the diagram below:

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.
fruit_sales = pd.DataFrame({"Apples" : [35,41], "Bananas" : [21,34]}, index=["2017 Sales", "2018 Sales"])


# Check your answer
q2.check()
fruit_sales


3.¶

Create a variable ingredients with a Series that looks like:

Flour     4 cups
Milk       1 cup
Eggs     2 large
Spam       1 can
Name: Dinner, dtype: object



ingredients = pd.Series(["4 cups","1 cup", "2 large","1 can"],index=["Flour", "Milk", "Eggs", "Spam"], name="Dinner")

# Check your answer
q3.check()
ingredients


4.

Read the following csv dataset of wine reviews into a DataFrame called reviews:

Image

The filepath to the csv file is ../input/wine-reviews/winemag-data_first150k.csv. The first few lines look like:

,country,description,designation,points,price,province,region_1,region_2,variety,winery
0,US,"This tremendous 100% varietal wine[...]",Martha's Vineyard,96,235.0,California,Napa Valley,Napa,Cabernet Sauvignon,Heitz
1,Spain,"Ripe aromas of fig, blackberry and[...]",Carodorum Selección Especial Reserva,96,110.0,Northern Spain,Toro,,Tinta de Toro,Bodega Carmen Rodríguez

reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv", index_col=0)

# Check your answer
q4.check()
reviews


5.

Run the cell below to create and display a DataFrame called animals:


animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals
