import pandas as pd

# Read Excel file
df = pd.read_excel(r'C:\Users\Asus\Desktop\TE\SEM 6\DS using Python LAB\EXP1\Sample_Aadhar_Enrollment_Dataset.xlsx')

print(df.head())

dataframe_shape = df.shape

print(f"DataFrame shape (rows, columns): {dataframe_shape}")
print(f"Number of rows: {dataframe_shape[0]}")
print(f"Number of columns: {dataframe_shape[1]}")

print("\nDescriptive Summary:")
print(df.describe())

print("\nDataset Information")
df.info()

print("\nNull or Missing Values Before Handling")
print(df.isnull().sum())

# Handle Missing Values using Mean
df.fillna(df.mean(numeric_only=True), inplace=True) 

print("\nNull or Missing Values After Handling")
print(df.isnull().sum())
