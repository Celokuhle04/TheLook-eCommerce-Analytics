# TheLook eCommerce: Business Analysis Report

# Executive Summary

This project analyses the business performance of TheLook eCommerce using SQL Server and Python. The analysis evaluates sales performance, product profitability, customer purchasing behaviour, order statuses and geographic market performance.

The dataset contains 100,000 customers, 124,923 orders and 180,952 order items. The analysis identified 68,682 qualifying orders and 99,691 qualifying items, generating total sales revenue of $5,925,136.64 and an estimated gross profit of $3,073,428.77. The estimated gross profit margin was 51.87%.

Outerwear & Coats generated the highest category revenue at $706,674.90, while Suits & Sport Coats recorded a gross profit margin of 59.79%. China, the United States and Brazil were the leading revenue-generating countries, collectively contributing approximately 71.48% of total revenue.

The analysis also identified opportunities to improve order fulfilment, investigate cancellations and returns, strengthen customer retention and improve geographic data quality.

Based on these findings, the project provides practical business recommendations to support inventory planning, profitability management, customer engagement and data-driven decision-making.

## 1. Introduction

This report presents an analysis of TheLook eCommerce dataset to evaluate business performance, product performance, customer purchasing behaviour and geographic sales distribution. SQL Server and Python were used to query, analyse and interpret the data.

The analysis focuses on completed sales, defined as order items with a status of **Shipped** or **Complete**. Revenue and estimated gross profit calculations therefore exclude Processing, Cancelled and Returned items.

## 2. Business Questions and Findings

### 2.1 Order and Order-Item Status Distribution

The order status analysis identified 37,654 Shipped orders and 31,028 Complete orders. At the order-item level, 54,681 items were Shipped and 45,010 were Complete.

Shipped and Complete items represented 55.09% of all order items, while Cancelled and Returned items accounted for 25.04%.

**Business interpretation:** A considerable proportion of order items did not reach the Shipped or Complete statuses. This highlights an opportunity to investigate order cancellations and returns.

**Recommendation:** Management should investigate the main causes of cancellations and returns and identify opportunities to improve order fulfilment and customer satisfaction.

### 2.2 Overall Business Performance

The business performance analysis produced the following results:

| Metric | Result |
|---|---:|
| Total customers | 100,000 |
| Total orders | 124,923 |
| Completed orders | 68,682 |
| Qualifying items sold | 99,691 |
| Total sales revenue | $5,925,136.64 |
| Average order value | $86.27 |

The business generated approximately $5.93 million in qualifying sales revenue, with an average order value of $86.27.

**Business interpretation:** The results provide an overview of the business's sales performance and customer activity.

**Recommendation:** Management should focus on improving order completion, retaining customers and identifying opportunities to increase average order value.

### 2.3 Product Categories Generating the Highest Revenue

The five highest-revenue product categories were:

| Product category | Revenue |
|---|---:|
| Outerwear & Coats | $706,674.90 |
| Jeans | $687,533.11 |
| Sweaters | $465,310.10 |
| Suits & Sport Coats | $364,882.87 |
| Swim | $360,428.97 |

Outerwear & Coats generated the highest revenue, followed by Jeans. Together, these two categories contributed approximately 23.53% of total revenue.

**Business interpretation:** Revenue is concentrated in a number of leading product categories, particularly Outerwear & Coats and Jeans.

**Recommendation:** Management should monitor demand and inventory levels in these leading categories and investigate opportunities to sustain their sales performance.

### 2.4 Individual Products Generating the Highest Revenue

The top ten individual products generated a combined revenue of $55,097. The highest individual product revenue was $7,224, shared by two products.

Several products from Outerwear & Coats featured in the top ten, including products from The North Face and Jordan.

**Business interpretation:** A relatively small group of individual products makes a notable contribution to sales among the leading products. Outerwear products feature prominently in this group.

**Recommendation:** Management should monitor the availability and sales performance of these leading products and investigate whether targeted promotions could support continued demand.

