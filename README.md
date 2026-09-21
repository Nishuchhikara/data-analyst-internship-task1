# Dataset Cleaning – Task 1 (Data Analyst Internship, SWYNEX Technologies)

## Dataset
A retail sales dataset containing 315 order records with fields: OrderID, CustomerName, OrderDate, Region, City, Category, Quantity, UnitPrice, and TotalSales.

- **Raw file:** `Task1_Raw_Dataset.xlsx`
- **Cleaned file:** `Task1_Cleaned_Dataset.xlsx`

## Issues Identified
- **Missing values:** 16 missing CustomerName, 16 missing Region, 16 missing City, 15 missing Quantity, 16 missing UnitPrice
- **Duplicate records:** 11 duplicate rows (same OrderID appearing more than once)
- **Inconsistent categorical values:** Region and Category had mixed casing and stray whitespace (e.g., "north", "SOUTH", "East "); City had multiple naming variants for the same city (e.g., "NY", "new york", "New York City" all referring to New York)
- **Invalid data entries:** 5 records had negative Quantity values (data entry errors)

## Cleaning Steps
1. **Missing values:**
   - Dropped rows missing `CustomerName` (a required identifying field with no reasonable way to impute)
   - Filled missing `Region`/`City` with "Unknown" as a placeholder category
   - Filled missing `Quantity`/`UnitPrice` with the column median to avoid skewing totals
2. **Duplicates:** Identified and removed 11 duplicate rows based on `OrderID`, keeping the first occurrence
3. **Data types:** Standardized `OrderDate` (originally in two different formats) into a single, consistent datetime format
4. **Inconsistent values:** Standardized `Region` and `Category` text casing (Title Case, trimmed whitespace); mapped all city name variants (e.g., "NY", "new york") to a single canonical value ("New York")
5. **Invalid entries:** Corrected 5 negative `Quantity` values by taking the absolute value, treating them as data entry sign errors
6. **Recalculated `TotalSales`** (Quantity × UnitPrice) after cleaning to ensure consistency

## Result
- Raw dataset: 315 rows → Cleaned dataset: 288 rows (after removing duplicates and unrecoverable missing records)
- Zero missing values remaining in the cleaned dataset
- All categorical fields standardized to consistent naming

## Tools Used
Python (pandas) for data cleaning and transformation, Excel (.xlsx) for input/output format
