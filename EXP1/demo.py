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

print(" Dataset Information")
print(df.info())

print("Null or Missing Values")
print(df.isnull().sum())