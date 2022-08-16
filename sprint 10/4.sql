---------------------------------------------------- 4 ----------------------------------------------------

/*
Given a database with (at least) a table customers as shown below, write an SQL query that returns the name, city and grade of all customers who live in London or Paris, in ascending order of name.

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
name             city        grade
---------------  ----------  -----
Brad Guzan       London      100
Fabian Johns     Paris       300
Julian Green     London      300
*/

SELECT name, city, grade
FROM customers
WHERE city like '%Par%'OR city like '%Lon%'
ORDER BY name

/*
Test	Expected	Got	
-- Testing with original db
name             city        grade
---------------  ----------  -----
Brad Guzan       London      100
Fabian Johns     Paris       300
Julian Green     London      300
name             city        grade
---------------  ----------  -----
Brad Guzan       London      100
Fabian Johns     Paris       300
Julian Green     London      300
-- Testing with extra rows
name             city        grade
---------------  ----------  -----
Angus McGee      Paris       500
Brad Guzan       London      100
Fabian Johns     Paris       300
Julian Green     London      300
name             city        grade
---------------  ----------  -----
Angus McGee      Paris       500
Brad Guzan       London      100
Fabian Johns     Paris       300
Julian Green     London      300
*/
