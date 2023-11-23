/*
 Example: Find all addresses for Argentina in the address table using values for Argentina in the country table

 */

-- **************** The naive method ****************************

SELECT country_id,
       country
FROM 
    country
WHERE 
    country = 'Argentina';

-- One now knows that the country_id for Argentina is 6. Using City table we get:

SELECT country_id,
       city,
       city_id
FROM 
    city
WHERE 
    country_id = 6;

-- Great this gives us all the cities and their id's so we can now search all those codes in the address table.

SELECT address_id,
       address,
       address2,
       district,
       city_id,
       postal_code
FROM 
    address
WHERE city_id IN (20, 43, 45, 128, 161, 165, 289, 334, 424, 454, 457, 524, 567);


-- **************** The effective method ****************************

-- To create a JOIN in SQL using the following syntax:

-- {[INNER] | {LEFT | RIGHT | FULL} [OUTER]} JOIN {table2} ON {boolean condition};

-- JOIN the city and county tables together:

SELECT country.country_id ,
       country,
       city_id
FROM 
    country
INNER JOIN 
    city ON country.country_id = city.country_id
WHERE 
    country = 'Argentina';

-- complete solution

SELECT address.city_id,
       country,
       city.country_id,
       address,
       address2,
       postal_code,
       district
FROM 
    country
INNER JOIN 
    city ON country.country_id = city.country_id
INNER JOIN
    address ON address.city_id = city.city_id   
WHERE 
    country = 'Argentina';

-- A tip for resolving this is to build your JOINs up in stages first.

/* 

PRACTICALS

*/

-- Find the addresses of all the stores in the Pagila database

SELECT * FROM address

-- Return the first names, last names, addresses, districts and postal code for all the staff in the database

SELECT 	first_name,
		last_name,
		address,
		address.district,
		address.postal_code
FROM 
	staff
INNER JOIN
	address ON staff.address_id = address.address_id

-- Return the first names, last names, addresses, districts and cities of customers who have rented a film

SELECT 	first_name,
		last_name,
		address,
		address.district,
		address.postal_code,
        city,
        rental_date,
        return_date
FROM 
	customer
INNER JOIN
	address ON customer.address_id = address.address_id
INNER JOIN
    city ON city.city_id = address.city_id
INNER JOIN
    rental ON customer.customer_id = rental.customer_id


-- Return the first names, last names, addresses, districts and cities of customers who have rented a film between 26/05/2005 and 29/05/2005. 
-- Limit the results to 25 customers and sort the results by the last names in ascending order

SELECT  first_name,
		last_name,
		address,
		district,
		postal_code,
        city,
        rental_date,
        return_date
FROM 
	customer
INNER JOIN
	address ON customer.address_id = address.address_id
INNER JOIN
    city ON city.city_id = address.city_id
INNER JOIN
    rental ON customer.customer_id = rental.customer_id
WHERE
    rental_date BETWEEN '2005-05-26 00:00:00' AND '2005-05-29 23:59:59'-- 26/05/2005 and 29/05/2005. 
ORDER BY
    last_name ASC
LIMIT 25;


/*

A SELF JOIN is joining a table to itself. 
This can be a useful JOIN if the table references itself in some way.

**************************USE staff-db DATABASE/ CONNECTION*************************
*/

SELECT employees.employee_id,
       employees.name,
       employees.manager_id,
       managers.name AS manager_name
FROM
    current_employees employees
INNER JOIN 
    current_employees managers ON employees.manager_id = managers.employee_id;

/*

The INNER JOIN checks two or more tables and if the condition matches in the join predicate then the rows are returned in the resultant dataset.

**************************USE staff-db DATABASE/ CONNECTION*************************
*/
--  This will find all rows in Table A which matches rows in Table B based on a condition

SELECT managers.employee_id,
       managers.name,
       managers.salary
FROM
    current_employees
INNER JOIN 
    managers ON managers.employee_id = current_employees.employee_id;

/*

The LEFT JOIN or LEFT OUTER JOIN (aka left outer inclusive join) joins all rows from the left table and matchings rows from the right table based on the join predicate. 
When joined, all data from the left table and only data which intersects (exists in) the right table is returned.
**************************USE staff-db DATABASE/ CONNECTION*************************
*/
--  look at the current_employees table and check which rows contain data for managers.
-- The left table will always be the table the data is being joined onto, the table specified in the FROM statement. 

