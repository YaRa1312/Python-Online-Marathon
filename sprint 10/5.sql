---------------------------------------------------- 5 ----------------------------------------------------
/*
Given a database with (at least) a table "customers" as shown below, write an SQL query that Update in to "customers" table , a customer  named Jozy Altidore ,id 3003, from city Kyiv to city Paris and from grade 500 to grade 300 , salesperson_id 5007  .

After Update write an SQL query that returns the columns name, city and grade of all customers who live in London or Paris, in ascending order of id.

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
name                  city             grade
--------------------  ---------------  ----------
Brad Guzan            London           100
Jozy Altidore         Paris            300
Fabian Johns          Paris            300
Julian Green          London           300
*/


-- UPDATE customers
-- SET  city  = 'Paris', id = 3003,.
-- WHERE name like 'Jozy Altidore';


-- UPDATE customers
-- SET  city  = 'London '
-- WHERE name like 'Jozy Altidore';

-- select distinct name, city, grade from customers order by id

UPDATE customers
SET city = 'Paris', grade = 300
WHERE id = 3003;
SELECT name, city, grade
FROM customers
WHERE city LIKE '%Lon%' OR city LIKE '%Par%'
ORDER BY id

-- SELECT *
-- FROM customers
-- -- SET city = 'Paris', grade = 300
-- WHERE id = 3003

/*
Test	Expected	Got	
-- Testing with original db
name                  city             grade
--------------------  ---------------  ----------
Brad Guzan            London           100
Jozy Altidore         Paris            300
Fabian Johns          Paris            300
Julian Green          London           300
name                  city             grade
--------------------  ---------------  ----------
Brad Guzan            London           100
Jozy Altidore         Paris            300
Fabian Johns          Paris            300
Julian Green          London           300
-- Testing with extra rows
name                  city             grade
--------------------  ---------------  ----------
Angus McGee           London           500
Brad Guzan            London           100
Jozy Altidore         Paris            300
Fabian Johns          Paris            300
Julian Green          London           300
name                  city             grade
--------------------  ---------------  ----------
Angus McGee           London           500
Brad Guzan            London           100
Jozy Altidore         Paris            300
Fabian Johns          Paris            300
Julian Green          London           300
*/
