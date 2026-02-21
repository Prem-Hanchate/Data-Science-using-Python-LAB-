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
plt.savefig('bar_charts_by_state.png', dpi=300, bbox_inches='tight')
print("✓ Saved: bar_charts_by_state.png")
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
plt.savefig('top_10_districts_bar_chart.png', dpi=300, bbox_inches='tight')
print("✓ Saved: top_10_districts_bar_chart.png")
plt.show()

print("\nBar charts displayed successfully!")

# Box Plot Visualization
print("\n" + "="*50)
print("Generating Box Plots...")
print("="*50)

# 1. Box Plot: Distribution of Enrollments by Age Groups
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Box plot for age group distributions
age_data = [df['age_0_5'].dropna(), df['age_5_17'].dropna(), df['age_18_greater'].dropna()]
bp1 = ax1.boxplot(age_data, labels=['Age 0-5', 'Age 5-17', 'Age 18+'], 
                   patch_artist=True, notch=True, showmeans=True)

# Customize box colors
colors = ['skyblue', 'lightcoral', 'lightgreen']
for patch, color in zip(bp1['boxes'], colors):
    patch.set_facecolor(color)

ax1.set_xlabel('Age Groups', fontsize=12, fontweight='bold')
ax1.set_ylabel('Enrollment Count', fontsize=12, fontweight='bold')
ax1.set_title('Distribution of Aadhar Enrollments by Age Group', fontsize=14, fontweight='bold')
ax1.grid(axis='y', alpha=0.3)

# Box plot for enrollment distribution by state
states = df['State'].dropna().unique()
state_data = []
state_labels = []

for state in states:
    state_df = df[df['State'] == state]
    total_enrollments = state_df['Total_Enrollment'].dropna()
    if len(total_enrollments) > 0:
        state_data.append(total_enrollments)
        state_labels.append(state)

bp2 = ax2.boxplot(state_data, labels=state_labels, patch_artist=True, showmeans=True)

# Customize box colors with gradient
colors2 = plt.cm.viridis(np.linspace(0, 1, len(bp2['boxes'])))
for patch, color in zip(bp2['boxes'], colors2):
    patch.set_facecolor(color)

ax2.set_xlabel('State', fontsize=12, fontweight='bold')
ax2.set_ylabel('Total Enrollment', fontsize=12, fontweight='bold')
ax2.set_title('Distribution of Total Enrollments by State', fontsize=14, fontweight='bold')
ax2.set_xticklabels(state_labels, rotation=45, ha='right')
ax2.grid(axis='y', alpha=0.3)
    
plt.tight_layout()
plt.savefig('box_plots_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Saved: box_plots_distribution.png")
plt.show()

# 2. Single Box Plot: Overall Enrollment Distribution
plt.figure(figsize=(10, 6))

# Prepare data for all age groups combined
all_ages_data = [
    df['age_0_5'].dropna().values,
    df['age_5_17'].dropna().values,
    df['age_18_greater'].dropna().values,
    df['Total_Enrollment'].dropna().values
]

bp3 = plt.boxplot(all_ages_data, labels=['Age 0-5', 'Age 5-17', 'Age 18+', 'Total'], 
                   patch_artist=True, notch=True, showmeans=True,
                   meanprops=dict(marker='D', markerfacecolor='red', markersize=8))

# Customize colors
box_colors = ['skyblue', 'lightcoral', 'lightgreen', 'gold']
for patch, color in zip(bp3['boxes'], box_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

plt.xlabel('Enrollment Categories', fontsize=12, fontweight='bold')
plt.ylabel('Count', fontsize=12, fontweight='bold')
plt.title('Box Plot: Aadhar Enrollment Distribution Analysis\n(Shows Median, Quartiles, and Outliers)', 
          fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('box_plot_overall_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Saved: box_plot_overall_analysis.png")
plt.show()

print("\nBox plots displayed successfully!")
print("\nBox Plot Insights:")
print("- The box shows the interquartile range (IQR) - middle 50% of data")
print("- The line inside the box is the median")
print("- The diamond marker shows the mean")
print("- Whiskers extend to 1.5 × IQR")
print("- Points beyond whiskers are potential outliers")

print("\n" + "="*50)
print("ALL PLOTS SAVED SUCCESSFULLY!")
print("="*50)
print("\nSaved Files:")
print("1. bar_charts_by_state.png")
print("2. top_10_districts_bar_chart.png")
print("3. box_plots_distribution.png")
print("4. box_plot_overall_analysis.png")
print("\nYou can now view all plots as image files in the current directory.")
print("Simply close each plot window as it appears to continue.")
