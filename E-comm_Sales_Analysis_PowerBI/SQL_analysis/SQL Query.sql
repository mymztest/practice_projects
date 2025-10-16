use amazon;
SELECT Category, sum(Qty) as Quantity, SUM(Qty * Amount) AS total_revenue FROM amazon_sales GROUP BY Category order by total_revenue desc;

SELECT month, SUM(Qty * Amount) AS total_sales FROM amazon_sales WHERE Courier_Status = "Shipped" GROUP BY month ORDER BY total_sales desc;

SELECT Category, SUM(Qty * Amount) AS monthly_total_sales, month FROM amazon_sales GROUP BY Category, month ORDER BY monthly_total_sales desc;

SELECT Fulfilment, Count(Fulfilment), SUM(Amount) As total_sales, SUM(Qty * Amount) as Revenue, Courier_Status 
FROM amazon_sales GROUP BY Fulfilment, Courier_Status ORDER BY total_sales desc;

SELECT Courier_Status, (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM amazon_sales)) AS percentage 
FROM amazon_sales 
WHERE Courier_Status IN ("Shipped","Cancelled") GROUP BY Courier_Status;

select Category, count(Category) As total_products, Max(Qty), Courier_Status, B2B
from amazon_sales where B2B = 'True' group by Category, Courier_Status, B2B order by total_products desc;

select * from (
SELECT Category, SUM(Qty * Amount) AS total_revenue, RANK() 
OVER (order BY SUM(Qty * Amount) DESC) As rank1 
FROM amazon_sales WHERE Courier_Status = "Shipped" GROUP BY Category order by rank1) data
where rank1 <= 5;


select * from (SELECT Category, SUM(Qty) AS total_quantity, RANK() 
OVER (order BY SUM(Qty) DESC) As rank1 FROM amazon_sales GROUP BY Category order by rank1) data where rank1 <= 5;


SELECT Category, 
       SUM(CASE WHEN MONTH(Date) = 1 THEN Amount ELSE 0 END) AS Jan_Revenue,
       SUM(CASE WHEN MONTH(Date) = 2 THEN Amount ELSE 0 END) AS Feb_Revenue,
       SUM(CASE WHEN MONTH(Date) = 3 THEN Amount ELSE 0 END) AS Mar_Revenue,
       SUM(CASE WHEN MONTH(Date) = 4 THEN Amount ELSE 0 END) AS Apr_Revenue,
       SUM(CASE WHEN MONTH(Date) = 5 THEN Amount ELSE 0 END) AS May_Revenue,
       SUM(CASE WHEN MONTH(Date) = 6 THEN Amount ELSE 0 END) AS Jun_Revenue,
       SUM(CASE WHEN MONTH(Date) = 7 THEN Amount ELSE 0 END) AS Jul_Revenue,
       SUM(CASE WHEN MONTH(Date) = 8 THEN Amount ELSE 0 END) AS Aug_Revenue,
       SUM(CASE WHEN MONTH(Date) = 9 THEN Amount ELSE 0 END) AS Sep_Revenue,
       SUM(CASE WHEN MONTH(Date) = 10 THEN Amount ELSE 0 END) AS Oct_Revenue,
       SUM(CASE WHEN MONTH(Date) = 11 THEN Amount ELSE 0 END) AS Nov_Revenue,
       SUM(CASE WHEN MONTH(Date) = 12 THEN Amount ELSE 0 END) AS Dec_Revenue FROM amazon_sales WHERE Courier_Status = "Shipped" GROUP BY Category
ORDER BY Category;