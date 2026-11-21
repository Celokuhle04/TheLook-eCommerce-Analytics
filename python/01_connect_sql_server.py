
import pyodbc
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# SQL Server connection details
server = r"localhost\SQLEXPRESS"
database = "TheLookEcommerce"
driver = "ODBC Driver 18 for SQL Server"

# Windows Authentication connection
connection_string = (
    f"DRIVER={{{driver}}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

# Create SQLAlchemy engine
connection_url = quote_plus(connection_string)
engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={connection_url}"
)

# Test the connection
try:
    with engine.connect() as connection:
        result = connection.exec_driver_sql(
            "SELECT DB_NAME() AS database_name"
        )
        print("Connection successful!")
        print("Connected database:", result.scalar())

except Exception as error:
    print("Connection failed:")
    print(error)