### 2.5 Product Categories Generating the Highest Gross Profit and Margins

The profitability analysis measured estimated gross profit as selling price less product cost.

Selected results include:

| Product category | Gross profit | Gross profit margin |
|---|---:|---:|
| Outerwear & Coats | $392,997.31 | 55.61% |
| Jeans | $319,676.67 | 46.50% |
| Suits & Sport Coats | $218,177.95 | 59.79% |

Outerwear & Coats generated the highest gross profit among these categories, while Suits & Sport Coats recorded the highest gross profit margin of the three.

**Business interpretation:** The category generating the highest revenue does not necessarily have the highest gross profit margin. Therefore, evaluating categories using revenue alone may overlook differences in profitability.

**Recommendation:** Management should consider both revenue and gross profit margin when making product assortment, pricing and inventory decisions.

*Note: Gross profit is an estimate based on product selling prices less product costs. It does not account for other operating expenses and should not be interpreted as net profit.*

### 2.6 Revenue Trends Over Time

The monthly revenue analysis covered the period from January 2019 to June 2022, representing 42 months of sales data.

The business generated an average monthly revenue of approximately $141,074.68. May 2022 recorded the highest monthly revenue of $584,566.79, while June 2022 recorded $338,563.02.

**Business interpretation:** Monthly revenue varied throughout the analysis period, with May 2022 recording a particularly strong performance. However, June 2022 represents only a partial month in the dataset, so its revenue should not be directly compared with complete months.

**Recommendation:** Management should monitor monthly revenue trends to identify periods of strong and weak sales performance. This information can support sales forecasting, inventory planning and the timing of promotional activities.

### 2.7 Customers Generating the Highest Revenue

The customer revenue analysis identified the ten customers generating the highest revenue from Shipped and Complete order items.

Gabriel Navarro ranked first, generating $1,546.46 from 10 items across four orders. Joseph Hancock ranked second with $1,474.62 from nine items across four orders.

The average revenue generated by the top ten customers was approximately $1,342.42.

**Business interpretation:** The results identify customers who contributed the highest revenue during the analysis period. However, high revenue alone does not establish long-term customer loyalty or purchasing behaviour.

**Recommendation:** Management should analyse the purchasing patterns of high-revenue customers and consider targeted customer retention initiatives to encourage repeat purchases.

### 2.8 Distribution of Returns and Cancellations

The order-item status analysis identified 27,133 Cancelled items and 18,187 Returned items. Together, these accounted for 45,320 order items.

The total recorded sales value associated with Cancelled items was $1,620,562.87, while Returned items accounted for $1,084,094.93.

**Business interpretation:** Cancellations and returns represent a considerable proportion of order items. The associated sales values indicate the scale of transactions recorded under these statuses, but they should not automatically be interpreted as confirmed financial losses or refunded amounts.

**Recommendation:** Management should investigate the main reasons for cancellations and returns, including possible product-related issues, delivery problems and customer dissatisfaction. This could help identify opportunities to improve fulfilment processes and reduce avoidable returns.

### 2.9 Percentage of Order Items Returned or Cancelled

The analysis showed the following distribution across all 180,952 order items:

| Status | Order items | Percentage |
|---|---:|---:|
| Shipped | 54,681 | 30.22% |
| Complete | 45,010 | 24.87% |
| Processing | 35,941 | 19.86% |
| Cancelled | 27,133 | 14.99% |
| Returned | 18,187 | 10.05% |

Cancelled items represented 14.99% of all order items, while Returned items represented 10.05%. Combined, they accounted for approximately 25.04% of the dataset.

**Business interpretation:** Approximately one in four recorded order items had a Cancelled or Returned status. This highlights an area that requires further investigation to understand the factors contributing to these outcomes.

**Recommendation:** Management should monitor cancellation and return rates regularly, identify products and categories with unusually high rates, and investigate the underlying causes. These insights could support improvements in product descriptions, quality control and order fulfilment.

