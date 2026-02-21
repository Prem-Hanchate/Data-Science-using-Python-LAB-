import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# Bar Chart Visualization
print("\n" + "="*50)
print("Generating Bar Charts...")
print("="*50)

# 1. Grouped Bar Chart: Enrollments by State and Age Group
state_enrollments = df.groupby('State')[['age_0_5', 'age_5_17', 'age_18_greater']].sum()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Grouped Bar Chart
x = np.arange(len(state_enrollments.index))
width = 0.25

bars1 = ax1.bar(x - width, state_enrollments['age_0_5'], width, label='Age 0-5', color='skyblue')
bars2 = ax1.bar(x, state_enrollments['age_5_17'], width, label='Age 5-17', color='lightcoral')
bars3 = ax1.bar(x + width, state_enrollments['age_18_greater'], width, label='Age 18+', color='lightgreen')

ax1.set_xlabel('State', fontsize=12, fontweight='bold')
ax1.set_ylabel('Total Enrollments', fontsize=12, fontweight='bold')
ax1.set_title('Aadhar Enrollments by State and Age Group', fontsize=14, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(state_enrollments.index, rotation=45, ha='right')
ax1.legend()
ax1.grid(axis='y', alpha=0.3)

# Stacked Bar Chart
ax2.bar(state_enrollments.index, state_enrollments['age_0_5'], label='Age 0-5', color='skyblue')
ax2.bar(state_enrollments.index, state_enrollments['age_5_17'], bottom=state_enrollments['age_0_5'], 
        label='Age 5-17', color='lightcoral')
ax2.bar(state_enrollments.index, state_enrollments['age_18_greater'], 
        bottom=state_enrollments['age_0_5'] + state_enrollments['age_5_17'], 
        label='Age 18+', color='lightgreen')

ax2.set_xlabel('State', fontsize=12, fontweight='bold')
ax2.set_ylabel('Total Enrollments', fontsize=12, fontweight='bold')
ax2.set_title('Stacked Aadhar Enrollments by State', fontsize=14, fontweight='bold')
ax2.set_xticklabels(state_enrollments.index, rotation=45, ha='right')
ax2.legend()
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

# 2. Simple Bar Chart: Top 10 Districts by Total Enrollment
df['Total_Enrollment'] = df['age_0_5'].fillna(0) + df['age_5_17'].fillna(0) + df['age_18_greater'].fillna(0)
top_districts = df.groupby('district')['Total_Enrollment'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
bars = plt.bar(range(len(top_districts)), top_districts.values, color='steelblue', edgecolor='black')
plt.xlabel('District', fontsize=12, fontweight='bold')
plt.ylabel('Total Enrollments', fontsize=12, fontweight='bold')
plt.title('Top 10 Districts by Total Aadhar Enrollments', fontsize=14, fontweight='bold')
plt.xticks(range(len(top_districts)), top_districts.index, rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)

# Add value labels on bars
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()

print("\nBar charts displayed successfully!")    