
import pandas as pd
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

# Business KPI query
query = """
SELECT
    (SELECT COUNT(*) FROM dbo.users) AS total_customers,

    (SELECT COUNT(*) FROM dbo.orders) AS total_orders,

    (SELECT COUNT(*)
     FROM dbo.orders
     WHERE status IN ('Shipped', 'Complete')) AS completed_orders,

    (SELECT SUM(sale_price)
     FROM dbo.order_items
     WHERE status IN ('Shipped', 'Complete')) AS total_revenue,

    (SELECT CAST(SUM(sale_price) AS DECIMAL(18,2))
        / NULLIF(COUNT(DISTINCT order_id), 0)
     FROM dbo.order_items
     WHERE status IN ('Shipped', 'Complete')) AS average_order_value;
"""

# Retrieve results using Pandas
df = pd.read_sql(query, engine)

# Display results
print("\nTHELOOK E-COMMERCE BUSINESS KPIs")
print("=" * 45)
print(df.to_string(index=False))

engine.dispose()
