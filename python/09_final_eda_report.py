
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

# Overall business performance
kpi_query = """
SELECT
    (SELECT COUNT(*) FROM dbo.users) AS total_customers,
    (SELECT COUNT(*) FROM dbo.orders) AS total_orders,
    (SELECT COUNT(*) FROM dbo.orders
     WHERE status IN ('Shipped', 'Complete')) AS completed_orders,
    (SELECT COUNT(*) FROM dbo.order_items
     WHERE status IN ('Shipped', 'Complete')) AS qualifying_items,
    (SELECT SUM(sale_price) FROM dbo.order_items
     WHERE status IN ('Shipped', 'Complete')) AS total_revenue,
    (SELECT SUM(oi.sale_price - p.cost)
     FROM dbo.order_items oi
     INNER JOIN dbo.products p ON oi.product_id = p.id
     WHERE oi.status IN ('Shipped', 'Complete')) AS gross_profit;
"""

# Category performance
category_query = """
SELECT TOP 5
    p.category,
    SUM(oi.sale_price) AS revenue
FROM dbo.order_items oi
INNER JOIN dbo.products p ON oi.product_id = p.id
WHERE oi.status IN ('Shipped', 'Complete')
GROUP BY p.category
ORDER BY revenue DESC;
"""

# Order item status distribution
status_query = """
SELECT
    status,
    COUNT(*) AS total_items
FROM dbo.order_items
GROUP BY status
ORDER BY total_items DESC;
"""

# Retrieve data
kpis = pd.read_sql(kpi_query, engine)
categories = pd.read_sql(category_query, engine)
statuses = pd.read_sql(status_query, engine)

engine.dispose()

# Extract KPI values
kpi = kpis.iloc[0]

# Calculate gross profit margin
gross_profit_margin = (
    kpi["gross_profit"] / kpi["total_revenue"]
) * 100

# Display report
print("\n" + "=" * 65)
print("THELOOK E-COMMERCE: FINAL PYTHON EDA REPORT")
print("=" * 65)

print("\n1. OVERALL BUSINESS PERFORMANCE")
print("-" * 65)
print(f"Total customers: {kpi['total_customers']:,}")
print(f"Total orders: {kpi['total_orders']:,}")
print(f"Completed orders: {kpi['completed_orders']:,}")
print(f"Qualifying items sold: {kpi['qualifying_items']:,}")
print(f"Total revenue: ${kpi['total_revenue']:,.2f}")
print(f"Estimated gross profit: ${kpi['gross_profit']:,.2f}")
print(f"Estimated gross profit margin: {gross_profit_margin:.2f}%")

print("\n2. TOP 5 PRODUCT CATEGORIES")
print("-" * 65)
print(categories.to_string(index=False))

print("\n3. ORDER ITEM STATUS DISTRIBUTION")
print("-" * 65)
print(statuses.to_string(index=False))

# Export report data
with pd.ExcelWriter(
    "python_eda_summary.xlsx",
    engine="openpyxl"
) as writer:
    kpis.to_excel(writer, sheet_name="Business KPIs", index=False)
    categories.to_excel(writer, sheet_name="Top Categories", index=False)
    statuses.to_excel(writer, sheet_name="Order Item Status", index=False)

print("\n" + "=" * 65)
print("EDA REPORT COMPLETED SUCCESSFULLY")
print("Excel summary exported: python_eda_summary.xlsx")
print("=" * 65)
