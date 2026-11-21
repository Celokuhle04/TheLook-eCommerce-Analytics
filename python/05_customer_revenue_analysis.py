
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

# Top 10 customers by revenue
query = """
SELECT TOP 10
    u.id AS customer_id,
    CONCAT(u.first_name, ' ', u.last_name) AS customer_name,
    COUNT(DISTINCT oi.order_id) AS total_orders,
    COUNT(*) AS items_purchased,
    SUM(oi.sale_price) AS total_revenue
FROM dbo.order_items oi
INNER JOIN dbo.users u
    ON oi.user_id = u.id
WHERE oi.status IN ('Shipped', 'Complete')
GROUP BY
    u.id,
    u.first_name,
    u.last_name
ORDER BY total_revenue DESC;
"""

# Retrieve data
df = pd.read_sql(query, engine)
engine.dispose()

# Display results
print("\nTOP 10 CUSTOMERS BY REVENUE")
print("=" * 65)
print(df.to_string(index=False))

# Revenue summary
print("\nCUSTOMER REVENUE SUMMARY")
print("=" * 65)
print(f"Highest customer revenue: ${df['total_revenue'].max():,.2f}")
print(f"Average revenue among top 10: ${df['total_revenue'].mean():,.2f}")

# Visualisation
plt.figure(figsize=(12, 7))

plt.barh(
    df["customer_name"],
    df["total_revenue"]
)

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Total Revenue ($)")
plt.ylabel("Customer")
plt.gca().invert_yaxis()
plt.tight_layout()

plt.show()
