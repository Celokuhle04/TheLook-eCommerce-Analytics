
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

# Customer purchasing behaviour
query = """
SELECT
    u.id AS customer_id,
    COUNT(DISTINCT oi.order_id) AS total_orders,
    COUNT(*) AS items_purchased,
    SUM(oi.sale_price) AS total_revenue
FROM dbo.order_items oi
INNER JOIN dbo.users u
    ON oi.user_id = u.id
WHERE oi.status IN ('Shipped', 'Complete')
GROUP BY u.id;
"""

# Retrieve customer data
df = pd.read_sql(query, engine)
engine.dispose()

# Summary statistics
print("\nCUSTOMER PURCHASING BEHAVIOUR")
print("=" * 65)
print(f"Purchasing customers: {len(df):,}")
print(f"Average orders per customer: {df['total_orders'].mean():.2f}")
print(f"Average revenue per customer: ${df['total_revenue'].mean():,.2f}")
print(f"Average items per customer: {df['items_purchased'].mean():.2f}")

# Purchasing frequency groups
def classify_customer(orders):
    if orders == 1:
        return "1 Order"
    elif orders <= 3:
        return "2–3 Orders"
    else:
        return "4+ Orders"

df["purchasing_frequency"] = df["total_orders"].apply(
    classify_customer
)

frequency = (
    df["purchasing_frequency"]
    .value_counts()
    .reindex(["1 Order", "2–3 Orders", "4+ Orders"])
)

print("\nCUSTOMER PURCHASING FREQUENCY")
print("=" * 65)
print(frequency.to_string())

# Visualisation
plt.figure(figsize=(9, 6))

frequency.plot(
    kind="bar",
    rot=0
)

plt.title("Customer Distribution by Purchasing Frequency")
plt.xlabel("Number of Orders")
plt.ylabel("Number of Customers")
plt.tight_layout()

plt.show()
