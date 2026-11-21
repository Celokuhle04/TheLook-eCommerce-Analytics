
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

# Revenue by product category
query = """
SELECT
    p.category,
    COUNT(*) AS items_sold,
    SUM(oi.sale_price) AS total_revenue,
    SUM(p.cost) AS total_product_cost,
    SUM(oi.sale_price - p.cost) AS gross_profit
FROM dbo.order_items oi
INNER JOIN dbo.products p
    ON oi.product_id = p.id
WHERE oi.status IN ('Shipped', 'Complete')
GROUP BY p.category
ORDER BY total_revenue DESC;
"""

# Load data
df = pd.read_sql(query, engine)
engine.dispose()

# Display results
print("\nREVENUE BY PRODUCT CATEGORY")
print("=" * 65)
print(df.to_string(index=False))

# Calculate revenue contribution
total_revenue = df["total_revenue"].sum()

df["revenue_percentage"] = (
    df["total_revenue"] / total_revenue
) * 100

print("\nTOP 5 CATEGORIES BY REVENUE")
print("=" * 65)
print(
    df[["category", "total_revenue", "revenue_percentage"]]
    .head(5)
    .to_string(index=False)
)

# Visualisation
plt.figure(figsize=(12, 7))

sns.barplot(
    data=df,
    x="total_revenue",
    y="category"
)

plt.title("Revenue by Product Category")
plt.xlabel("Total Revenue ($)")
plt.ylabel("Product Category")
plt.tight_layout()

plt.show()
