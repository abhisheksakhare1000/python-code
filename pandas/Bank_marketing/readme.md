### List of Functions Used:

1. `pd.read_csv(url)`: Reads a CSV file from a specified URL.
2. `df.isnull().sum()`: Checks for missing values in the DataFrame.
3. `df.dropna(axis=1)`: Drops columns with missing values.
4. `df.dropna(inplace=True)`: Drops rows with missing values (in-place).
5. `df.fillna(value="sudh")`: Fills missing values with the string "sudh".
6. `df.fillna(value=df['Age'].mean())`: Fills missing values in the 'Age' column with the mean value.
7. `df.groupby('Survived').describe()['PassengerId'].transpose()`: Groups data, calculates statistics, and transposes the result.
8. `pd.concat([df2, df3])`: Concatenates DataFrames vertically.
9. `df2 = df2.set_index('age')`: Sets the 'age' column as the index for `df2`.
