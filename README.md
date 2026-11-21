# TheLook eCommerce: End-to-End Business Performance Analysis

**SQL Server • Python • Excel • Power BI • Business Analytics**

## Project Overview

This project analyses the business performance of TheLook eCommerce using SQL Server, Python, Excel and Power BI.

The objective is to transform raw e-commerce data into meaningful business insights by examining sales performance, product profitability, customer purchasing behaviour, order statuses and geographic performance.

The analysis addresses 14 business questions to identify performance trends, evaluate profitability and provide actionable business recommendations.

The project follows an end-to-end analytical workflow, from data preparation and SQL querying to Python exploratory data analysis, Excel reporting and interactive Power BI dashboards.

## Business Objectives

- Evaluate overall business performance using key performance indicators (KPIs).
- Identify the highest-revenue product categories and individual products.
- Analyse gross profit and gross profit margins.
- Examine monthly revenue trends.
- Identify high-value customers and purchasing behaviour.
- Investigate order cancellations and returns.
- Evaluate revenue and customer distribution across geographic markets.
- Develop recommendations to support business decision-making.

## Tools and Technologies

| Tool | Application |
|---|---|
| SQL Server | Data storage, querying and business analysis |
| Python | Exploratory data analysis and visualisation |
| Pandas | Data manipulation and analysis |
| Matplotlib | Data visualisation |
| Seaborn | Statistical data visualisation |
| Excel | Business analysis, reporting and visualisation |
| Power BI | Interactive dashboard development |
| Git & GitHub | Version control and project documentation |

## Dataset Overview

The dataset contains the following tables:

| Table | Records |
|---|---:|
| Users | 100,000 |
| Products | 29,120 |
| Orders | 124,923 |
| Order Items | 180,952 |
| Inventory Items | 487,901 |
| Distribution Centers | 10 |
| Events | 2,420,738 |
| **Total** | **3,625,634** |

## Key Business Findings

### Overall Business Performance

| KPI | Result |
|---|---:|
| Total Customers | 100,000 |
| Total Orders | 124,923 |
| Completed Orders | 68,682 |
| Qualifying Items Sold | 99,691 |
| Total Sales Revenue | $5,925,136.64 |
| Estimated Gross Profit | $3,073,428.77 |
| Estimated Gross Profit Margin | 51.87% |
| Average Order Value | $86.27 |

### Product Performance

- Outerwear & Coats generated the highest category revenue of $706,674.90.
- Jeans ranked second, generating $687,533.11.
- Suits & Sport Coats recorded a gross profit margin of 59.79%.
- The top ten individual products generated combined revenue of $55,097.

### Customer and Geographic Performance

- Gabriel Navarro was the highest-revenue customer, generating $1,546.46.
- China generated the highest country-level revenue at $2,027,419.22.
- China, the United States and Brazil collectively contributed approximately 71.48% of total revenue.
- Spain recorded the highest average revenue per customer among countries with substantial purchasing customer bases, at $115.07.

### Order Status Analysis

- Shipped and Complete items accounted for approximately 55.09% of all order items.
- Cancelled and Returned items accounted for approximately 25.04%.

## Business Recommendations

Based on the analysis, the project identifies opportunities to:

1. Improve order fulfilment and investigate the causes of cancellations and returns.
2. Prioritise high-revenue product categories through effective inventory planning.
3. Consider gross profit margins alongside revenue when making product decisions.
4. Strengthen customer retention and engagement strategies.
5. Focus on major geographic markets while exploring opportunities in other countries.
6. Improve geographic data quality to support reliable business reporting.

## Project Structure

```text
TheLook-eCommerce-Analytics/
│
├── data/
│    └── Original dataset CSV files
│
├── excel/
│   └── TheLook_eCommerce_Analysis.xlsx
|
├── powerbi/
│   ├── TheLook_eCommerce_Analytics.pbix
│   └── TheLook_eCommerce_Analytics.pdf
│
├── python/
│   ├── 01_connect_sql_server.py
│   ├── 02_business_kpis.py
│   ├── 03_monthly_revenue_analysis.py
│   ├── 04_category_revenue_analysis.py
│   ├── 05_customer_revenue_analysis.py
│   ├── 06_product_performance_analysis.py
│   ├── 07_customer_purchasing_behaviour.py
│   ├── 08_returns_cancellations_analysis.py
│   ├── 09_final_eda_report.py
│   └── python_eda_summary.xlsx
│
├── reports/
│   └── business_analysis_report.md
├── screenshots
│
├── sql/
│   └── 01_business_performance.sql
├── .gitignore
│
└── screenshots/
```

## Methodology

The project follows an end-to-end analytical workflow:

1. Data preparation and validation.
2. SQL-based business performance analysis.
3. Python-based exploratory data analysis.
4. Business interpretation and recommendations.
5. Excel-based analysis and reporting.
6. Power BI dashboard development.

## Key Business Metric Definitions

**Qualifying sales:** Order items with a status of `Shipped` or `Complete`.

**Total Revenue:** Sum of selling prices for qualifying order items.

**Estimated Gross Profit:** Selling price less product cost for qualifying order items.

**Estimated Gross Profit Margin:** Estimated gross profit divided by total revenue, expressed as a percentage.

**Average Order Value:** Total qualifying revenue divided by the number of distinct qualifying orders.

*Note: Estimated gross profit excludes other operating expenses and should not be interpreted as net profit. Recorded sales values associated with returned and cancelled items are not necessarily confirmed refunds or financial losses.*

## Conclusion

This project demonstrates the application of SQL Server, Python, Excel and Power BI to real-world business analytics problems. It focuses on extracting meaningful insights from e-commerce data, analysing business performance and translating analytical findings into practical recommendations that can support business decision-making.