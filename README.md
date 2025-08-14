# TASK-7-Get-Basic-Sales-Summary-from-a-Tiny-SQLite-Database-using-Python
Python script that connects to a SQLite database, summarizes sales data, and visualizes revenue by product with a bar chart.
Basic Sales Summary from SQLite Database using Python

This project shows how to connect Python to a SQLite database and turn raw sales data into clear, visual insights.
The script fetches total units sold and total revenue for each product, displays the results in a table, and creates a bar chart for easy understanding.

Features

Connects to a local SQLite database (sales_data.db)

Runs an SQL query to summarize sales per product

Displays results as a formatted table

Creates and saves a bar chart (sales_chart.png)

Uses pandas and matplotlib for analysis and visualization

How It Works

Connect to the SQLite database using sqlite3

Run a SQL aggregation query:

SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;


Load results into a pandas DataFrame

Print the summary table

Generate and save a revenue-by-product bar chart

Requirements

Python 3.x

pandas

matplotlib

Install dependencies:

pip install pandas matplotlib

Usage

Make sure sales_data.db is in the same folder as the script.

Run the script:

python task7_summary.py


Check the terminal for the table output.

Open sales_chart.png to view the chart.

Example Output

Table:

      product  total_qty  revenue
Wireless Mouse         8   119.92
USB-C Cable           18   117.00
Headphones             8   312.00
Laptop Sleeve          6   108.00
Webcam                 4   199.96


Chart:
(Example revenue-by-product bar chart)

Why This Project

This is a simple but practical way to practice:

Writing SQL queries

Working with SQLite in Python

Using pandas for data analysis

Creating basic visualizations
