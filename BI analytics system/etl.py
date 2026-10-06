import pandas as pd



df = pd.read_csv("Global_Superstore_Raw.csv.csv")

print("Dataset shape:", df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nMissing values by column:")
missing = df.isnull().sum()
print(missing[missing > 0])

print("\nRows with missing values:")
print(df[df.isnull().sum(axis=1) > 0])

incomplete_rows = df[df.isnull().sum(axis=1) > 0]

print("\nIncomplete rows:")
print(incomplete_rows)

print("\nNumber of non-missing values in each incomplete row:")
print(incomplete_rows.notna().sum(axis=1))

df = df.dropna()

print("\nShape after cleaning:", df.shape)

print("\nData types:")
print(df.dtypes)

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    errors="coerce"
)

df = df.dropna(subset=["Order Date", "Ship Date"])

print("\nDate data types:")
print(df[["Order Date", "Ship Date"]].dtypes)


df = df.dropna(how="all")

print("\nShape after removing empty rows:", df.shape)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nQuantity minimum:", df["Quantity"].min())
print("Sales minimum:", df["Sales"].min())
print("Profit minimum:", df["Profit"].min())
print("Discount minimum:", df["Discount"].min())

print("\nRows with Sales = 0:")
print((df["Sales"] == 0).sum())

print(df[df["Sales"] == 0].T)

df = df[df["Sales"] > 0].copy()

print("\nShape after removing invalid sales:", df.shape)



df.to_csv(
    "Global_Superstore_Cleaned.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Cleaned dataset saved successfully!")

print("\nBasic Statistics:")
print(df.describe())


print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nFinal shape:")
print(df.shape)

total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

total_profit = df["Profit"].sum()
print("Total Profit:", total_profit)

total_quantity = df["Quantity"].sum()
print("Total Quantity:", total_quantity)

profit_margin = (total_profit / total_sales) * 100
print("Profit Margin:", profit_margin, "%")

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Category:")
print(category_sales)


category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\nProfit by Category:")
print(category_profit)

subcategory_profit = (
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\nProfit by Sub-Category:")
print(subcategory_profit)

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n9. Sales by Region:")
print(region_sales)

segment_sales = (
    df.groupby("Segment")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n10. Sales by Segment:")
print(segment_sales)

region_profit = (
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\n11. Profit by Region:")
print(region_profit)

df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n12. Monthly Sales:")
print(monthly_sales)

monthly_profit = df.groupby("Month")["Profit"].sum()

print("\n13. Monthly Profit:")
print(monthly_profit)

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n14. Top 10 Products by Sales:")
print(top_products)

top_profit_products = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n15. Top 10 Products by Profit:")
print(top_profit_products)

loss_products = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values()
    .head(10)
)

print("\n16. Top 10 Loss-Making Products:")
print(loss_products)

df["Year"] = df["Order Date"].dt.year

yearly_analysis = (
    df.groupby("Year")[["Sales", "Profit"]]
    .sum()
)

print("\n17. Yearly Sales and Profit:")
print(yearly_analysis)


best_sales_year = yearly_analysis["Sales"].idxmax()
best_profit_year = yearly_analysis["Profit"].idxmax()

print("\n18. Best Sales Year:", best_sales_year)
print("Best Profit Year:", best_profit_year)

top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n19. Top 10 Customers by Sales:")
print(top_customers)

discount_analysis = (
    df.groupby("Category")["Discount"]
    .mean()
    .sort_values(ascending=False)
)

print("\n20. Average Discount by Category:")
print(discount_analysis)


print("\n===================================")
print("ETL PROCESS COMPLETED SUCCESSFULLY")
print("===================================")