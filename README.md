Sales Performance Analysis

Capstone Project – End-to-End Data Analysis



## 1. Project Overview

The Sales Performance Analysis project focuses on analyzing sales data using Python, data visualization techniques, and Microsoft Power BI. The main objective is to understand sales performance, identify top-performing products, compare sales across categories and regions, and discover trends that can help businesses make better decisions.

This project covers the complete data analytics workflow, including dataset selection, data preparation, exploratory data analysis (EDA), visualization, dashboard development, and business recommendations.

## 2. Problem Statement

Businesses generate sales data every day, but raw data alone does not provide enough information to make effective decisions. Analyzing this data helps identify profitable products, high-performing regions, customer purchasing patterns, and opportunities for improvement.

The purpose of this project is to transform raw sales data into meaningful insights using Python and Power BI.

## 3. Project Objectives

* Select and prepare a sales dataset for analysis.
* Inspect the dataset and identify its columns and data types.
* Handle missing values and duplicate records where necessary.
* Perform exploratory data analysis using Python.
* Calculate sales amounts and descriptive statistics.
* Analyze sales by product, category, region, and month.
* Create meaningful visualizations using Python.
* Develop an interactive sales performance dashboard in Power BI.
* Identify important business insights and provide recommendations.

## 4. Dataset Description

The project uses a sales dataset containing order information, customer names, product details, quantities, prices, and regions.

### Dataset Columns

| Column        | Description                        |
| ------------- | ---------------------------------- |
| Order ID      | Unique identifier for an order     |
| Order Date    | Date on which the order was placed |
| Customer Name | Name of the customer               |
| Product       | Name of the product purchased      |
| Category      | Product category                   |
| Quantity      | Number of units purchased          |
| Unit Price    | Price per unit                     |
| Region        | Region associated with the sale    |
| Sales Amount  | Calculated sales value             |

**Sales Amount = Quantity × Unit Price**

The `Sales Amount` column was created during the analysis to calculate the value of each sales record.

## 5. Tools and Technologies Used

* **Python:** Data analysis and calculations.
* **Pandas:** Data inspection, cleaning, and manipulation.
* **Matplotlib:** Data visualization.
* **Seaborn:** Statistical visualization.
* **Microsoft Power BI:** Interactive dashboard development.
* **DAX:** Measures and calculations in Power BI.
* **Git:** Version control.
* **GitHub:** Project storage, documentation, and collaboration.
* **CSV:** Dataset storage format.

## 6. Data Cleaning and Preparation

The dataset was inspected and prepared before performing the analysis.

The data preparation process included:

1. Loading the original sales dataset into Python.
2. Inspecting the first and last records.
3. Checking the number of rows and columns.
4. Identifying column names and data types.
5. Checking for missing values.
6. Handling missing values where necessary.
7. Checking for duplicate records.
8. Reviewing data types and correcting them where required.
9. Preparing the cleaned dataset for analysis.
10. Calculating the `Sales Amount` column using quantity and unit price.

The cleaned dataset was then used for exploratory data analysis, visualization, and Power BI dashboard development.

## 7. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand the structure and characteristics of the sales dataset.

The analysis included:

* Dataset inspection.
* Descriptive statistics.
* Missing-value analysis.
* Duplicate-record checks.
* Sales calculations.
* Category-wise sales analysis.
* Region-wise sales analysis.
* Monthly sales trend analysis.
* Top-selling product identification.
* Correlation analysis between numerical variables.
* Outlier inspection where applicable.

These steps helped identify important patterns and understand the overall sales performance.

## 8. Data Visualizations

The following visualizations were created during the project:

1. **Sales by Category:** Compares total sales across product categories.
2. **Sales by Region:** Shows how sales are distributed across different regions.
3. **Monthly Sales Trend:** Displays sales performance over time.
4. **Top 10 Products by Sales:** Identifies products generating the highest sales.
5. **Quantity vs. Unit Price:** Examines the relationship between product quantity and unit price.
6. **Sales Amount Distribution:** Shows the distribution of sales amounts.

These visualizations make the results easier to understand and help identify high-performing products, categories, and regions.

## 9. Power BI Dashboard

An interactive Sales Performance Dashboard was developed using Microsoft Power BI.

### Dashboard Components

