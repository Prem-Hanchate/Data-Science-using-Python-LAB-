import pandas as pd
import numpy as np

print("=" * 80)
print("Experiment No: 3 - EXPLORING PANDAS LIBRARY")
print("Sample Aadhar Enrollment Dataset")
print("=" * 80)

# ============================================================================
# 1. DATA CREATION AND I/O
# ============================================================================
print("\n" + "=" * 80)
print("1. DATA CREATION AND I/O")
print("=" * 80)

# Read existing Excel file using pd.read_excel()
print("\n--- pd.read_excel() - Reading Excel file ---")
df = pd.read_excel('Sample_Aadhar_Enrollment_Dataset.xlsx')
print("✓ Excel file loaded successfully!")
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# Save to CSV using df.to_csv()
print("\n--- df.to_csv() - Saving to CSV format ---")
df.to_csv('Aadhar_Enrollment_Data.csv', index=False)
print("✓ Data saved to 'Aadhar_Enrollment_Data.csv'")

# Read from CSV using pd.read_csv()
print("\n--- pd.read_csv() - Reading from CSV ---")
df_read = pd.read_csv('Aadhar_Enrollment_Data.csv')
print("✓ Data read from CSV file successfully!")
print(f"Shape: {df_read.shape}")

# Save to Excel using df.to_excel()
print("\n--- df.to_excel() - Saving to Excel format ---")
df.to_excel('Aadhar_Enrollment_Output.xlsx', index=False, sheet_name='Enrollments')
print("✓ Data saved to 'Aadhar_Enrollment_Output.xlsx'")

# ============================================================================
# 2. DATA VIEWING AND INSPECTION
# ============================================================================
print("\n" + "=" * 80)
print("2. DATA VIEWING AND INSPECTION")
print("=" * 80)

# Display first few rows
print("\n--- df.head() - First 5 rows ---")
print(df.head())

# Display last few rows
print("\n--- df.tail(3) - Last 3 rows ---")
print(df.tail(3))

# Display DataFrame information
print("\n--- df.info() - DataFrame Information ---")
print(df.info())

# Display statistical summary
print("\n--- df.describe() - Statistical Summary ---")
print(df.describe())

# Display shape
print(f"\n--- df.shape - Shape of DataFrame ---")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Display column names
print(f"\n--- df.columns - Column Names ---")
print(df.columns.tolist())

# ============================================================================
# 3. DATA CLEANING AND PREPROCESSING
# ============================================================================
print("\n" + "=" * 80)
print("3. DATA CLEANING AND PREPROCESSING")
print("=" * 80)

# Check for missing values using df.isnull()
print("\n--- df.isnull() - Detecting Missing Values ---")
print(df.isnull().sum())

# Check for non-missing values using df.notnull()
print("\n--- df.notnull().sum() - Detecting Non-Missing Values ---")
print(df.notnull().sum())

# Show rows with missing values
print("\n--- Rows with Missing Values ---")
print(df[df.isnull().any(axis=1)])

# Create a copy for cleaning operations
df_cleaned = df.copy()

# Fill missing values in numeric columns with mean using df.fillna()
print("\n--- df.fillna() - Filling Missing Numeric Values with Mean ---")
numeric_cols = df_cleaned.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    if df_cleaned[col].isnull().sum() > 0:
        mean_val = df_cleaned[col].mean()
        df_cleaned[col].fillna(mean_val, inplace=True)
        print(f"✓ {col}: filled {df[col].isnull().sum()} missing values with mean ({mean_val:.2f})")

# Fill missing values in text columns with a placeholder
print("\n--- Filling Missing Text Values ---")
text_cols = df_cleaned.select_dtypes(include=['object']).columns
for col in text_cols:
    if df_cleaned[col].isnull().sum() > 0:
        df_cleaned[col].fillna('Not Provided', inplace=True)
        print(f"✓ {col}: filled {df[col].isnull().sum()} missing values with 'Not Provided'")

# Display after filling
print("\nMissing values after cleaning:")
print(df_cleaned.isnull().sum())

