SET GLOBAL sql_mode = '';


CREATE SCHEMA portfolio_project;

ALTER TABLE walmart_sales
CHANGE `Product Line` `product_line` varchar(250);

SELECT 
    *
FROM
    portfolio_project.walmart_sales;

SELECT 
    time,
    (CASE
        WHEN 'time' BETWEEN '00:00:00:' AND '12:00:00' THEN 'Morning'
        WHEN 'time' BETWEEN '12:00:00' AND '17:00:00' THEN 'Afternoon'
        ELSE 'Evening'
    END) AS time_of_day
FROM
    walmart_sales;
    
ALTER TABLE walmart_sales add column time_of_day varchar(20);

UPDATE walmart_sales 
SET 
    time_of_day = (CASE
        WHEN 'time' BETWEEN '00:00:00:' AND '12:00:00' THEN 'Morning'
        WHEN 'time' BETWEEN '12:00:00' AND '17:00:00' THEN 'Afternoon'
        ELSE 'Evening'
    END);

SELECT 
    `date`, DAYNAME(date)
FROM
    walmart_sales;
    
alter table walmart_sales add column Day varchar(20);

UPDATE walmart_sales 
SET 
    Day = DAYNAME(date);

alter table walmart_sales add column Month varchar(20);

UPDATE walmart_sales 
SET 
    Month = MONTHNAME(date);

SELECT 
    *
FROM
    walmart_sales;

SELECT DISTINCT
    city, branch
FROM
    walmart_sales;

SELECT DISTINCT
    product_line, SUM(cogs)
FROM
    walmart_sales
GROUP BY product_line
ORDER BY SUM(cogs) DESC;

SELECT
	DISTINCT day,
    sum(cogs)
FROM
	walmart_sales
WHERE
	month = 'March'
GROUP BY day 
order by sum(cogs) desc; 

SELECT
	distinct month,
    sum(cogs)
FROM
	walmart_sales
GROUP BY month
ORDER BY sum(cogs) desc;

SELECT
	sum(quantity) as qty,
    product_line
FROM
	walmart_sales
GROUP BY product_line 
ORDER BY qty desc;

SELECT
	distinct product_line,
    sum(total) as revenue
from
	walmart_sales
group by product_line
order by revenue desc;

alter table walmart_sales
add column profit decimal(10,2);

UPDATE walmart_sales 
SET 
    profit = total - cogs;
    
SELECT DISTINCT
    product_line, SUM(profit)
FROM
    walmart_sales
GROUP BY product_line
ORDER BY SUM(profit) DESC;

SELECT
	product_line,
    avg(quantity)
from
	walmart_sales
group by product_line
order by avg(quantity) desc;

SELECT
	product_line,
    (CASE
    WHEN avg(quantity) >= 3 then 'Good'
    ELSE 'Bad'
    END) as Remark
FROM
	walmart_sales
GROUP BY product_line
ORDER BY avg(quantity);

SELECT 
    *
FROM
    walmart_sales;