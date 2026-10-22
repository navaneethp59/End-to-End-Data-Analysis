import pandas as pd
import matplotlib.pyplot as plt

# Task 5: Data Visualization

# Load the cleaned sales dataset

df = pd.read_csv("cleaned_sales_dataset.csv")

# Convert Order Date to datetime format

df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

# Calculate Sales Amount

df["Sales Amount"] = df["Quantity"] * df["Unit Price"]

# Display basic information

print("DATA VISUALIZATION PROJECT")
print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))

print("\nDataset loaded successfully!")
print(df.head())



# Chart 1: Sales by Product Category

category_sales = df.groupby("Category")["Sales Amount"].sum().sort_values(
ascending=False
)

print("\nTOTAL SALES BY PRODUCT CATEGORY")
print(category_sales)

plt.figure(figsize=(9, 6))
category_sales.plot(kind="bar")

plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales (Rs.)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("chart1_sales_by_category.png")
plt.show()


# Chart 2: Sales by Region

region_sales = df.groupby("Region")["Sales Amount"].sum().sort_values(
ascending=False
)

print("\nTOTAL SALES BY REGION")
print(region_sales)

plt.figure(figsize=(9, 6))
region_sales.plot(kind="bar")

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales (Rs.)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("chart2_sales_by_region.png")
plt.show()



# Chart 3: Monthly Sales Trend

df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

monthly_sales = df.groupby("Month")["Sales Amount"].sum().sort_index()

print("\nTOTAL SALES BY MONTH")
print(monthly_sales)

plt.figure(figsize=(9, 6))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales (Rs.)")
plt.grid(True)
plt.tight_layout()

plt.savefig("chart3_monthly_sales_trend.png")
plt.show()





# Chart 4: Top 10 Products by Sales

product_sales = df.groupby("Product")["Sales Amount"].sum().sort_values(
    ascending=False
).head(10)

print("\nTOP 10 PRODUCTS BY SALES")
print(product_sales)

plt.figure(figsize=(10, 6))
product_sales.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales (Rs.)")
plt.ylabel("Product")
plt.tight_layout()

plt.savefig("chart4_top10_products.png")
plt.show()




# Chart 5: Quantity vs Unit Price

print("\nQUANTITY AND UNIT PRICE ANALYSIS")
print(df[["Quantity", "Unit Price"]].describe())

plt.figure(figsize=(9, 6))
plt.scatter(df["Quantity"], df["Unit Price"])

plt.title("Relationship Between Quantity and Unit Price")
plt.xlabel("Quantity Ordered")
plt.ylabel("Unit Price (Rs.)")
plt.grid(True)
plt.tight_layout()

plt.savefig("chart5_quantity_vs_unit_price.png")
plt.show()




# Chart 6: Sales Amount Distribution

print("\nSALES AMOUNT DISTRIBUTION")
print(df["Sales Amount"].describe())

plt.figure(figsize=(9, 6))
plt.hist(df["Sales Amount"], bins=10, edgecolor="black")

plt.title("Distribution of Sales Amounts")
plt.xlabel("Sales Amount (Rs.)")
plt.ylabel("Number of Orders")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig("chart6_sales_amount_distribution.png")
plt.show()