# Add duplicate rows for demonstration
df_with_duplicates = pd.concat([df_cleaned, df_cleaned.iloc[[0, 1]]], ignore_index=True)
print(f"\n--- Added duplicate rows ---")
print(f"Shape before removing duplicates: {df_with_duplicates.shape}")

# Remove duplicates using df.drop_duplicates()
df_no_duplicates = df_with_duplicates.drop_duplicates()
print(f"Shape after removing duplicates: {df_no_duplicates.shape}")

# Using df.replace() to replace values
print("\n--- df.replace() - Replacing Values ---")
# Find a categorical column to demonstrate replacement
if len(text_cols) > 0:
    sample_col = text_cols[0]
    unique_vals = df_cleaned[sample_col].unique()
    if len(unique_vals) > 1:
        old_val = unique_vals[0]
        new_val = f"{old_val}_Updated"
        df_cleaned[sample_col] = df_cleaned[sample_col].replace(old_val, new_val)
        print(f"✓ Replaced '{old_val}' with '{new_val}' in column '{sample_col}'")
        print(f"Value counts after replacement:")
        print(df_cleaned[sample_col].value_counts())

# ============================================================================
# 4. DATA MANIPULATION AND TRANSFORMATION (User-Defined Functions)
# ============================================================================
print("\n" + "=" * 80)
print("4. DATA MANIPULATION AND TRANSFORMATION")
print("=" * 80)

# Create a fresh copy for manipulation
df_transform = df_cleaned.copy()

# Get numeric and text columns for transformations
numeric_cols_transform = df_transform.select_dtypes(include=[np.number]).columns
text_cols_transform = df_transform.select_dtypes(include=['object']).columns

# User-defined function 1: Categorize numeric values
def categorize_numeric(value):
    """Categorizes numeric values into Low, Medium, High"""
    if pd.isna(value):
        return 'Unknown'
    elif value < 30:
        return 'Low'
    elif value < 60:
        return 'Medium'
    else:
        return 'High'

# Apply user-defined function using df.apply()
if len(numeric_cols_transform) > 0:
    sample_numeric_col = numeric_cols_transform[0]
    print(f"\n--- df.apply() - Applying User-Defined Function to '{sample_numeric_col}' ---")
    new_col_name = f'{sample_numeric_col}_Category'
    df_transform[new_col_name] = df_transform[sample_numeric_col].apply(categorize_numeric)
    print(df_transform[[sample_numeric_col, new_col_name]].head(10))

# User-defined function 3: Generate custom codes
def generate_code(value):
    """Generates a custom code based on value"""
    if pd.isna(value):
        return 'UNK'
    value_str = str(value)
    return value_str[:3].upper() if len(value_str) >= 3 else value_str.upper()

if len(text_cols_transform) > 1:
    sample_col_code = text_cols_transform[1] if len(text_cols_transform) > 1 else text_cols_transform[0]
    print(f"\n--- Custom Code Generation for '{sample_col_code}' ---")
    code_col_name = f'{sample_col_code}_Code'
    df_transform[code_col_name] = df_transform[sample_col_code].apply(generate_code)
    print(df_transform[[sample_col_code, code_col_name]].head())

# Sort values using df.sort_values()
if len(numeric_cols_transform) > 0:
    sort_col = numeric_cols_transform[0]
    print(f"\n--- df.sort_values() - Sorting by '{sort_col}' ---")
    df_sorted = df_transform.sort_values(by=sort_col, ascending=False)
    display_cols = [sort_col] + list(text_cols_transform[:2]) if len(text_cols_transform) >= 2 else [sort_col]
    print(df_sorted[display_cols].head())

# Create pivot table using pd.pivot_table()
print("\n--- pd.pivot_table() - Creating Pivot Table ---")
if len(text_cols_transform) >= 2 and len(numeric_cols_transform) > 0:
    pivot_row = text_cols_transform[0]
    pivot_col = text_cols_transform[1]
    pivot_val = numeric_cols_transform[0]
    
    try:
        pivot_table = pd.pivot_table(df_cleaned, 
                                      values=pivot_val, 
                                      index=pivot_row, 
                                      columns=pivot_col, 
                                      aggfunc='mean', 
                                      fill_value=0)
        print(f"Pivot Table: {pivot_val} by {pivot_row} (rows) and {pivot_col} (columns)")
        print(pivot_table)
    except Exception as e:
        print(f"Pivot table creation skipped: {str(e)[:100]}")