SELECT current_employees.employee_id,
       current_employees.name,
       managers.salary,
       current_employees.manager_id
FROM
    current_employees
LEFT OUTER JOIN 
    managers ON current_employees.employee_id = managers.employee_id;


/*
Exclusive LEFT JOIN
LEFT JOINS and OUTER joins are used when you know you want to keep the majority of the data in one table. Why the majority of the data?
we are getting all the records in the left table minus the records in the right table i.e removing the intersection of the two tables. 
The intersection of the two tables will be the managers from the managers table since this is the table on the right. 
Following on from our previous query we just need to add a WHERE clause to the statement for SQL to perform the exclusive JOIN:

**************************USE staff-db DATABASE/ CONNECTION*************************
*/

SELECT current_employees.employee_id,
       current_employees.name,
       managers.salary,
       current_employees.manager_id
FROM
    current_employees
LEFT OUTER JOIN 
    managers ON current_employees.employee_id = managers.employee_id
WHERE
    managers.employee_id is NULL;

-- The intersection was removed with the WHERE managers.employee_id is NULL statement. 
-- Remember the managers.employee_id column is still is available to be filtered with the WHERE statement. 
-- Though not viewable in the final data since it is not selected in the SELECT statement, as SELECT comes after WHERE in the order of execution. 
-- WHERE managers.employee_id is NULL can only be the case when the current employee isn't a manager. 


/*
The RIGHT JOIN or RIGHT OUTER JOIN 
joins all rows from the right table and matchings rows from the left table based on the join condition. 
When joined, all data from the right table and only the data in the left table which exists in the right table is returned.
**************************USE staff-db DATABASE/ CONNECTION*************************
*/
SELECT current_employees.employee_id,
       current_employees.name,
       managers.salary,
       current_employees.manager_id
FROM
    managers
RIGHT OUTER JOIN 
    current_employees ON current_employees.employee_id = managers.employee_id;

-- Returns the same data as:

SELECT current_employees.employee_id,
       current_employees.name,
       managers.salary,
       current_employees.manager_id
FROM
    current_employees
LEFT OUTER JOIN 
    managers ON current_employees.employee_id = managers.employee_id;

-- most people will prefer using LEFT JOIN's over RIGHT JOINS's. There's the theory this is due to most languages being read from left-to-right so it's more natural for most people to think this way. 



/*
Exclusive RIGHT JOIN
jThe exclusive RIGHT JOIN can be written similarly to the exclusive LEFT JOIN:
**************************USE staff-db DATABASE/ CONNECTION*************************
*/

SELECT current_employees.employee_id,
       current_employees.name,
       managers.salary,
       current_employees.manager_id
FROM
    managers
RIGHT OUTER JOIN 
    current_employees ON current_employees.employee_id =  managers.employee_id
WHERE
    managers.employee_id is NULL;




/*
A FULL OUTER JOIN, also sometimes know as a FULL JOIN, 
returns all the rows from both the right and the left tables along with any matching rows in both tables. 
If the two tables have no rows in common, the JOIN will still return all rows from both tables, but with NULL values that correspond to missing data.
**************************USE staff-db DATABASE/ CONNECTION*************************
*/

SELECT non_managers.employee_id AS non_manager_employee_id,
       non_managers.name AS name_of_non_manager,
       managers.salary,
       managers.name AS name_of_manager,
       managers.employee_id AS manager_employee_id     
FROM
    non_managers
FULL OUTER JOIN
    managers ON managers.employee_id = non_managers.employee_id;


/*
CROSS JOIN
For every record in table A the CROSS JOIN will match every record in table B. 
This returns the Cartesian product of the rows from the tables. 
In Mathematics the Cartesian product(denoted A x B), is the set of all ordered pairs(a,b), 
where a exists in the set A and b exists in the set B. 
**************************USE staff-db DATABASE/ CONNECTION*************************
*/

-- Just be careful with CROSS JOINS, they will generated a large amount of data.

SELECT managers.name AS managers_name,
       non_managers.name AS staff_name
FROM
    managers
CROSS JOIN
    non_managers;




