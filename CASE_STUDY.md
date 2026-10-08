# Retail Sales Analytics: Complete Case Study
## SWYNEX Technologies Data Analyst Internship - Final Project

**Author:** Nishu Chhikara  
**Date:** October 2026  
**Duration:** 4-Week Project  
**Dataset:** Retail Sales (288 validated records)

---

## Executive Summary

This comprehensive case study demonstrates an end-to-end data analytics workflow applied to a retail sales dataset. The project showcases the complete lifecycle of data analysis: from raw data through cleaning, exploratory analysis, dashboard development, and actionable business insights.

**Key Metrics:**
- 288 validated records analyzed
- $753,045 total sales analyzed
- 6 interactive visualizations created
- 5+ actionable business insights derived
- 100% data quality achieved

---

## Table of Contents

1. [Problem Statement](#problem-statement)
2. [Dataset Overview](#dataset-overview)
3. [Data Cleaning Process](#data-cleaning-process)
4. [Exploratory Data Analysis](#exploratory-data-analysis)
5. [Interactive Dashboard](#interactive-dashboard)
6. [Key Business Insights](#key-business-insights)
7. [Recommendations](#recommendations)
8. [Technical Stack](#technical-stack)
9. [Project Structure](#project-structure)

---

## Problem Statement

### Business Challenge
A retail organization was struggling with:
- **Incomplete data quality** — missing values, duplicates, inconsistent formatting
- **Lack of visibility** — no clear understanding of sales patterns across regions and categories
- **Inefficient decision-making** — decisions based on incomplete or unreliable data
- **Untapped opportunities** — failure to identify high-performing segments and seasonal trends

### Project Objective
Develop a complete data analytics solution that:
1. Transforms raw data into a clean, validated dataset
2. Uncovers hidden patterns and trends through exploratory analysis
3. Creates an interactive dashboard for real-time decision-making
4. Provides actionable recommendations to drive business growth

### Expected Outcomes
- Clean, reliable dataset for ongoing analysis
- Visual insights accessible to non-technical stakeholders
- Data-driven recommendations for strategic decisions
- Replicable framework for future analytics projects

---

## Dataset Overview

### Source & Collection
- **Dataset Type:** Retail sales transaction data
- **Records:** 315 raw transactions → 288 validated records
- **Date Range:** January 2025 – December 2025
- **Format:** Excel (.xlsx) / CSV

### Data Structure

| Column | Type | Description |
|--------|------|-------------|
| OrderID | Integer | Unique transaction identifier |
| CustomerName | String | Customer identifier |
| OrderDate | Date | Transaction date |
| Region | String | Geographic region |
| City | String | City location |
| Category | String | Product category |
| Quantity | Integer | Units ordered |
| UnitPrice | Decimal | Price per unit |
| TotalSales | Decimal | Transaction value (Qty × Price) |

### Initial Data Quality Assessment

| Issue | Count | Percentage |
|-------|-------|-----------|
| Missing CustomerName | 16 | 5.1% |
| Missing Region | 16 | 5.1% |
| Missing City | 16 | 5.1% |
| Missing Quantity | 15 | 4.8% |
| Missing UnitPrice | 16 | 5.1% |
| Duplicate OrderIDs | 11 | 3.5% |
| Inconsistent Dates | Multiple | Various formats |
| Invalid Quantity (negative) | 5 | 1.6% |

---

## Data Cleaning Process

### Phase 1: Assessment & Audit
- Identified 79 missing values across 5 columns
- Detected 11 duplicate records
- Found inconsistent data formatting in dates and categorical fields
- Validated data types and ranges

### Phase 2: Handling Missing Values

#### Missing CustomerName (16 records)
- **Action:** Dropped rows (can't impute customer identity)
- **Rationale:** Core identifying field with no reasonable replacement
- **Impact:** 16 rows removed

#### Missing Region & City (16 records each)
- **Action:** Filled with "Unknown" placeholder category
- **Rationale:** Preserves transaction data; flags missing geography for investigation
- **Impact:** Created "Unknown" segment for analysis

#### Missing Quantity & UnitPrice (15-16 records)
- **Action:** Imputed with column median
- **Rationale:** Numeric fields; median is robust to outliers
- **Quantity Median:** 11 units
- **UnitPrice Median:** $247.50
- **Impact:** Preserved transaction records; minimal statistical distortion

### Phase 3: Duplicate Removal

#### Detection Method
- Identified exact duplicates based on OrderID
- Found 11 duplicate records (same OrderID appearing twice)

#### Resolution
- Kept first occurrence; removed subsequent duplicates
- Assumption: Later duplicates are data entry errors
- **Impact:** 11 rows removed

### Phase 4: Data Type & Format Standardization

#### Date Standardization
- **Issue:** Dates stored in two formats:
  - Format 1: DD/MM/YYYY (e.g., 15/01/2025)
  - Format 2: YYYY-MM-DD (e.g., 2025-01-15)
- **Solution:** Converted all to consistent datetime format (YYYY-MM-DD)
- **Validation:** Ensured all dates fall within 2025

#### Categorical Field Standardization
- **Region:** Standardized casing to Title Case
  - "north" → "North"
  - "SOUTH" → "South"
  - "East " → "East" (removed trailing space)
- **Category:** Applied same standardization
- **City:** Mapped variants to canonical city names:
  - "NY", "new york", "New York City" → "New York"
  - "LA", "los angeles" → "Los Angeles"

### Phase 5: Data Validation & Correction

#### Invalid Quantity Values
- **Issue:** 5 records had negative quantities (impossible in retail)
- **Root Cause:** Data entry errors (likely sign errors)
- **Solution:** Applied absolute value transformation
- **Validation:** All quantities now positive

#### Recalculation
- Recalculated TotalSales field after all corrections
- Formula: Quantity × UnitPrice
- Ensured consistency across all records

### Cleaning Results

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Total Records | 315 | 288 | -27 (-8.6%) |
| Missing Values | 79 | 0 | -79 (-100%) |
| Duplicates | 11 | 0 | -11 (-100%) |
| Data Quality | 94.9% | 100% | +5.1% |

---

## Exploratory Data Analysis

### Statistical Overview

```
Total Records Analyzed: 288
Date Range: 2025-01-01 to 2025-12-31

SALES METRICS:
├─ Total Sales: $753,045.00
├─ Average Order Value: $2,615.16
├─ Median Order Value: $2,447.50
├─ Std Deviation: $1,847.32
├─ Min Order: $12.50
└─ Max Order: $9,976.00

QUANTITY METRICS:
├─ Average Quantity: 10.8 units
├─ Median Quantity: 11 units
├─ Min Quantity: 1 unit
└─ Max Quantity: 20 units

PRICING METRICS:
├─ Average Unit Price: $242.17
├─ Median Unit Price: $247.50
├─ Min Price: $10.00
└─ Max Price: $500.00
```

### Key Insight 1: Order Value Distribution

**Finding:** Median significantly lower than mean ($2,447.50 vs $2,615.16)

**Implication:** Right-skewed distribution with high-value outliers  
**Action:** Focus on both volume and premium segments

### Key Insight 2: Regional Performance

| Region | Sales | % of Total | Avg Order |
|--------|-------|-----------|-----------|
| South | $232,104 | 30.8% | $2,598 |
| North | $188,925 | 25.1% | $2,477 |
| East | $189,345 | 25.1% | $2,635 |
| West | $142,671 | 18.9% | $2,540 |

**Finding:** South outperforms others by 23% vs lowest performer  
**Action:** Replicate South's success factors in underperforming regions

### Key Insight 3: Category Performance

| Category | Sales | % of Total | Order Count |
|----------|-------|-----------|------------|
| Electronics | $249,104 | 33.1% | 91 |
| Groceries | $263,456 | 35.0% | 100 |
| Furniture | $241,485 | 32.1% | 97 |

**Finding:** Groceries leads slightly; Electronics close behind  
**Action:** Cross-promotional strategies between categories

### Key Insight 4: Order Pattern Analysis

**High-Quantity Orders (Top 25%):**
- Count: 72 orders
- Average Size: 15.3 units
- Revenue Contribution: $288,765 (38.4%)
- Avg Order Value: $4,011

**Low-Quantity Orders (Bottom 25%):**
- Count: 72 orders
- Average Size: 7 units
- Revenue Contribution: $176,905 (23.5%)
- Avg Order Value: $2,457

**Finding:** Top quartile drives 38% revenue from 25% of orders  
**Action:** Develop bulk-order incentive programs

### Key Insight 5: Temporal Patterns

**Peak Months:**
- January: $72,450 (highest sales)
- August: $68,920
- March: $65,340

**Trough Months:**
- May: $58,230
- October: $59,670

**Pattern:** Clear seasonality with 23% variance between peak and trough  
**Action:** Align inventory and staffing with seasonal demand

---

## Interactive Dashboard

### Dashboard Features

#### 1. Real-Time KPI Cards
- **Total Sales:** Aggregate revenue with thousands separator
- **Average Order Value:** Mean transaction value (updated with filters)
- **Total Orders:** Transaction count
- **Top Category:** Best-performing category by revenue

#### 2. Interactive Charts

**Chart 1: Sales by Region (Bar Chart)**
- Purpose: Regional performance comparison
- Interaction: Hover for exact values
- Insight: Identifies top and underperforming regions

**Chart 2: Sales by Category (Pie Chart)**
- Purpose: Revenue contribution breakdown
- Interaction: Click legend to toggle categories
- Insight: Shows category importance in overall revenue

**Chart 3: Monthly Sales Trend (Line Chart)**
- Purpose: Temporal pattern visualization
- Interaction: Zoom and pan to focus on specific periods
- Insight: Reveals seasonality and trend direction

**Chart 4: Quantity Distribution (Histogram)**
- Purpose: Order size frequency analysis
- Interaction: Hover to see exact counts
- Insight: Shows concentration of order sizes

**Chart 5: Unit Price Distribution (Histogram)**
- Purpose: Price point concentration
- Interaction: Identify most common price ranges
- Insight: Reveals pricing strategy effectiveness

**Chart 6: Quantity vs. Sales Correlation (Scatter Plot)**
- Purpose: Relationship visualization
- Interaction: Hover for individual transaction details
- Insight: Strong positive correlation = larger orders drive more revenue

#### 3. Dynamic Filters
- **Region Filter:** Drill down by geography
- **Category Filter:** Focus on specific product types
- **Reset Button:** Return to full dataset view
- **Real-Time Updates:** All KPIs and charts respond instantly

### Dashboard Access
- **Live Link:** https://nishuchhikara.github.io/data-analyst-internship-task1/dashboard.html
- **Responsive:** Works on desktop, tablet, mobile
- **Technology:** HTML5, CSS3, JavaScript, Plotly.js
- **Performance:** Loads in <2 seconds

---

## Key Business Insights

### Insight 1: Regional Growth Opportunity
**Finding:** South region generates 30.8% of revenue vs. West's 18.9% — a 63% performance gap

**Root Cause Analysis:**
- Higher market demand in South
- Better regional positioning/marketing
- Established customer relationships

**Recommendation:**
- Conduct competitive analysis of South's success factors
- Replicate marketing strategies in underperforming regions
- Invest in North/East/West market development
- Expected Impact: 10-15% revenue increase if West reaches South's performance

---

### Insight 2: Bulk Order Segment Drives Disproportionate Revenue
**Finding:** Top 25% of orders (by quantity) generate 38.4% of revenue

**Implications:**
- Small group of wholesale/bulk customers critical to business
- High-quantity orders significantly more profitable per transaction
- Volume discounts may not be eroding margins

**Recommendation:**
- Create dedicated account management for high-volume customers
- Develop tiered pricing for bulk orders ($500-$1000+ commitments)
- Implement loyalty program for repeat bulk purchasers
- Expected Impact: 8-12% margin improvement on bulk segment

---

### Insight 3: Strong Seasonality Requires Dynamic Planning
**Finding:** 23% revenue variance between peak (January: $72K) and trough (May: $58K) months

**Strategic Implications:**
- Predictable demand fluctuations enable proactive planning
- Inventory needs vary significantly by quarter
- Staffing and marketing budget allocation should align with seasons

**Recommendation:**
- Build inventory 30% higher before January and August peaks
- Plan hiring cycles for peak months (start recruiting 60 days prior)
- Launch promotional campaigns 6-8 weeks before peak seasons
- Expected Impact: 5-10% cost savings through better resource allocation

---

### Insight 4: Category Performance Parity Suggests Cross-Sell Opportunity
**Finding:** Electronics (33.1%), Groceries (35.0%), Furniture (32.1%) — relatively balanced

**Strategic Opportunity:**
- No dominant category creates bundle opportunity
- Customers buying one category likely receptive to others
- Cross-category promotions have high success probability

**Recommendation:**
- Implement "Frequently Bought Together" recommendations
- Create category bundles (e.g., "Office Setup": Electronics + Furniture)
- Run cross-category promotions during peak seasons
- Expected Impact: 12-18% increase in average order value

---

### Insight 5: Data Quality Improvements Enable Trust & Automation
**Finding:** 100% data quality achieved after cleaning (from 94.9%)

**Impact:**
- Dashboard metrics now fully reliable
- Can confidently automate reporting and alerts
- Enables machine learning for forecasting
- Eliminates manual data verification overhead

**Recommendation:**
- Implement data validation at point of entry
- Establish data quality KPI (target: 99%+)
- Create data stewardship role
- Expected Impact: 20-30% reduction in analytical rework

---

## Recommendations

### Short-Term (1-3 months)

1. **Implement Category Cross-Selling**
   - Launch "Complete Your Setup" recommendations
   - Pilot with top 100 customers
   - Target: 5% AOV increase

2. **Optimize High-Quantity Customer Program**
   - Assign dedicated support to top 20 bulk customers
   - Establish quarterly business reviews
   - Target: Retain 100% of high-value segment

3. **Refresh Regional Marketing Strategy**
   - Conduct South region customer interviews
   - Document best practices and success factors
   - Target: Identify 3-5 replicable strategies

### Medium-Term (3-6 months)

1. **Launch Seasonal Demand Planning**
   - Build 12-month rolling forecast model
   - Align inventory to predicted peaks/troughs
   - Target: 15% inventory cost reduction

2. **Develop Tiered Pricing Strategy**
   - Create volume discount tiers
   - Test profitability vs. volume trade-offs
   - Target: 8% margin improvement on bulk orders

3. **Expand to Underperforming Regions**
   - Open regional sales office or partner in North/West
   - Allocate marketing budget proportional to opportunity
   - Target: Close 40% of regional performance gap

### Long-Term (6-12 months)

1. **Build Predictive Analytics Capability**
   - Develop demand forecasting model
   - Implement churn prediction for high-value customers
   - Enable inventory optimization automation

2. **Create Personalized Customer Experience**
   - Segment customers by purchase pattern
   - Develop personalized product recommendations
   - Target: 25% repeat purchase rate improvement

3. **Establish Data-Driven Culture**
   - Democratize dashboard access to department heads
   - Monthly data-driven strategy reviews
   - Embed analytics into hiring and performance evaluation

---

## Technical Stack

### Data Processing
- **Language:** Python 3.9+
- **Libraries:** Pandas (data manipulation), NumPy (calculations)
- **Format:** CSV, Excel (.xlsx)

### Analysis & Visualization
- **Tools:** Plotly.js (interactive charts), Matplotlib/Seaborn (static visualization)
- **Approach:** Exploratory Data Analysis (EDA) with statistical summaries

### Dashboard Development
- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **Visualization Library:** Plotly.js
- **Data Processing:** PapaParse (CSV parsing in browser)
- **Deployment:** GitHub Pages (zero-cost hosting)

### Version Control & Collaboration
- **Platform:** GitHub
- **Repository:** data-analyst-internship-task1
- **Documentation:** Markdown files with embedded charts

---

## Project Structure

```
data-analyst-internship-task1/
│
├── Task1_DataCleaning/
│   ├── Task1_Raw_Dataset.xlsx          (315 raw records)
│   ├── Task1_Cleaned_Dataset.xlsx      (288 validated records)
│   └── README.md                        (Cleaning documentation)
│
├── Task2_ExploratoryAnalysis/
│   ├── Task2_EDA_Report.md              (Statistical findings)
│   ├── Task2_EDA_Visualizations.png     (6 charts)
│   └── task2_eda.py                     (Python analysis code)
│
├── Task3_InteractiveDashboard/
│   ├── dashboard.html                   (Live dashboard)
│   ├── cleaned_data.csv                 (Data source)
│   └── README_TASK3.md                  (Dashboard documentation)
│
├── Task4_CaseStudy/
│   ├── CASE_STUDY.md                    (This document)
│   ├── EXECUTIVE_SUMMARY.pdf            (1-page summary)
│   └── RECOMMENDATIONS.docx             (Action items)
│
└── README.md                            (Project overview)
```

---

## Lessons Learned

### Data Quality is Foundation
- 8.6% data removal required to achieve 100% quality
- Investing in cleaning upfront saves 10x effort downstream
- Automated validation prevents recurring quality issues

### Visualization Communicates Better Than Tables
- Interactive dashboard revealed insights tables missed
- Non-technical stakeholders engage with visuals, not spreadsheets
- Real-time filters enable self-service analysis

### Domain Knowledge Enhances Analysis
- Understanding retail operations revealed seasonal patterns
- Business context helped distinguish signals from noise
- Collaboration with domain experts accelerated insights

### Scalability Requires Modular Design
- Separated cleaning, analysis, and visualization layers
- Easier to update data without recoding analysis
- Framework replicable for other datasets

---

## Conclusion

This four-week analytics project demonstrates a complete, production-ready data analytics workflow. From raw data with 8.6% quality issues to a clean, interactive dashboard with 5+ actionable insights, the project shows how structured methodology and modern tools transform raw data into strategic business intelligence.

The retail sales dataset analysis revealed significant opportunities in regional expansion, bulk customer engagement, seasonal planning, and cross-category marketing — opportunities that would have remained hidden without systematic data exploration and visualization.

**Impact Summary:**
- ✅ 100% data quality achieved
- ✅ 5+ business insights generated
- ✅ Interactive dashboard deployed
- ✅ $753K revenue analyzed
- ✅ Actionable recommendations delivered

This project serves as a foundation for ongoing analytics initiatives and demonstrates readiness for advanced roles in data science and business intelligence.

---

## Appendix: Tools & Technologies

### Data Analysis Tools
- **Python:** Data manipulation and statistical analysis
- **Pandas:** DataFrame operations, cleaning, transformation
- **NumPy:** Numerical computations and array operations
- **Matplotlib/Seaborn:** Statistical visualization
- **PapaParse:** CSV parsing in JavaScript

### Visualization & BI
- **Plotly.js:** Interactive chart library
- **GitHub Pages:** Free web hosting for dashboard

### Version Control
- **Git/GitHub:** Code versioning and collaboration

### Documentation
- **Markdown:** Technical documentation
- **PDF:** Executive summaries
- **HTML:** Interactive web content

---

**Project Completion Date:** October 2026  
**Total Duration:** 4 weeks  
**Author:** Nishu Chhikara  
**Contact:** nishuchhikara1@gmail.com  
**LinkedIn:** linkedin.com/in/nishu-chhikara  
**GitHub:** github.com/Nishuchhikara
