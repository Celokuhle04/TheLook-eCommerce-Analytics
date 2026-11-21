
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

# Order item status analysis
query = """
SELECT
    status,
    COUNT(*) AS total_items,
    SUM(sale_price) AS associated_revenue,
    AVG(sale_price) AS average_item_value
FROM dbo.order_items
GROUP BY status
ORDER BY total_items DESC;
"""

# Retrieve data
df = pd.read_sql(query, engine)
engine.dispose()

# Calculate percentages
total_items = df["total_items"].sum()

df["percentage"] = (
    df["total_items"] / total_items
) * 100

# Display results
print("\nORDER ITEM STATUS ANALYSIS")
print("=" * 75)
print(df.to_string(index=False))

# Returns and cancellations summary
problem_statuses = df[
    df["status"].isin(["Returned", "Cancelled"])
]

problem_items = problem_statuses["total_items"].sum()
problem_percentage = problem_statuses["percentage"].sum()
associated_value = problem_statuses["associated_revenue"].sum()

print("\nRETURNS AND CANCELLATIONS SUMMARY")
print("=" * 75)
print(f"Returned and cancelled items: {problem_items:,}")
print(f"Percentage of all items: {problem_percentage:.2f}%")
print(f"Associated sale value: ${associated_value:,.2f}")

# Visualisation
plt.figure(figsize=(11, 6))

sns.barplot(
    data=df,
    x="status",
    y="total_items"
)

plt.title("Order Items by Status")
plt.xlabel("Order Item Status")
plt.ylabel("Number of Items")
plt.tight_layout()

plt.show()
