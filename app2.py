df.isnull()
df.notnull()

# Muestra los resultados donde nuestra columna esa vacia.
df[df["columna"].isnull()] 


#Drop  columns with non values
df.dropna()
# Drop columns with at least 1 value
df.dropna(thresh=1)


# Values with non value will be replace to "new value
df.fillna("new value")