### 2.10 Countries Generating the Highest Revenue

The geographic sales analysis identified China, the United States and Brazil as the three highest-revenue countries.

| Country | Customers | Revenue |
|---|---:|---:|
| China | 17,918 | $2,027,419.22 |
| United States | 11,732 | $1,321,335.24 |
| Brazil | 7,788 | $886,882.49 |

China generated the highest revenue, followed by the United States and Brazil. Together, these three countries contributed approximately 71.48% of total business revenue.

**Business interpretation:** Revenue is concentrated in a small number of major geographic markets, with China contributing the largest share.

**Recommendation:** Management should prioritise understanding customer demand in these leading markets while exploring opportunities to grow revenue in other countries. Inventory allocation and marketing strategies should consider differences in market demand.

### 2.11 States Generating the Highest Revenue

The geographic analysis identified Guangdong in China as the highest-revenue state, generating $304,596.93 from 2,768 customers and 3,591 orders.

Other strong-performing regions included England in the United Kingdom, California in the United States and Shanghai in China.

| Country | State | Customers | Revenue |
|---|---|---:|---:|
| China | Guangdong | 2,768 | $304,596.93 |
| United Kingdom | England | 2,168 | $244,099.73 |
| United States | California | 1,934 | $214,307.16 |
| China | Shanghai | 1,313 | $147,098.20 |
| United States | Texas | 1,276 | $141,213.50 |

**Business interpretation:** Revenue varies across geographic regions, with Guangdong recording the highest revenue among the 15 country-state combinations analysed. China, the United States and Brazil appear repeatedly among the leading regions.

**Recommendation:** Management should consider regional sales performance when planning marketing campaigns and inventory distribution. However, geographic data accuracy should be checked before making major location-specific business decisions.

### 2.12 Cities Generating the Highest Revenue

The city-level analysis identified Seoul, South Korea, as the highest-revenue city, generating $81,101.83 from 726 customers and 949 orders.

Other leading cities included New York, Tokyo, London and Salvador.

| Country | City | Customers | Revenue |
|---|---|---:|---:|
| South Korea | Seoul | 726 | $81,101.83 |
| United States | New York | 416 | $49,420.89 |
| Japan | Tokyo | 429 | $46,598.14 |
| United Kingdom | London | 265 | $32,859.39 |
| Brasil | Salvador | 267 | $30,803.30 |

**Business interpretation:** Revenue is distributed across several international cities, with Seoul generating the highest revenue among the cities analysed. The results also show that major cities in the United States, Japan and the United Kingdom contribute to business sales.

**Recommendation:** Management should evaluate city-level demand when planning regional marketing and inventory strategies. However, geographic data inconsistencies should be addressed before making major location-specific decisions.

### 2.13 Customer Distribution by Country

The customer distribution analysis showed that China had the largest customer base, with 34,040 customers, followed by the United States with 22,400 and Brazil with 14,784.

| Country | Total customers | Total states | Total cities |
|---|---:|---:|---:|
| China | 34,040 | 32 | 255 |
| United States | 22,400 | 51 | 2,475 |
| Brasil | 14,784 | 27 | 735 |
| South Korea | 5,244 | 16 | 85 |
| France | 4,753 | 13 | 1,228 |
| United Kingdom | 4,609 | 4 | 604 |
| Germany | 4,159 | 16 | 783 |
| Spain | 3,953 | 20 | 777 |
| Japan | 2,388 | 35 | 208 |
| Australia | 2,156 | 8 | 423 |

**Business interpretation:** The customer base is concentrated in China, the United States and Brazil. Together, these three countries account for 71.22% of the 100,000 customers in the dataset.

**Recommendation:** Management should prioritise customer engagement and retention strategies in countries with the largest customer bases while exploring opportunities to expand into smaller markets. Geographic data should also be validated before making decisions based on the number of states and cities.

### 2.14 Average Revenue per Customer by Country

The analysis compared total revenue with the number of customers who made qualifying purchases in each country.

