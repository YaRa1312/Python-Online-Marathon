---------------------------------------------------- 2 ----------------------------------------------------

/* 
Given a database with (at least) a table customers as shown below, write an SQL query that insert in to table new customer with  name Stefan Huk ,id 3006, city Kyiv and grade 500, salesperson_id 5007  .

After insert write an SQL query that returns the all columns of all customers who live in London or Kyiv, in ascending order of id.

.

First 5 rows of customers table, ordered by id
id      name             city          grade   salesperson_id
------  ---------------  ------------  ------  --------------
3001    Brad Guzan       London        100     5005
3002    Nick Rimando     New York      100     5001
3003    Jozy Altidore    Kyiv          200     5007
3004    Fabian Johns     Paris         300     5006
3005    Graham Zusi      California    200     5002 

For example:

Test	Result
-- Testing with original db
id               name        city   grade       salesperson_id
---------------  ----------  -----  ----------  --------------
3001             Brad Guzan  Londo  100         5005
3006             Stefan Huk  Kyiv   500         5007
3008             Julian Gre  Londo  300         5002
*/

INSERT INTO customers (id, name, city, grade, salesperson_id)
VALUES (3006, "Stefan Huk", "Kyiv", 500, 5007);
SELECT * FROM customers WHERE city = "London" OR city = "Kyiv" ORDER BY id

/*
Test	Expected	Got	
-- Testing with original db
id               name        city   grade       salesperson_id
---------------  ----------  -----  ----------  --------------
3001             Brad Guzan  Londo  100         5005
3006             Stefan Huk  Kyiv   500         5007
3008             Julian Gre  Londo  300         5002
id               name        city   grade       salesperson_id
---------------  ----------  -----  ----------  --------------
3001             Brad Guzan  Londo  100         5005
3006             Stefan Huk  Kyiv   500         5007
3008             Julian Gre  Londo  300         5002
-- Testing with extra rows
id               name        city   grade       salesperson_id
---------------  ----------  -----  ----------  --------------
2999             Angus McGe  Londo  500         6001
3001             Brad Guzan  Londo  100         5005
3006             Stefan Huk  Kyiv   500         5007
3008             Julian Gre  Londo  300         5002
id               name        city   grade       salesperson_id
---------------  ----------  -----  ----------  --------------
2999             Angus McGe  Londo  500         6001
3001             Brad Guzan  Londo  100         5005
3006             Stefan Huk  Kyiv   500         5007
*/