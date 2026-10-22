
import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned sales dataset
df = pd.read_csv("cleaned_sales_dataset.csv")

# Display the first five rows
print("FIRST FIVE ROWS OF THE DATASET")
print(df.head())


# Step 6: Data Inspection

print("\nDATASET SHAPE (ROWS, COLUMNS)")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nDATASET INFORMATION")
df.info()

print("\nDATA TYPES OF EACH COLUMN")
print(df.dtypes)

print("\nSTATISTICAL SUMMARY")
print(df.describe())




# Step 7: Check Missing Values and Duplicate Records

print("\nMISSING VALUES IN EACH COLUMN")
print(df.isnull().sum())

print("\nTOTAL MISSING VALUES")
print(df.isnull().sum().sum())

print("\nNUMBER OF DUPLICATE ROWS")
print(df.duplicated().sum())

# Display duplicate rows if any exist
print("\nDUPLICATE RECORDS")
print(df[df.duplicated()])



# Step 8: Data Cleaning and Missing-Value Handling

# Convert Order Date to datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

# Convert Quantity and Unit Price to numeric values
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Unit Price"] = pd.to_numeric(df["Unit Price"], errors="coerce")

# Check for missing values after conversion
print("\nMISSING VALUES AFTER DATA TYPE CONVERSION")
print(df.isnull().sum())

# Check placeholder values
print("\nUNKNOWN VALUES IN EACH COLUMN")
for column in df.columns:
    print(f"{column}: {(df[column].astype(str).str.strip().str.lower() == 'unknown').sum()}")

# Check invalid quantities and prices
print("\nINVALID QUANTITIES (ZERO OR NEGATIVE)")
print((df["Quantity"] <= 0).sum())

print("\nINVALID UNIT PRICES (NEGATIVE)")
print((df["Unit Price"] < 0).sum())

# Display updated data types
print("\nUPDATED DATA TYPES")
print(df.dtypes)



# Step 9: Descriptive Statistics

print("\nDESCRIPTIVE STATISTICS FOR NUMERICAL COLUMNS")
print(df[["Quantity", "Unit Price"]].describe())

# Calculate sales amount for each order
df["Sales Amount"] = df["Quantity"] * df["Unit Price"]

print("\nSALES AMOUNT STATISTICS")
print(df["Sales Amount"].describe())

# Calculate total sales
total_sales = df["Sales Amount"].sum()

# Calculate average sales per order
average_sales = df["Sales Amount"].mean()

# Calculate median sales per order
median_sales = df["Sales Amount"].median()

print("\nKEY SALES STATISTICS")
print(f"Total Sales: Rs. {total_sales:,.2f}")
print(f"Average Sales per Order: Rs. {average_sales:,.2f}")
print(f"Median Sales per Order: Rs. {median_sales:,.2f}")




# Step 10: Correlation Analysis

print("\nCORRELATION ANALYSIS")

# Select numerical columns for correlation

correlation_data = df[["Quantity", "Unit Price", "Sales Amount"]]

# Calculate the correlation matrix

correlation_matrix = correlation_data.corr()

# Display the correlation matrix

print(correlation_matrix)

# Visualize the correlation matrix

plt.figure(figsize=(8, 6))
plt.imshow(correlation_matrix, cmap="coolwarm", vmin=-1, vmax=1)
plt.colorbar(label="Correlation Coefficient")

plt.xticks(range(len(correlation_matrix.columns)),
correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)),
correlation_matrix.columns)

# Display correlation values inside the chart

for i in range(len(correlation_matrix.columns)):
 for j in range(len(correlation_matrix.columns)):
   plt.text(j, i, f"{correlation_matrix.iloc[i, j]:.2f}",
     ha="center", va="center")

plt.title("Correlation Matrix of Sales Data")
plt.tight_layout()
plt.savefig("correlation_matrix.png")
plt.show()






# Step 11: Identify Important Patterns and Trends

# Sales by product category

category_sales = df.groupby("Category")["Sales Amount"].sum().sort_values(ascending=False)

print("\nTOTAL SALES BY CATEGORY")
print(category_sales)

# Sales by region

region_sales = df.groupby("Region")["Sales Amount"].sum().sort_values(ascending=False)

print("\nTOTAL SALES BY REGION")
print(region_sales)

# Sales by month

df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
monthly_sales = df.groupby("Month")["Sales Amount"].sum()

print("\nTOTAL SALES BY MONTH")
print(monthly_sales)

# Create a bar chart of sales by category

category_sales.plot(kind="bar", figsize=(8, 5), title="Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Sales Amount (Rs.)")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

# Create a bar chart of sales by region

region_sales.plot(kind="bar", figsize=(8, 5), title="Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales Amount (Rs.)")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()

# Create a line chart of monthly sales

monthly_sales.plot(kind="line", marker="o", figsize=(8, 5), title="Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Amount (Rs.)")
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()


# Step 12: Outlier Detection Using the IQR Method

print("\nOUTLIER DETECTION")

# Calculate the first and third quartiles

Q1 = df["Sales Amount"].quantile(0.25)
Q3 = df["Sales Amount"].quantile(0.75)

# Calculate the Interquartile Range (IQR)

IQR = Q3 - Q1

# Calculate the lower and upper boundaries

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"Q1: Rs. {Q1:,.2f}")
print(f"Q3: Rs. {Q3:,.2f}")
print(f"IQR: Rs. {IQR:,.2f}")
print(f"Lower Bound: Rs. {lower_bound:,.2f}")
print(f"Upper Bound: Rs. {upper_bound:,.2f}")

# Identify outlier orders

outliers = df[
(df["Sales Amount"] < lower_bound) |
(df["Sales Amount"] > upper_bound)
]

print("\nIDENTIFIED OUTLIER ORDERS")
print(outliers[["Order ID", "Product", "Quantity", "Unit Price", "Sales Amount"]])

print(f"\nTotal Number of Outlier Orders: {len(outliers)}")

# Create a box plot to visualize outliers

plt.figure(figsize=(8, 5))
plt.boxplot(df["Sales Amount"].dropna())
plt.title("Box Plot of Sales Amount")
plt.ylabel("Sales Amount (Rs.)")
plt.tight_layout()
plt.savefig("sales_amount_outliers.png")
plt.show()