* **Total Sales:** Displays the total sales amount.
* **Total Orders:** Shows the number of distinct orders.
* **Total Quantity Sold:** Displays the total quantity sold.
* **Sales by Category:** Compares sales across product categories.
* **Sales by Region:** Compares sales across regions.
* **Monthly Sales Trend:** Shows monthly sales performance.
* **Top 10 Products by Sales:** Highlights the best-performing products.
* **Slicers:** Allow users to filter the dashboard by region, category, and order date.

### DAX Measures

The following measures were created in Power BI:

Total Sales = SUM('cleaned_sales_dataset'[Sales Amount])
Total Orders = DISTINCTCOUNT('cleaned_sales_dataset'[Order ID])
Total Quantity Sold = SUM('cleaned_sales_dataset'[Quantity])```

The dashboard helps users explore sales performance interactively and compare results across different business dimensions.

## 10. Key Findings and Business Insights

The analysis produced the following findings:

### Overall Sales Performance

* **Total Sales:** ₹308,750
* **Distinct Orders:** 39
* **January 2026 Sales:** ₹266,500
* **February 2026 Sales:** ₹42,250

February contains fewer recorded days than January in the dataset. Therefore, the figures should not be treated as a complete-month comparison.

### Category-Wise Sales

| Category    | Total Sales |
| ----------- | ----------: |
| Electronics |    ₹233,500 |
| Furniture   |     ₹43,600 |
| Accessories |     ₹24,850 |
| Stationery  |      ₹4,600 |
| Unknown     |      ₹2,200 |

Electronics generated the highest sales among the listed categories, contributing the largest share of total revenue.

### Region-Wise Sales

| Region  | Total Sales |
| ------- | ----------: |
| South   |    ₹131,900 |
| North   |     ₹81,550 |
| West    |     ₹64,250 |
| East    |     ₹26,250 |
| Unknown |      ₹4,800 |

The South region recorded the highest sales, followed by the North and West regions. The East region generated comparatively lower sales.

### Top 10 Products by Sales

| Rank | Product        | Total Sales |
| ---: | -------------- | ----------: |
|    1 | Laptop         |    ₹110,000 |
|    2 | Monitor        |     ₹50,000 |
|    3 | Printer        |     ₹43,500 |
|    4 | Office Chair   |     ₹18,600 |
|    5 | Desk           |     ₹17,000 |
|    6 | Headphones     |     ₹12,000 |
|    7 | External Drive |      ₹9,600 |
|    8 | USB Hub        |      ₹9,000 |
|    9 | Webcam         |      ₹8,400 |
|   10 | Keyboard       |      ₹8,400 |

Laptops generated the highest sales among the products analyzed, followed by monitors and printers.

## 11. Business Recommendations

Based on the findings, the following recommendations are suggested:

1. **Focus on High-Performing Products:** Maintain sufficient stock of laptops, monitors, and printers because they generate substantial sales.
2. **Strengthen Electronics Sales:** Explore opportunities to expand the electronics category while continuing to monitor demand for other categories.
3. **Study Regional Performance:** Analyze the reasons for the South region's strong performance and identify opportunities to improve sales in the East region.
4. **Improve Inventory Planning:** Use historical sales patterns to support inventory and purchasing decisions.
5. **Monitor Sales Trends:** Review sales regularly to identify changes in demand and take timely action.
6. **Investigate Unknown Values:** Review records assigned to the `Unknown` category or region and correct them when reliable information is available.
7. **Use the Power BI Dashboard:** Monitor key performance indicators and filter the dashboard to support data-driven decisions.

## 12. Project Workflow

The project followed these stages:

1. Git and GitHub setup.
2. Git workflow practice using clone, add, commit, push, and pull.
3. Dataset selection and data preparation.
4. Exploratory Data Analysis using Python.
5. Data visualization using Matplotlib and Seaborn.
6. Interactive dashboard development using Power BI.
7. Business insights and recommendations.
8. GitHub documentation and project presentation.

## 13. Conclusion

The Sales Performance Analysis project demonstrates how data analytics tools can be used to convert raw sales data into meaningful business information. Python was used for data preparation, exploratory analysis, calculations, and visualizations, while Power BI was used to develop an interactive dashboard.

The analysis identified total sales, high-performing product categories, leading regions, and top-selling products. The results provide useful information for inventory planning, regional sales improvement, product prioritization, and business decision-making.

This capstone project provided practical experience with data cleaning, exploratory data analysis, data visualization, dashboard development, Git, and GitHub.




## 14. Author

**NAVANEETH P**
B.Tech Computer Science and Engineering
College of Engineering Trikaripur

**Project:** End-to-End Data Analysis
**Domain:** Sales Data Analytics
