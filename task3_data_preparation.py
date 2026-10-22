import pandas as pd

# Task 3: Dataset Selection and Data Preparation

# Load the dataset

df = pd.read_csv("dataset - sales_dataset.csv")

# Display the first five rows

print("FIRST FIVE ROWS OF THE DATASET")
print(df.head())

# Display the last five rows

print("\nLAST FIVE ROWS OF THE DATASET")
print(df.tail())

# Display the dataset shape

print("\nDATASET SHAPE")
print(df.shape)

# Display column names

print("\nCOLUMN NAMES")
print(df.columns.tolist())

# Display dataset information

print("\nDATASET INFORMATION")
df.info()

# Display statistical summary

print("\nSTATISTICAL SUMMARY")
print(df.describe(include="all"))


# STEP 6: Identify Columns and Data Types

print("\nIDENTIFICATION OF COLUMNS AND DATA TYPES")
for column in df.columns:
    print(f"{column}: {df[column].dtype}")


# STEP 7: Identify Missing Values

print("\nMISSING VALUES IN EACH COLUMN")
print(df.isnull().sum())

print("\nTOTAL NUMBER OF MISSING VALUES")
print(df.isnull().sum().sum())

# STEP 8: Handle Missing Values

# Fill missing text values with "Unknown"

text_columns = ["Customer Name", "Category", "Region"]

for column in text_columns:
    df[column] = df[column].fillna("Unknown")

# Fill missing order dates with the most frequent date

df["Order Date"] = df["Order Date"].fillna(df["Order Date"].mode()[0])

# Fill missing unit prices with the median price

df["Unit Price"] = df["Unit Price"].fillna(df["Unit Price"].median())

print("\nMISSING VALUES AFTER HANDLING")
print(df.isnull().sum())

print("\nDATASET AFTER HANDLING MISSING VALUES")
print(df.head())

# STEP 9: Identify and Remove Duplicate Records

print("\nNUMBER OF DUPLICATE ROWS BEFORE REMOVAL")
print(df.duplicated().sum())

# Remove duplicate rows

df = df.drop_duplicates()

print("\nNUMBER OF DUPLICATE ROWS AFTER REMOVAL")
print(df.duplicated().sum())

print("\nDATASET SHAPE AFTER DUPLICATE REMOVAL")
print(df.shape)



# STEP 10: Identify and Handle Incorrect Records

# Convert Order Date to datetime format

df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

# Display records with invalid dates

print("\nRECORDS WITH INVALID ORDER DATES")
print(df[df["Order Date"].isnull()])

# Display records with invalid quantities

print("\nRECORDS WITH ZERO OR NEGATIVE QUANTITIES")
print(df[df["Quantity"] <= 0])

# Display records with invalid unit prices

print("\nRECORDS WITH ZERO OR NEGATIVE UNIT PRICES")
print(df[df["Unit Price"] <= 0])

# Remove records with invalid dates or nonpositive quantities/prices

df = df.dropna(subset=["Order Date"])
df = df[df["Quantity"] > 0]
df = df[df["Unit Price"] > 0]

print("\nDATASET SHAPE AFTER REMOVING INCORRECT RECORDS")
print(df.shape)

print("\nREMAINING INVALID RECORDS")
print("Invalid dates:", df["Order Date"].isnull().sum())
print("Nonpositive quantities:", (df["Quantity"] <= 0).sum())
print("Nonpositive prices:", (df["Unit Price"] <= 0).sum())



# STEP 11: Save the Cleaned Dataset

# Save the cleaned dataset to a new CSV file

df.to_csv("cleaned_sales_dataset.csv", index=False)

print("\nCLEANED DATASET SAVED SUCCESSFULLY")
print("File name: cleaned_sales_dataset.csv")
print("Final number of rows:", df.shape[0])
print("Final number of columns:", df.shape[1])




# STEP 12: Verify the Final Dataset

print("\nFINAL DATASET VERIFICATION")

# Check dataset dimensions

print("\nDataset shape:")
print(df.shape)

# Check missing values

print("\nMissing values in each column:")
print(df.isnull().sum())

# Check duplicate records

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Check invalid quantities

print("\nRecords with zero or negative quantities:")
print((df["Quantity"] <= 0).sum())

# Check invalid unit prices

print("\nRecords with zero or negative unit prices:")
print((df["Unit Price"] <= 0).sum())

# Display the first five cleaned records

print("\nFirst five records of the cleaned dataset:")
print(df.head())

# Display final column data types

print("\nFinal column data types:")
print(df.dtypes)