| Country | Customers | Revenue | Revenue per customer |
|---|---:|---:|---:|
| Colombia | 5 | $600.23 | $120.05 |
| Spain | 2,078 | $239,123.71 | $115.07 |
| Brasil | 7,788 | $886,882.49 | $113.88 |
| China | 17,918 | $2,027,419.22 | $113.15 |
| Belgium | 690 | $77,868.58 | $112.85 |
| United States | 11,732 | $1,321,335.24 | $112.63 |
| United Kingdom | 2,432 | $273,015.88 | $112.26 |
| Japan | 1,280 | $142,342.66 | $111.21 |
| Germany | 2,200 | $243,193.58 | $110.54 |
| Australia | 1,162 | $127,020.00 | $109.31 |
| South Korea | 2,776 | $303,138.63 | $109.20 |
| France | 2,514 | $269,890.22 | $107.35 |
| Poland | 129 | $13,286.70 | $103.00 |
| Austria | 1 | $19.50 | $19.50 |

**Business interpretation:** Colombia recorded the highest average revenue per customer at $120.05, but this result was based on only five purchasing customers. Among countries with larger customer bases, Spain recorded the highest average revenue per customer at $115.07, followed by Brazil at $113.88 and China at $113.15.

**Recommendation:** Management should investigate the purchasing behaviour of customers in Spain and Brazil to identify practices that could be applied to other markets. Countries with very small customer bases should be evaluated cautiously because their average revenue figures may not represent broader market performance.

## 3. Business Recommendations

Based on the findings of the SQL and Python analysis, the following recommendations are proposed to improve business performance and support data-driven decision-making.

### 3.1 Improve Order Fulfilment and Reduce Returns

Cancelled and Returned items account for approximately 25.04% of all recorded order items. Management should investigate the main causes of cancellations and returns, monitor these rates regularly and identify opportunities to improve product quality, order processing and delivery.

### 3.2 Prioritise High-Revenue Product Categories

Outerwear & Coats and Jeans are the two highest-revenue categories, contributing approximately 23.53% of total revenue. Management should monitor demand, maintain appropriate inventory levels and consider targeted marketing campaigns to support these categories.

### 3.3 Consider Profitability in Product Decisions

Suits & Sport Coats recorded a gross profit margin of 59.79%, while Outerwear & Coats generated the highest gross profit at $392,997.31. Management should consider both revenue and gross profit margins when making pricing, inventory and product assortment decisions rather than focusing exclusively on sales revenue.

### 3.4 Strengthen Customer Retention

The analysis identified customers who generated the highest revenue, with Gabriel Navarro leading at $1,546.46. Management should examine the purchasing patterns of high-revenue customers and introduce appropriate customer engagement and retention initiatives to encourage repeat purchases.

### 3.5 Focus on Major Geographic Markets

China, the United States and Brazil collectively generated approximately 71.48% of total revenue. Management should prioritise understanding demand in these markets and use regional sales information to guide marketing and inventory allocation decisions.

### 3.6 Investigate Opportunities in High-Value Customer Markets

Spain recorded the highest average revenue per customer among countries with substantial purchasing customer bases, at $115.07. Management should investigate customer purchasing behaviour in Spain and Brazil to identify opportunities to improve revenue per customer in other markets.

### 3.7 Improve Data Quality

The geographic analysis revealed inconsistencies in some city and state combinations. Management should improve the validation of customer location information to ensure that geographic reporting and future business decisions are based on reliable data.

## 4. Conclusion

The analysis provided an overview of TheLook eCommerce's business performance using SQL Server and Python. The business generated $5.93 million in qualifying sales revenue and an estimated gross profit of $3.07 million, with an estimated gross profit margin of 51.87%.

The findings identified leading product categories, high-revenue customers, important geographic markets and opportunities to improve order fulfilment. Overall, the analysis demonstrates how data analytics can support business performance evaluation, identify areas requiring attention and inform strategic decision-making.