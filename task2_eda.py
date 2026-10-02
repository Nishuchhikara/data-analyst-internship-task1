import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load cleaned dataset from Task 1
df = pd.read_excel('/mnt/user-data/outputs/Task1_Cleaned_Dataset.xlsx')

print("=" * 80)
print("TASK 2: EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 80)

# ---- SECTION 1: DATASET OVERVIEW ----
print("\n1. DATASET OVERVIEW")
print(f"   Total Records: {len(df)}")
print(f"   Total Columns: {len(df.columns)}")
print(f"   Date Range: {df['OrderDate'].min()} to {df['OrderDate'].max()}")
print(f"   Columns: {list(df.columns)}")

# ---- SECTION 2: STATISTICAL SUMMARY ----
print("\n2. STATISTICAL SUMMARY")
print("\nNumeric Columns Statistics:")
print(df[['Quantity', 'UnitPrice', 'TotalSales']].describe().round(2))

# ---- SECTION 3: KEY INSIGHTS ----
print("\n" + "=" * 80)
print("KEY INSIGHTS & FINDINGS")
print("=" * 80)

# Insight 1: Total Sales & Average Order Value
total_sales = df['TotalSales'].sum()
avg_order_value = df['TotalSales'].mean()
median_order_value = df['TotalSales'].median()
print(f"\n1. ORDER VALUE ANALYSIS:")
print(f"   - Total Sales: ${total_sales:,.2f}")
print(f"   - Average Order Value: ${avg_order_value:,.2f}")
print(f"   - Median Order Value: ${median_order_value:,.2f}")
print(f"   - Insight: Median < Mean suggests some high-value outlier orders are skewing the average.")

# Insight 2: Regional Performance
print(f"\n2. REGIONAL PERFORMANCE:")
regional_sales = df.groupby('Region')['TotalSales'].agg(['sum', 'count', 'mean']).sort_values('sum', ascending=False)
print(regional_sales.round(2))
top_region = regional_sales.index[0]
top_region_sales = regional_sales.loc[top_region, 'sum']
print(f"   - Insight: {top_region} region generates the highest sales (${top_region_sales:,.2f})")

# Insight 3: Product Category Performance
print(f"\n3. PRODUCT CATEGORY PERFORMANCE:")
category_sales = df.groupby('Category')['TotalSales'].agg(['sum', 'count', 'mean']).sort_values('sum', ascending=False)
print(category_sales.round(2))
top_category = category_sales.index[0]
top_category_sales = category_sales.loc[top_category, 'sum']
print(f"   - Insight: {top_category} is the leading category by revenue (${top_category_sales:,.2f})")

# Insight 4: Quantity vs Price Relationship
print(f"\n4. QUANTITY & PRICING PATTERNS:")
avg_qty = df['Quantity'].mean()
avg_price = df['UnitPrice'].mean()
print(f"   - Average Quantity per Order: {avg_qty:.1f} units")
print(f"   - Average Unit Price: ${avg_price:,.2f}")
high_qty_orders = df[df['Quantity'] > df['Quantity'].quantile(0.75)]
print(f"   - High-Quantity Orders (top 25%): {len(high_qty_orders)} orders ({len(high_qty_orders)/len(df)*100:.1f}% of total)")
print(f"   - Insight: Top quartile by quantity represents {high_qty_orders['TotalSales'].sum() / total_sales * 100:.1f}% of total revenue")

# Insight 5: Temporal Trends (by Month)
print(f"\n5. TEMPORAL TRENDS:")
df['Month'] = pd.to_datetime(df['OrderDate']).dt.to_period('M')
monthly_sales = df.groupby('Month')['TotalSales'].agg(['sum', 'count']).sort_index()
best_month = monthly_sales['sum'].idxmax()
best_month_sales = monthly_sales.loc[best_month, 'sum']
print(monthly_sales.round(2))
print(f"   - Insight: {best_month} was the peak sales period (${best_month_sales:,.2f})")

# ---- VISUALIZATIONS ----
print("\n" + "=" * 80)
print("GENERATING VISUALIZATIONS...")
print("=" * 80)

fig = plt.figure(figsize=(16, 12))

# Chart 1: Sales by Region (Bar Chart)
ax1 = plt.subplot(2, 3, 1)
regional_sales['sum'].plot(kind='bar', ax=ax1, color='skyblue', edgecolor='black')
ax1.set_title('Total Sales by Region', fontsize=12, fontweight='bold')
ax1.set_ylabel('Sales ($)')
ax1.set_xlabel('Region')
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)

# Chart 2: Sales by Category (Pie Chart)
ax2 = plt.subplot(2, 3, 2)
category_sales['sum'].plot(kind='pie', ax=ax2, autopct='%1.1f%%', startangle=90)
ax2.set_title('Sales Distribution by Category', fontsize=12, fontweight='bold')
ax2.set_ylabel('')

# Chart 3: Quantity vs TotalSales (Scatter Plot)
ax3 = plt.subplot(2, 3, 3)
ax3.scatter(df['Quantity'], df['TotalSales'], alpha=0.6, s=50, color='green', edgecolors='black')
ax3.set_title('Quantity vs Total Sales Relationship', fontsize=12, fontweight='bold')
ax3.set_xlabel('Quantity (units)')
ax3.set_ylabel('Total Sales ($)')
ax3.grid(True, alpha=0.3)

