import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# =============================================================================
# AADHAR ENROLLMENT DATASET ANALYSIS - HISTOGRAM & HEATMAP VISUALIZATION
# =============================================================================

# Read Excel file
df = pd.read_excel(r'C:\Users\Asus\Desktop\TE\SEM 6\DS using Python LAB\EXP4\Sample_Aadhar_Enrollment_Dataset.xlsx')

print(f"\nDataFrame Shape: {df.shape[0]} rows × {df.shape[1]} columns")

print("\n" + "="*70)
print("DATASET INFORMATION")
print("="*70)
df.info()

# Calculate Total Enrollment
df['Total_Enrollment'] = df['age_0_5'].fillna(0) + df['age_5_17'].fillna(0) + df['age_18_greater'].fillna(0)

# =============================================================================
# HISTOGRAM VISUALIZATIONS
# =============================================================================
print("\n" + "="*70)
print("GENERATING HISTOGRAMS")
print("="*70)

# Create figure with subplots for comprehensive histogram analysis
fig = plt.figure(figsize=(16, 12))

# 1. Histogram for Age 0-5 Enrollments
ax1 = plt.subplot(3, 2, 1)
ax1.hist(df['age_0_5'].dropna(), bins=20, color='skyblue', edgecolor='black', alpha=0.7)
ax1.set_xlabel('Enrollment Count', fontsize=11, fontweight='bold')
ax1.set_ylabel('Frequency', fontsize=11, fontweight='bold')
ax1.set_title('Histogram: Age Group 0-5 Enrollments', fontsize=12, fontweight='bold')
ax1.grid(axis='y', alpha=0.3)
ax1.axvline(df['age_0_5'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["age_0_5"].mean():.2f}')
ax1.axvline(df['age_0_5'].median(), color='green', linestyle='--', linewidth=2, label=f'Median: {df["age_0_5"].median():.2f}')
ax1.legend()

# 2. Histogram for Age 5-17 Enrollments
ax2 = plt.subplot(3, 2, 2)
ax2.hist(df['age_5_17'].dropna(), bins=20, color='lightcoral', edgecolor='black', alpha=0.7)
ax2.set_xlabel('Enrollment Count', fontsize=11, fontweight='bold')
ax2.set_ylabel('Frequency', fontsize=11, fontweight='bold')
ax2.set_title('Histogram: Age Group 5-17 Enrollments', fontsize=12, fontweight='bold')
ax2.grid(axis='y', alpha=0.3)
ax2.axvline(df['age_5_17'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["age_5_17"].mean():.2f}')
ax2.axvline(df['age_5_17'].median(), color='green', linestyle='--', linewidth=2, label=f'Median: {df["age_5_17"].median():.2f}')
ax2.legend()

# 3. Histogram for Age 18+ Enrollments
ax3 = plt.subplot(3, 2, 3)
ax3.hist(df['age_18_greater'].dropna(), bins=20, color='lightgreen', edgecolor='black', alpha=0.7)
ax3.set_xlabel('Enrollment Count', fontsize=11, fontweight='bold')
ax3.set_ylabel('Frequency', fontsize=11, fontweight='bold')
ax3.set_title('Histogram: Age Group 18+ Enrollments', fontsize=12, fontweight='bold')
ax3.grid(axis='y', alpha=0.3)
ax3.axvline(df['age_18_greater'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["age_18_greater"].mean():.2f}')
ax3.axvline(df['age_18_greater'].median(), color='green', linestyle='--', linewidth=2, label=f'Median: {df["age_18_greater"].median():.2f}')
ax3.legend()

# 4. Histogram for Total Enrollment
ax4 = plt.subplot(3, 2, 4)
ax4.hist(df['Total_Enrollment'].dropna(), bins=25, color='gold', edgecolor='black', alpha=0.7)
ax4.set_xlabel('Enrollment Count', fontsize=11, fontweight='bold')
ax4.set_ylabel('Frequency', fontsize=11, fontweight='bold')
ax4.set_title('Histogram: Total Enrollments', fontsize=12, fontweight='bold')
ax4.grid(axis='y', alpha=0.3)
ax4.axvline(df['Total_Enrollment'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["Total_Enrollment"].mean():.2f}')
ax4.axvline(df['Total_Enrollment'].median(), color='green', linestyle='--', linewidth=2, label=f'Median: {df["Total_Enrollment"].median():.2f}')
ax4.legend()

# 5. Overlapping Histogram for Age Group Comparison
ax5 = plt.subplot(3, 2, 5)
ax5.hist(df['age_0_5'].dropna(), bins=15, color='skyblue', alpha=0.6, label='Age 0-5', edgecolor='black')
ax5.hist(df['age_5_17'].dropna(), bins=15, color='lightcoral', alpha=0.6, label='Age 5-17', edgecolor='black')
ax5.hist(df['age_18_greater'].dropna(), bins=15, color='lightgreen', alpha=0.6, label='Age 18+', edgecolor='black')
ax5.set_xlabel('Enrollment Count', fontsize=11, fontweight='bold')
ax5.set_ylabel('Frequency', fontsize=11, fontweight='bold')
ax5.set_title('Overlapping Histogram: Age Group Comparison', fontsize=12, fontweight='bold')
ax5.legend()
ax5.grid(axis='y', alpha=0.3)

# 6. Histogram with Cumulative Distribution
ax6 = plt.subplot(3, 2, 6)
n, bins, patches = ax6.hist(df['Total_Enrollment'].dropna(), bins=20, color='steelblue', 
                             edgecolor='black', alpha=0.7, label='Frequency')
# Add cumulative line
counts, bin_edges = np.histogram(df['Total_Enrollment'].dropna(), bins=20)
cumulative = np.cumsum(counts)
ax6_twin = ax6.twinx()
ax6_twin.plot(bin_edges[1:], cumulative, color='red', linewidth=2.5, marker='o', 
              markersize=4, label='Cumulative')
ax6.set_xlabel('Total Enrollment', fontsize=11, fontweight='bold')
ax6.set_ylabel('Frequency', fontsize=11, fontweight='bold', color='steelblue')
ax6_twin.set_ylabel('Cumulative Frequency', fontsize=11, fontweight='bold', color='red')
ax6.set_title('Histogram with Cumulative Distribution', fontsize=12, fontweight='bold')
ax6.grid(axis='y', alpha=0.3)
ax6.legend(loc='upper left')
ax6_twin.legend(loc='upper right')

plt.tight_layout()
plt.savefig('aadhar_enrollment_histograms.png', dpi=300, bbox_inches='tight')
print("✓ Saved: aadhar_enrollment_histograms.png")
plt.show()

# =============================================================================
# HISTOGRAM ANALYSIS SUMMARY
# =============================================================================
print("\n" + "="*70)
print("HISTOGRAM ANALYSIS SUMMARY")
print("="*70)

print("\n Total Enrollments:")
print(f"   - Mean: {df['Total_Enrollment'].mean():.2f}")
print(f"   - Median: {df['Total_Enrollment'].median():.2f}")
print(f"   - Std Dev: {df['Total_Enrollment'].std():.2f}")
print(f"   - Range: {df['Total_Enrollment'].min():.0f} to {df['Total_Enrollment'].max():.0f}")

print("\n" + "="*70)
print("KEY INSIGHTS FROM HISTOGRAMS:")
print("="*70)
print("• The histograms show the frequency distribution of enrollments")
print("• Age 5-17 group shows the highest enrollment counts on average")
print("• Red dashed line indicates mean, green dashed line indicates median")
print("• Most distributions show right-skewed patterns (positive skew)")
print("• Cumulative histogram helps understand enrollment accumulation")
print("\n" + "="*70)
print("HISTOGRAM GENERATION COMPLETE!")
print("="*70)

# =============================================================================
# CORRELATION HEATMAP VISUALIZATION
# =============================================================================
print("\n" + "="*70)
print("GENERATING CORRELATION HEATMAP")
print("="*70)

# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include=[np.number])

# Calculate correlation matrix
correlation_matrix = numeric_df.corr()

# Create heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, 
            annot=True,  # Show correlation values
            fmt='.3f',   # Format to 3 decimal places
            cmap='coolwarm',  # Color scheme (blue-white-red)
            center=0,    # Center the colormap at 0
            square=True,  # Make cells square-shaped
            linewidths=1,  # Add gridlines
            cbar_kws={'shrink': 0.8, 'label': 'Correlation Coefficient'})

plt.title('Correlation Heatmap: Aadhar Enrollment Dataset', 
          fontsize=14, fontweight='bold', pad=20)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(rotation=0, fontsize=10)
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
print("✓ Saved: correlation_heatmap.png")
plt.show()

# =============================================================================
# CORRELATION ANALYSIS SUMMARY
# =============================================================================
print("\n" + "="*70)
print("CORRELATION ANALYSIS SUMMARY")
print("="*70)

print("\nCorrelation Matrix:")
print(correlation_matrix)

print("\n" + "="*70)
print("KEY INSIGHTS FROM CORRELATION HEATMAP:")
print("="*70)
print("• Positive correlation (red): Variables increase together")
print("• Negative correlation (blue): One increases as other decreases")
print("• Values range from -1 (perfect negative) to +1 (perfect positive)")
print("• Values near 0 indicate weak or no linear relationship")

# Find strongest correlations (excluding diagonal)
print("\nStrongest Correlations:")
for i in range(len(correlation_matrix.columns)):
    for j in range(i+1, len(correlation_matrix.columns)):
        corr_value = correlation_matrix.iloc[i, j]
        if abs(corr_value) > 0.3:  # Only show correlations > 0.3
            print(f"  • {correlation_matrix.columns[i]} ↔ {correlation_matrix.columns[j]}: {corr_value:.3f}")

print("\n" + "="*70)
print("ALL VISUALIZATIONS COMPLETE!")
print("="*70)



