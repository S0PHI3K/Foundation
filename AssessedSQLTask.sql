# Create an SQL query that shows the TOP 3 authors who sold the most books in total!


SELECT SUM(b.sold_copies), a.author_name  
FROM Authors a
INNER JOIN
Books b 
ON
b.book_name = a.book_name
GROUP BY
a.author_name
ORDER BY 
b.sold_copies DESC LIMIT 3;
