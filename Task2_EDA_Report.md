# Task 2: Exploratory Data Analysis (EDA) Report

## Dataset Overview
- **Total Records:** 288
- **Date Range:** 2025-01-02 00:00:00 to 2025-10-28 00:00:00
- **Columns:** OrderID, CustomerName, OrderDate, Region, City, Category, Quantity, UnitPrice, TotalSales, Month

## Statistical Summary
### Numeric Columns
```
       Quantity  UnitPrice  TotalSales
count    288.00     288.00      288.00
mean      10.59     246.76     2615.24
std        5.57     131.46     2093.13
min        1.00      10.83       22.70
25%        5.00     146.97      969.24
50%       11.00     237.34     2121.51
75%       15.00     340.99     3713.49
max       20.00     499.69     9952.00
```

## Key Findings & Insights

### 1. Order Value Analysis
- **Total Sales:** $753,189.71
- **Average Order Value:** $2,615.24
- **Median Order Value:** $2,121.51
- **Standard Deviation:** $2,093.13
- **Finding:** The median is significantly lower than the mean, indicating the presence of high-value outlier orders. This suggests a right-skewed distribution where a few large orders drive substantial revenue.

### 2. Regional Performance
               sum  count     mean
Region                            
South    232616.83     90  2584.63
North    226418.37     78  2902.80
East     176545.46     70  2522.08
West      87420.93     34  2571.20
Unknown   30188.12     16  1886.76
- **Top Region:** South ($232,616.83, 30.9% of revenue)
- **Finding:** Regional sales vary considerably. The top region outperforms others, suggesting regional marketing or demand variation that could be leveraged for targeted sales strategies.

### 3. Product Category Performance
                   sum  count     mean
Category                              
Electronics  249194.53     95  2623.10
Furniture    241457.93     93  2596.32
Groceries    135377.71     56  2417.46
Clothing     127159.54     44  2889.99
- **Top Category:** Electronics ($249,194.53, 33.1% of revenue)
- **Finding:** Electronics dominates the revenue. Understanding the seasonality and customer preferences for this category can drive inventory and marketing decisions.

### 4. Quantity & Pricing Patterns
- **Average Quantity per Order:** 10.6 units
- **Average Unit Price:** $246.76
- **High-Quantity Orders (Top Quartile):** 66 orders (22.9% of total)
  - These 66 high-quantity orders generate $295,224.84, representing 39.2% of total revenue.
- **Finding:** A small fraction of high-volume orders drives disproportionate revenue. This suggests the importance of bulk-order or wholesale customer segments.

### 5. Temporal Trends (Monthly Analysis)
- **Peak Sales Month:** 2025-08 ($108,417.43)
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
1. Focus marketing efforts on South region and understand why it outperforms.
2. Increase inventory and promote Electronics category during peak months.
3. Develop bulk-order incentives to capture more high-volume orders.
4. Investigate regional demand drivers to replicate success in underperforming regions.
5. Plan staffing and fulfillment capacity around peak sales months.

---
**Analysis Date:** 2026-10-02 06:37:23
**Dataset:** Task1_Cleaned_Dataset.xlsx (288 records)
