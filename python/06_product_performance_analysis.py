
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Database connection
server = r"localhost\SQLEXPRESS"
database = "TheLookEcommerce"
driver = "ODBC Driver 18 for SQL Server"

connection_string = (
    f"DRIVER={{{driver}}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={quote_plus(connection_string)}"
)

# Top 10 products by revenue
query = """
SELECT TOP 10
    p.id AS product_id,
    p.name AS product_name,
    p.category,
    p.brand,
    COUNT(*) AS items_sold,
    SUM(oi.sale_price) AS total_revenue,
    AVG(oi.sale_price) AS average_selling_price
FROM dbo.order_items oi
INNER JOIN dbo.products p
    ON oi.product_id = p.id
WHERE oi.status IN ('Shipped', 'Complete')
GROUP BY
    p.id,
    p.name,
    p.category,
    p.brand
ORDER BY total_revenue DESC;
"""

# Retrieve data
df = pd.read_sql(query, engine)
engine.dispose()

# Display results
print("\nTOP 10 PRODUCTS BY REVENUE")
print("=" * 100)
print(df.to_string(index=False))

# Summary
print("\nPRODUCT PERFORMANCE SUMMARY")
print("=" * 65)
print(f"Number of products analysed: {len(df)}")
print(f"Highest product revenue: ${df['total_revenue'].max():,.2f}")
print(f"Total revenue from top 10: ${df['total_revenue'].sum():,.2f}")

# Visualisation
plt.figure(figsize=(13, 8))

plt.barh(
    df["product_name"],
    df["total_revenue"]
)

plt.title("Top 10 Products by Revenue")
plt.xlabel("Total Revenue ($)")
plt.ylabel("Product")
plt.gca().invert_yaxis()
plt.tight_layout()

plt.show()
