-- Check order statuses
SELECT
    status,
    COUNT(*) AS total_orders
FROM dbo.orders
GROUP BY status
ORDER BY total_orders DESC;


-- Check order item statuses
SELECT
    status,
    COUNT(*) AS total_order_items
FROM dbo.order_items
GROUP BY status
ORDER BY total_order_items DESC;


-- =====================================================
-- THELOOK ECOMMERCE ANALYSIS
-- 01: BUSINESS PERFORMANCE OVERVIEW
-- =====================================================


-- BUSINESS QUESTION 1:
-- What is the distribution of orders and order items
-- across different statuses?

-- Order status distribution
SELECT
    status,
    COUNT(*) AS total_orders
FROM dbo.orders
GROUP BY status
ORDER BY total_orders DESC;


-- Order item status distribution
SELECT
    status,
    COUNT(*) AS total_order_items
FROM dbo.order_items
GROUP BY status
ORDER BY total_order_items DESC;


-- BUSINESS QUESTION 2:
-- How is the business performing in terms of customers,
-- orders, completed sales revenue and average order value?

-- Business Performance KPIs
SELECT
    (SELECT COUNT(*)
     FROM dbo.users) AS total_customers,

    (SELECT COUNT(*)
     FROM dbo.orders) AS total_orders,

    (SELECT COUNT(*)
     FROM dbo.orders
     WHERE status IN ('Shipped', 'Complete')
    ) AS completed_orders,

    (SELECT SUM(sale_price)
     FROM dbo.order_items
     WHERE status IN ('Shipped', 'Complete')
    ) AS total_sales_revenue,

    (SELECT
        CAST(SUM(sale_price) AS DECIMAL(18,2))
        / NULLIF(COUNT(DISTINCT order_id), 0)
     FROM dbo.order_items
     WHERE status IN ('Shipped', 'Complete')
    ) AS average_order_value;

    
-- BUSINESS QUESTION 3:
-- Which product categories generate the highest revenue?

SELECT
    p.category,
    COUNT(*) AS total_items_sold,
    COUNT(DISTINCT oi.order_id) AS total_orders,
    SUM(oi.sale_price) AS total_revenue,
    AVG(oi.sale_price) AS average_item_price
FROM dbo.order_items oi
INNER JOIN dbo.products p
    ON oi.product_id = p.id
WHERE oi.status IN ('Shipped', 'Complete')
GROUP BY p.category
ORDER BY total_revenue DESC;


-- BUSINESS QUESTION 4:
-- Which individual products generate the highest revenue?

SELECT TOP 10
    p.id AS product_id,
    p.name AS product_name,
    p.category,
    p.brand,
    COUNT(*) AS total_items_sold,
    SUM(oi.sale_price) AS total_revenue,
    AVG(oi.sale_price) AS average_selling_price
FROM dbo.order_items oi
INNER JOIN dbo.products p
    ON oi.product_id = p.id
WHERE oi.status IN ('Shipped', 'Complete')
GROUP BY
    p.id,
    p.name,
    p.category,
    p.brand
ORDER BY total_revenue DESC;


-- BUSINESS QUESTION 5:
-- Which product categories generate the highest
-- gross profit and gross profit margins?

SELECT
    p.category,
    COUNT(*) AS total_items_sold,
    SUM(oi.sale_price) AS total_revenue,
    SUM(p.cost) AS total_product_cost,

    SUM(oi.sale_price - p.cost) AS gross_profit,

    CAST(
        SUM(oi.sale_price - p.cost) * 100.0
        / NULLIF(SUM(oi.sale_price), 0)
        AS DECIMAL(10,2)
    ) AS gross_profit_margin

FROM dbo.order_items oi
INNER JOIN dbo.products p
    ON oi.product_id = p.id

WHERE oi.status IN ('Shipped', 'Complete')

GROUP BY p.category
ORDER BY gross_profit DESC;


-- BUSINESS QUESTION 6:
-- How does revenue change over time?

SELECT
    YEAR(oi.created_at) AS sales_year,
    MONTH(oi.created_at) AS sales_month,
    DATENAME(MONTH, oi.created_at) AS month_name,

    COUNT(*) AS total_items_sold,

    COUNT(DISTINCT oi.order_id) AS total_orders,

    SUM(oi.sale_price) AS total_revenue,

    SUM(oi.sale_price - p.cost) AS gross_profit

FROM dbo.order_items oi

INNER JOIN dbo.products p
    ON oi.product_id = p.id

WHERE oi.status IN ('Shipped', 'Complete')

GROUP BY
    YEAR(oi.created_at),
    MONTH(oi.created_at),
    DATENAME(MONTH, oi.created_at)