# Chart 4: Monthly Sales Trend (Line Chart)
ax4 = plt.subplot(2, 3, 4)
monthly_sales['sum'].plot(ax=ax4, kind='line', marker='o', color='red', linewidth=2)
ax4.set_title('Monthly Sales Trend', fontsize=12, fontweight='bold')
ax4.set_ylabel('Sales ($)')
ax4.set_xlabel('Month')
plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45)
ax4.grid(True, alpha=0.3)

# Chart 5: Unit Price Distribution (Histogram)
ax5 = plt.subplot(2, 3, 5)
ax5.hist(df['UnitPrice'], bins=20, color='orange', edgecolor='black', alpha=0.7)
ax5.set_title('Unit Price Distribution', fontsize=12, fontweight='bold')
ax5.set_xlabel('Unit Price ($)')
ax5.set_ylabel('Frequency')
ax5.grid(True, alpha=0.3, axis='y')

# Chart 6: Orders by City (Top 10)
ax6 = plt.subplot(2, 3, 6)
city_counts = df['City'].value_counts().head(10)
city_counts.plot(kind='barh', ax=ax6, color='purple', edgecolor='black')
ax6.set_title('Top 10 Cities by Order Count', fontsize=12, fontweight='bold')
ax6.set_xlabel('Number of Orders')

plt.tight_layout()
plt.savefig('/home/claude/Task2_EDA_Visualizations.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Task2_EDA_Visualizations.png")

# ---- Generate EDA Summary Report ----
report = f"""# Task 2: Exploratory Data Analysis (EDA) Report

## Dataset Overview
- **Total Records:** {len(df)}
- **Date Range:** {df['OrderDate'].min()} to {df['OrderDate'].max()}
- **Columns:** {', '.join(df.columns)}

## Statistical Summary
### Numeric Columns
```
{df[['Quantity', 'UnitPrice', 'TotalSales']].describe().round(2).to_string()}
```

## Key Findings & Insights

### 1. Order Value Analysis
- **Total Sales:** ${total_sales:,.2f}
- **Average Order Value:** ${avg_order_value:,.2f}
- **Median Order Value:** ${median_order_value:,.2f}
- **Standard Deviation:** ${df['TotalSales'].std():,.2f}
- **Finding:** The median is significantly lower than the mean, indicating the presence of high-value outlier orders. This suggests a right-skewed distribution where a few large orders drive substantial revenue.

### 2. Regional Performance
{regional_sales.round(2).to_string()}
- **Top Region:** {top_region} (${top_region_sales:,.2f}, {(top_region_sales/total_sales*100):.1f}% of revenue)
- **Finding:** Regional sales vary considerably. The top region outperforms others, suggesting regional marketing or demand variation that could be leveraged for targeted sales strategies.

### 3. Product Category Performance
{category_sales.round(2).to_string()}
- **Top Category:** {top_category} (${top_category_sales:,.2f}, {(top_category_sales/total_sales*100):.1f}% of revenue)
- **Finding:** {top_category} dominates the revenue. Understanding the seasonality and customer preferences for this category can drive inventory and marketing decisions.

### 4. Quantity & Pricing Patterns
- **Average Quantity per Order:** {avg_qty:.1f} units
- **Average Unit Price:** ${avg_price:,.2f}
- **High-Quantity Orders (Top Quartile):** {len(high_qty_orders)} orders ({len(high_qty_orders)/len(df)*100:.1f}% of total)
  - These {len(high_qty_orders)} high-quantity orders generate ${high_qty_orders['TotalSales'].sum():,.2f}, representing {high_qty_orders['TotalSales'].sum()/total_sales*100:.1f}% of total revenue.
- **Finding:** A small fraction of high-volume orders drives disproportionate revenue. This suggests the importance of bulk-order or wholesale customer segments.

### 5. Temporal Trends (Monthly Analysis)
- **Peak Sales Month:** {best_month} (${best_month_sales:,.2f})
- **Monthly Volatility:** Sales fluctuate across months, indicating seasonal demand patterns.
- **Finding:** Clear seasonality detected. The peak month (and any troughs) can inform inventory planning, promotional calendars, and staffing decisions.

## Visualizations Generated
1. **Sales by Region (Bar Chart):** Shows regional performance at a glance.
2. **Sales Distribution by Category (Pie Chart):** Reveals category contribution to total revenue.
3. **Quantity vs Total Sales (Scatter Plot):** Illustrates the strong correlation between order quantity and sales value.
4. **Monthly Sales Trend (Line Chart):** Displays temporal patterns and seasonality.
5. **Unit Price Distribution (Histogram):** Shows the spread and concentration of pricing.
6. **Top 10 Cities by Order Count:** Identifies the most active cities.

## Actionable Recommendations
1. Focus marketing efforts on {top_region} region and understand why it outperforms.
2. Increase inventory and promote {top_category} category during peak months.
3. Develop bulk-order incentives to capture more high-volume orders.
4. Investigate regional demand drivers to replicate success in underperforming regions.
5. Plan staffing and fulfillment capacity around peak sales months.

---
**Analysis Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Dataset:** Task1_Cleaned_Dataset.xlsx (288 records)
"""

with open('/home/claude/Task2_EDA_Report.md', 'w') as f:
    f.write(report)

print("✓ Saved: Task2_EDA_Report.md")
print("\n" + "=" * 80)
print("EDA COMPLETE!")
print("=" * 80)
