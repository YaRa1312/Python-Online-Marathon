---------------------------------------------------- 1 ----------------------------------------------------

/*
Given a database with (at least) two tables: customers and orders as shown below, write an SQL query that returns the customer name, city and amount for all orders between $100 and $3500 inclusive, grouped by name and ordered by city.

result for example

name                  city                  totalSum
--------------------  --------------------  ---------------
Graham Zusi           California            261
Jozy Altidore         Kyiv                  2000.0
Brad Guzan            London                270.65
Julian Green          London                250.45
Nick Rimando          New York              3210.86

First 5 rows of "customers" table, ordered by id
id      name             city          grade   salesperson_id
------  ---------------  ------------  ------  --------------
3001    Brad Guzan       London        100     5005
3002    Nick Rimando     New York      100     5001
3003    Jozy Altidore    Kyiv          200     5007
3004    Fabian Johns     Paris         300     5006
3005    Graham Zusi      California    200     5002 
First 5 rows of "orders" table ordered by order_num
order_num   amount     date        customer_id  saleperson_id
----------  ---------  ----------  -----------  -------------
70001       150.5      2022-10-05  3005         5002
70002       65.26      2022-10-05  3002         5001
70003       2480.4     2022-10-10  3009         5003
70004       110.5      2022-08-17  3005         5003
70005       2400.6     2022-07-27  3007         5001
For example:

Test	Result
-- Testing with original db
name                  city                  totalSum
--------------------  --------------------  ---------------
Geoff Cameron         Berlin                2590.9
Graham Zusi           California            1099.0
Brad Guzan            London                270.65
Julian Green          London                250.45
Brad Davis            New York              2400.6
Nick Rimando          New York              3210.86
Fabian Johns          Paris                 1983.43
*/


-- SELECT name, city FROM customers
-- WHERE amount BETWEEN 100 AND 3500


-- SELECT  customers.name, customers.city, orders.amount
--  FROM customers
-- --  JOIN orders ON  customers.salesperson_id=orders.saleperson_id WHERE orders.amount > 100 OR orders.amount < 3500
--  JOIN orders ON  customers.salesperson_id=orders.saleperson_id
--  WHERE orders.amount > 100 AND  orders.order_num = 70005 OR  orders.order_num = 70003 OR  orders.order_num = 70001 OR saleperson_id = 5005 or saleperson_id = 5006 or saleperson_id = 5007
--  ORDER BY customers.city 
 



-- SELECT distinct customers.name, customers.city,  Sum(orders.amount)
--  FROM customers
--  inner JOIN orders ON  customers.salesperson_id=orders.saleperson_id WHERE orders.amount > 99 and orders.amount < 3500
--  --JOIN orders ON  customers.salesperson_id=orders.saleperson_id
--  --WHERE orders.amount > 100 AND  orders.order_num = 70005 OR  orders.order_num = 70003 OR  orders.order_num = 70001 OR saleperson_id = 5005 or saleperson_id = 5006 or saleperson_id = 5007
--  Group by customers.name
--  ORDER BY customers.city 



SELECT customers.name, customers.city, SUM(orders.amount) AS totalSum
FROM customers
JOIN orders ON customers.id=orders.customer_id
WHERE orders.amount BETWEEN 100 AND 3500
GROUP BY customers.name ORDER BY customers.city

/*
Test	Expected	Got	
-- Testing with original db
name                  city                  totalSum
--------------------  --------------------  ---------------
Geoff Cameron         Berlin                2590.9
Graham Zusi           California            1099.0
Brad Guzan            London                270.65
Julian Green          London                250.45
Brad Davis            New York              2400.6
Nick Rimando          New York              3210.86
Fabian Johns          Paris                 1983.43
name                  city                  totalSum
--------------------  --------------------  ---------------
Geoff Cameron         Berlin                2590.9
Graham Zusi           California            1099.0
Brad Guzan            London                270.65
Julian Green          London                250.45
Brad Davis            New York              2400.6
Nick Rimando          New York              3210.86
Fabian Johns          Paris                 1983.43
-- Testing with extra rows
name                  city                  totalSum
--------------------  --------------------  ---------------
Geoff Cameron         Berlin                2590.9
Graham Zusi           California            1599.0
Jozy Altidore         Kyiv                  2000.0
Brad Guzan            London                270.65
Julian Green          London                250.45
Brad Davis            New York              2400.6
Nick Rimando          New York              3210.86
Fabian Johns          Paris                 1983.43
name                  city                  totalSum
--------------------  --------------------  ---------------
Geoff Cameron         Berlin                2590.9
Graham Zusi           California            1599.0
Jozy Altidore         Kyiv                  2000.0
Brad Guzan            London                270.65
Julian Green          London                250.45
Brad Davis            New York              2400.6
Nick Rimando          New York              3210.86
Fabian Johns          Paris                 1983.43
*/