ORDER BY
    sales_year,
    sales_month;


    SELECT
    MIN(created_at) AS first_order_item_date,
    MAX(created_at) AS last_order_item_date,
    COUNT(DISTINCT YEAR(created_at) * 100 + MONTH(created_at))
        AS total_months
FROM dbo.order_items
WHERE status IN ('Shipped', 'Complete');

-- BUSINESS QUESTION 7:
-- Which customers generate the most revenue?

SELECT TOP 10
    u.id AS customer_id,
    u.first_name,
    u.last_name,
    COUNT(DISTINCT oi.order_id) AS total_orders,
    COUNT(*) AS total_items_purchased,
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

-- BUSINESS QUESTION 8:
-- What is the distribution of returns and cancellations?

SELECT
    status,
    COUNT(*) AS total_order_items,
    SUM(sale_price) AS total_sales_value,
    AVG(sale_price) AS average_item_value
FROM dbo.order_items
GROUP BY status
ORDER BY total_order_items DESC;

-- BUSINESS QUESTION 9:
-- What percentage of order items are returned or cancelled?

SELECT
    status,
    COUNT(*) AS total_order_items,
    CAST(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM dbo.order_items)
        AS DECIMAL(10,2)
    ) AS percentage_of_items
FROM dbo.order_items
GROUP BY status
ORDER BY percentage_of_items DESC;

-- BUSINESS QUESTION 10:
-- Which countries generate the most revenue?

SELECT
    u.country,
    COUNT(DISTINCT u.id) AS total_customers,
    COUNT(DISTINCT oi.order_id) AS total_orders,
    COUNT(*) AS total_items_sold,
    SUM(oi.sale_price) AS total_revenue,
    SUM(oi.sale_price - p.cost) AS gross_profit
FROM dbo.order_items oi
INNER JOIN dbo.users u
    ON oi.user_id = u.id
INNER JOIN dbo.products p
    ON oi.product_id = p.id
WHERE oi.status IN ('Shipped', 'Complete')
GROUP BY u.country
ORDER BY total_revenue DESC;

-- BUSINESS QUESTION 11:
-- Which states generate the most revenue?

SELECT TOP 15
    u.country,
    u.state,
    COUNT(DISTINCT u.id) AS total_customers,
    COUNT(DISTINCT oi.order_id) AS total_orders,
    SUM(oi.sale_price) AS total_revenue,
    SUM(oi.sale_price - p.cost) AS gross_profit
FROM dbo.order_items oi
INNER JOIN dbo.users u
    ON oi.user_id = u.id
INNER JOIN dbo.products p
    ON oi.product_id = p.id
WHERE oi.status IN ('Shipped', 'Complete')
GROUP BY
    u.country,
    u.state
ORDER BY total_revenue DESC;

-- BUSINESS QUESTION 12:
-- Which cities generate the most revenue?

SELECT TOP 15
    u.country,
    u.state,
    u.city,
    COUNT(DISTINCT u.id) AS total_customers,
    COUNT(DISTINCT oi.order_id) AS total_orders,
    SUM(oi.sale_price) AS total_revenue,
    SUM(oi.sale_price - p.cost) AS gross_profit
FROM dbo.order_items oi
INNER JOIN dbo.users u
    ON oi.user_id = u.id
INNER JOIN dbo.products p
    ON oi.product_id = p.id
WHERE oi.status IN ('Shipped', 'Complete')
GROUP BY
    u.country,
    u.state,
    u.city
ORDER BY total_revenue DESC;

-- BUSINESS QUESTION 13:
-- Customer distribution by country

SELECT
    country,
    COUNT(*) AS total_customers,
    COUNT(DISTINCT state) AS total_states,
    COUNT(DISTINCT city) AS total_cities
FROM dbo.users
GROUP BY country
ORDER BY total_customers DESC;

-- BUSINESS QUESTION 14:
-- Average revenue per customer by country

SELECT
    u.country,
    COUNT(DISTINCT u.id) AS total_customers,
    SUM(oi.sale_price) AS total_revenue,
    CAST(
        SUM(oi.sale_price) /
        NULLIF(COUNT(DISTINCT u.id), 0)
        AS DECIMAL(18,2)
    ) AS revenue_per_customer
FROM dbo.order_items oi
INNER JOIN dbo.users u
    ON oi.user_id = u.id
WHERE oi.status IN ('Shipped', 'Complete')
GROUP BY u.country
ORDER BY revenue_per_customer DESC;

-- FINAL SQL VALIDATION:
-- Verify total revenue and gross profit

SELECT
    COUNT(*) AS total_qualifying_items,
    COUNT(DISTINCT order_id) AS total_qualifying_orders,
    SUM(sale_price) AS total_revenue,
    SUM(sale_price - p.cost) AS total_gross_profit
FROM dbo.order_items oi
INNER JOIN dbo.products p
    ON oi.product_id = p.id
WHERE oi.status IN ('Shipped', 'Complete');