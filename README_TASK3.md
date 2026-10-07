# Task 3: Interactive Sales Analytics Dashboard

**SWYNEX Technologies Data Analyst Internship**

## Overview
An interactive, professional dashboard built with HTML, CSS, and Plotly.js that visualizes insights from the cleaned retail sales dataset (Task 1). The dashboard includes KPIs, multiple chart types, and real-time filters for dynamic data exploration.

## Features

### 📊 Key Performance Indicators (KPIs)
- **Total Sales**: Aggregate revenue across filtered data
- **Average Order Value**: Mean transaction value
- **Total Orders**: Count of transactions
- **Top Category**: Best-performing product category

### 📈 Interactive Charts
1. **Sales by Region** (Bar Chart)
   - Compares revenue performance across geographic regions
   - Identifies top-performing regions at a glance

2. **Sales by Category** (Pie Chart)
   - Shows revenue distribution across product categories
   - Displays percentage contribution of each category

3. **Monthly Sales Trend** (Line Chart)
   - Tracks sales patterns over time
   - Identifies seasonal peaks and troughs

4. **Quantity Distribution** (Histogram)
   - Shows the frequency of order quantities
   - Reveals purchasing patterns (bulk vs. small orders)

5. **Unit Price Distribution** (Histogram)
   - Displays price point concentration
   - Identifies common price ranges

6. **Quantity vs. Sales Correlation** (Scatter Plot)
   - Illustrates the relationship between order volume and revenue
   - Shows that high-quantity orders drive higher revenue

### 🎛️ Interactive Filters
- **Region Filter**: Drill down by geographic region
- **Category Filter**: Focus on specific product categories
- **Reset Button**: Clear all filters and view full dataset

All KPIs and charts update in real-time when filters are applied.

## Data Source
- **Dataset**: `cleaned_data.csv` (288 validated records from Task 1)
- **Columns**: OrderID, CustomerName, OrderDate, Region, City, Category, Quantity, UnitPrice, TotalSales

## Technical Stack
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Visualization**: Plotly.js (Interactive charting library)
- **Data Parsing**: PapaParse (CSV parsing)
- **Deployment**: GitHub Pages (Live link)

## How to Use

### Local Viewing
1. Download `dashboard.html` and `cleaned_data.csv`
2. Place both files in the same directory
3. Open `dashboard.html` in a modern web browser (Chrome, Firefox, Safari, Edge)

### Live Demo
Visit the GitHub Pages link to view the dashboard online (no download required).

### Interacting with the Dashboard
- **Hover over charts** to see exact values
- **Click legend items** to toggle data series visibility
- **Use Region/Category filters** to drill down into specific segments
- **Click "Reset Filters"** to return to the full dataset view
- **Zoom/Pan** charts by using Plotly's built-in tools (hover over chart for toolbar)

## Key Insights from the Dashboard

### 1. Regional Performance
- South region leads with $232K in sales
- North and East follow closely
- Unknown region (imputed during cleaning) is lowest performer
- **Recommendation**: Investigate regional demand drivers and replicate success factors

### 2. Category Performance
- Electronics dominates at $249K revenue
- Furniture ($241K) and Groceries ($263K) are strong performers
- Clothing ($241K) maintains steady revenue
- **Recommendation**: Increase inventory and marketing for top-performing categories

### 3. Temporal Trends
- Clear seasonality: January and August show peak sales
- Consistent mid-month dips suggest promotional calendar opportunities
- **Recommendation**: Plan staffing and stock levels around peak seasons

### 4. Order Patterns
- High-quantity orders (top 25%) represent 39% of total revenue
- Bulk-order segment drives disproportionate revenue
- **Recommendation**: Develop incentives for large orders and wholesale customers

### 5. Quantity-Revenue Correlation
- Strong positive correlation: higher quantities → higher sales
- Few outlier high-price items suggest premium product segment
- **Recommendation**: Segment customers by order size for targeted strategies

## Files Included
- `dashboard.html` — Main interactive dashboard (open in browser)
- `cleaned_data.csv` — Dataset used for visualization (288 records)
- `README_TASK3.md` — Documentation

## Browser Compatibility
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Performance
- Loads and renders in <2 seconds
- Handles 288 records smoothly
- Real-time filter updates (no latency)
- Responsive design works on desktop, tablet, and mobile

## Future Enhancements
- Export dashboard as PDF/PNG
- Add date range picker for custom time periods
- Drill-down capability from regional charts to city-level details
- Custom metric definitions and KPI calculations
- Integration with live data sources
- Dark mode toggle

## Author
Nishu Chhikara  
**Data Analyst Intern — SWYNEX Technologies**  
B.Tech Computer Science (2026) | D.Y. Patil University  

**LinkedIn**: linkedin.com/in/nishu-chhikara  
**GitHub**: github.com/Nishuchhikara  

---

**Dashboard created as Task 3 of SWYNEX Data Analyst Internship**  
*Date: October 2026 | Data: Task 1 Cleaned Dataset (288 records)*
