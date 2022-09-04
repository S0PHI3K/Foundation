# A selection of sql answers given. 

# Question 1 - Find out how many sales (amount) were recorded each week, 
# per day (where available) This would look like:
#-- Week 1, Tuesday, £x
#-- Week 1, Wednesday, £x
#-- Week 2, Monday, £x
#-- Week 2, Friday, £x

SELECT sa.week, sa.day, sa.SalesAmount FROM sales1 sa
ORDER BY sa.week asc, DAYOFWEEK(sa.day);


# Question 2 - Change the name of salesperson Inga to be Annette instead, 
# but only where Ignas Sales are <50

UPDATE Sales1 sa
SET sa.SalesPerson = 'Annette'
WHERE sa.SalesPerson = 'Inga' AND sa.SalesAmount < 50;

# QUESTION 6 - For each store:
# ○ The total of their sales;
# ○ The number of sales;
# ○ Their average sales;
# ○ Their lowest sales amount;
# ○ Their highest sales amount.

SELECT sa.store, SUM(sa.SalesAmount) as 'Total Sales', 
COUNT(sa.SalesAmount) AS 'Number of Sales', 
ROUND(AVG(sa.SalesAmount),2) AS 'Average Sales', MIN(sa.SalesAmount) AS 'Lowest Sales Amount', 
MAX(sa.SalesAmount) AS 'Highest Sales Amount'
FROM Sales1 sa
GROUP BY sa.Store;

# Question 1 - Return the PartID, Colour and Supplier name, where the supplier’s surname ends in an S, and the Supplier city is not London. Ensure the values are Unique.

SELECT DISTINCT s.p_id AS 'Part ID', p.colour, sr.sname AS 'Supplier Name', sr.city AS 'Supplier City', s.s_id, p.pname
FROM supply s
INNER JOIN part p ON s.p_id = p.p_id
INNER JOIN supplier sr ON s.s_id = sr.s_id
WHERE sr.sname LIKE '%s' AND NOT sr.city = 'London'
ORDER BY s.p_id;

