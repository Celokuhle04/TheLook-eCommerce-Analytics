
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

# Monthly revenue query
query = """
SELECT
    YEAR(created_at) AS sales_year,
    MONTH(created_at) AS sales_month,
    COUNT(*) AS items_sold,
    SUM(sale_price) AS total_revenue
FROM dbo.order_items
WHERE status IN ('Shipped', 'Complete')
GROUP BY
    YEAR(created_at),
    MONTH(created_at)
ORDER BY
    sales_year,
    sales_month;
"""

# Load data into Pandas
df = pd.read_sql(query, engine)

engine.dispose()

# Create monthly date column
df["month"] = pd.to_datetime(
    df["sales_year"].astype(str) + "-"
    + df["sales_month"].astype(str) + "-01"
)

# Display results
print("\nMONTHLY REVENUE ANALYSIS")
print("=" * 50)
print(df[["month", "items_sold", "total_revenue"]].to_string(index=False))

# Summary statistics
print("\nREVENUE SUMMARY")
print("=" * 50)
print(f"Total months: {len(df)}")
print(f"Average monthly revenue: ${df['total_revenue'].mean():,.2f}")
print(f"Highest monthly revenue: ${df['total_revenue'].max():,.2f}")

# Visualisation
plt.figure(figsize=(12, 6))

plt.plot(
    df["month"],
    df["total_revenue"],
    marker="o",
    linewidth=2
)

plt.title("TheLook E-Commerce: Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()