else:
    print("Pivot table skipped - insufficient columns")

# ============================================================================
# 5. GROUPING AND AGGREGATION
# ============================================================================
print("\n" + "=" * 80)
print("5. GROUPING AND AGGREGATION")
print("=" * 80)

# Get columns for grouping
group_cols = df_cleaned.select_dtypes(include=['object']).columns
numeric_agg_cols = df_cleaned.select_dtypes(include=[np.number]).columns

# Group by first categorical column using df.groupby()
if len(group_cols) > 0 and len(numeric_agg_cols) > 0:
    group_col_1 = group_cols[0]
    print(f"\n--- df.groupby() - Grouping by '{group_col_1}' ---")
    groups = df_cleaned.groupby(group_col_1)
    print(f"Number of groups: {len(groups)}")
    print(f"Group keys: {list(groups.groups.keys())[:5]}")  # Show first 5 groups
    
    # Count by group
    print(f"\n--- df.count() - Count by '{group_col_1}' ---")
    count_result = df_cleaned.groupby(group_col_1)[numeric_agg_cols[0]].count()
    print(count_result)
    
    # Calculate sum using df.sum()
    if len(numeric_agg_cols) > 0:
        print(f"\n--- df.sum() - Sum of '{numeric_agg_cols[0]}' by '{group_col_1}' ---")
        sum_result = df_cleaned.groupby(group_col_1)[numeric_agg_cols[0]].sum()
        print(sum_result)
    
    # Multiple aggregations using df.agg()
    print(f"\n--- df.agg() - Multiple Aggregations by '{group_col_1}' ---")
    agg_dict = {}
    for col in numeric_agg_cols[:2]:  # First 2 numeric columns
        agg_dict[col] = ['mean', 'sum', 'count']
    
    agg_result = df_cleaned.groupby(group_col_1).agg(agg_dict)
    print(agg_result)
    
    # Group by second categorical column if available
    if len(group_cols) > 1:
        group_col_2 = group_cols[1]
        print(f"\n--- Aggregation by '{group_col_2}' ---")
        agg_result_2 = df_cleaned.groupby(group_col_2).agg({
            numeric_agg_cols[0]: ['mean', 'sum', 'count']
        })
        print(agg_result_2)
    
    # Group by multiple columns
    if len(group_cols) >= 2:
        print(f"\n--- df.groupby() - Grouping by Multiple Columns ('{group_col_1}', '{group_col_2}') ---")
        multi_group = df_cleaned.groupby([group_col_1, group_col_2]).agg({
            numeric_agg_cols[0]: ['count', 'mean']
        })
        print(multi_group)

else:
    print("\n--- Grouping operations skipped - insufficient columns ---")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
print("\n✓ All pandas operations completed successfully!")
print(f"\nDataset Statistics:")
print(f"  • Total records: {len(df)}")
print(f"  • Total columns: {len(df.columns)}")
print(f"  • Numeric columns: {len(df.select_dtypes(include=[np.number]).columns)}")
print(f"  • Text columns: {len(df.select_dtypes(include=['object']).columns)}")
print(f"  • Memory usage: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")

print("\nOperations demonstrated:")
print("  ✓ Data Creation and I/O")
print("      - pd.read_excel(), pd.read_csv(), df.to_csv(), df.to_excel()")
print("  ✓ Data Viewing and Inspection")
print("      - head(), tail(), info(), describe(), shape, columns, dtypes")
print("      - unique(), value_counts()")
print("  ✓ Data Cleaning and Preprocessing")
print("      - isnull(), notnull(), fillna(), drop_duplicates(), replace()")
print("  ✓ Data Manipulation with User-Defined Functions")
print("      - apply(), sort_values(), pivot_table()")
print("      - 3 custom user-defined functions applied")
print("  ✓ Grouping and Aggregation")
print("      - groupby(), agg(), mean(), sum(), count()")
print("=" * 80)
