CREATE DATABASE Global_Superstore_DB;
USE Global_Superstore_DB;
SELECT COUNT(*) AS total_rows
FROM global_superstore_utf8;
SELECT *
FROM global_superstore_utf8
LIMIT 10;
SELECT SUM(CAST(Sales AS DECIMAL(15,2))) AS total_sales
FROM global_superstore_utf8;
SELECT SUM(CAST(Profit AS DECIMAL(15,2))) AS total_profit
FROM global_superstore_utf8;
SELECT SUM(CAST(Quantity AS UNSIGNED)) AS total_quantity
FROM global_superstore_utf8;
SELECT
    Category,
    SUM(CAST(Sales AS DECIMAL(15,2))) AS total_sales
FROM global_superstore_utf8
GROUP BY Category
ORDER BY total_sales DESC;
SELECT
    Category,
    SUM(CAST(Profit AS DECIMAL(15,2))) AS total_profit
FROM global_superstore_utf8
GROUP BY Category
ORDER BY total_profit DESC;
SELECT
    Region,
    SUM(CAST(Sales AS DECIMAL(15,2))) AS total_sales
FROM global_superstore_utf8
GROUP BY Region
ORDER BY total_sales DESC;
SELECT
    `Product Name`,
    SUM(CAST(Sales AS DECIMAL(15,2))) AS total_sales
FROM global_superstore_utf8
GROUP BY `Product Name`
ORDER BY total_sales DESC
LIMIT 10;
SELECT
    Market,
    SUM(CAST(Sales AS DECIMAL(15,2))) AS total_sales
FROM global_superstore_utf8
GROUP BY Market
ORDER BY total_sales DESC;
SELECT
    `Customer ID`,
    SUM(CAST(Sales AS DECIMAL(15,2))) AS total_sales
FROM global_superstore_utf8
GROUP BY `Customer ID`
ORDER BY total_sales DESC
LIMIT 10;
SELECT
    `Sub-Category`,
    SUM(CAST(Sales AS DECIMAL(15,2))) AS total_sales
FROM global_superstore_utf8
GROUP BY `Sub-Category`
ORDER BY total_sales DESC;
SELECT
    Segment,
    SUM(CAST(Sales AS DECIMAL(15,2))) AS total_sales
FROM global_superstore_utf8
GROUP BY Segment
ORDER BY total_sales DESC;
SELECT
    Region,
    SUM(CAST(Profit AS DECIMAL(15,2))) AS total_profit
FROM global_superstore_utf8
GROUP BY Region
ORDER BY total_profit DESC;
SELECT
    Discount,
    SUM(CAST(Profit AS DECIMAL(15,2))) AS total_profit
FROM global_superstore_utf8
GROUP BY Discount
ORDER BY Discount;