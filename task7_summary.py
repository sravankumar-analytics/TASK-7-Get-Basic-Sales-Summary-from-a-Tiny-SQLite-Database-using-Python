import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Connect to your SQLite database
# Make sure sales_data.db is in the same folder as this script
conn = sqlite3.connect("sales_data.db")

# 2. Write the SQL query
query = """
SELECT 
    product,
    SUM(quantity) AS total_qty,
    ROUND(SUM(quantity * price), 2) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;
"""

# 3. Run the query and store results in a pandas DataFrame
df = pd.read_sql_query(query, conn)

# 4. Print the summary table
print("\nSales Summary by Product:\n")
print(df.to_string(index=False))

# Close the database connection
conn.close()

# 5. Plot the revenue by product
plt.figure(figsize=(8, 5))
plt.bar(df["product"], df["revenue"])
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# 6. Save the chart as a PNG file
plt.savefig("sales_chart.png", dpi=150)
print("\nChart saved as 'sales_chart.png'")

# 7. (Optional) Show the chart
plt.show()
