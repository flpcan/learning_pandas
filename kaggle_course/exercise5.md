1.¶

What is the data type of the points column in the dataset?


dtype = reviews.points.dtype




2.

Create a Series from entries in the points column, but convert the entries to strings. Hint: strings are str in native Python.


point_strings = reviews.points.astype("str")



3.

Sometimes the price column is null. How many reviews in the dataset are missing a price?

n_missing_prices = reviews.price.isnull().sum()




4.

What are the most common wine-producing regions? Create a Series counting the number of times each value occurs in the region_1 field. This field is often missing data, so replace missing values with Unknown. Sort in descending order. Your output should look something like this:

reviews_per_region = reviews.region_1.fillna("Unknown").value_counts()

