/*
This is a workbook containing select clause and sorting operations. 

*/

-- Select all columns can be shown by specifying each of their names.

SELECT payment_id,
       customer_id,
       staff_id,
       rental_id,
       amount,
       payment_date
FROM payment;

-- Using the following query SELECT the address2 and city_id columns from the address table:

SELECT  customer_id, 
        amount 
FROM payment;

-- Aggregations and arithmetic operations can also be preformed within the SELECT statement. The supported arithmetic operators are:
-- +: Adds values
-- -: Subtracts values
-- *: Multiplies values
-- /: Divides values
-- % (Modulo): Returns an integer remainder of dividing two numbers together. For example 13 % 5 returns 3.

SELECT title, 
       (rental_rate / rental_duration) AS rental_rate_per_day, 
       (rental_rate * rental_duration) AS total_rental_cost, 
       (rental_rate * rental_duration) + replacement_cost AS total_replacement_cost
FROM 
    film;

-- to round the results of your arithmetic operations if there are too many trailing figures
-- ROUND(<source value>, n)

-- The function takes two arguments source value and n, source value represents the value to round 
-- and n(has the default value 0) represents the number of decimal places to round to.

SELECT title, 
       ROUND((rental_rate / rental_duration), 2) AS rental_rate_per_day, 
       (rental_rate * rental_duration) AS total_rental_cost, 
       (rental_rate * rental_duration) + replacement_cost AS total_replacement_cost
FROM 
    film;


-- One can also use the functions:

-- FLOOR(value): Returns smallest nearest integer
-- CEIL(value): Returns largest nearest integer

/* ORDER BY
You might want to order your results to see them in descending or ascending order, to see You may want to view the highest or lowest values after ordering the data. 
Normally after the query is run the results are returned in an unspecified order. This can be impacted by tables JOINs or the way the data is structured on the disk and can't be relied upon. 
To sort them in a more cohesive order you can use the ORDER BY clause which has the following syntax:

ORDER BY {expression1, expression2 ....} [ASC | DESC] [NULL { FIRST | LAST }]

ORDER BY can sort the data based on any column which is used in the SELECT statement. 
You can sort using multiple columns from the SELECT statement if required. 
The default sorting direction is ascending order, so you don't need to specify this, if that is your requirement. 
The last option NULL {FIRST | LAST} allows to control whether NULL's appear first or last after the sorting has taken place. 
Normally NULL's are treated as though they are highest value in the column. 
Thus by default, since the columns are sorted in ascending order NULL's will be placed at the bottom of the results.

Let's sort the rental_date column of the rental table to see which rental was most recent:
*/

SELECT customer_id,
       rental_date
FROM 
    rental
ORDER BY 
    rental_date DESC;

--  Let's instead order the data by two columns: 
--  first order it by the customer_id in ascending order and then by rental_date in descending order.

SELECT customer_id,
       rental_date
FROM 
    rental
ORDER BY 
    customer_id, rental_date DESC;

-- We can see with a customer_id of 19 there are multiple sales for that particular customer. 
-- In our ORDER BY statement since we first sorted the customer_id in ascending order, customer_id's so that will take precedence and be sorted first. 
-- If there is multiple values for the same customer like in this case, 
-- then the second second expression in the ORDER BY will run sorting by rental_date in descending order.

/*
LIMIT

LIMIT allows you to return a specified number of rows from your query. 
This should be used after an ORDER BY, since unsorted data can return rows in a random order. 
LIMIT can be written with the following syntax:

*/

SELECT {list of columns/aggregations ... }
FROM 
    {table_name}
ORDER BY 
    {expressions ...}
LIMIT 
    {number | ALL} [OFFSET number];

/*
By default, LIMIT with ALL is the same as not supplying the LIMIT clause, as it will return all rows from your data. 
You can add it for readability or you can specify an integer value to return a specific number of rows. 
If the number of rows returned by your query is less that the value specified in your LIMIT clause, then SQL will still return all the rows. 
For instance if you set LIMIT 10 and your query returned 5 rows they would still be returned.

OFFSET allows you to skip a number of rows, before returning the amount of rows you've specified in your LIMIT clause. 
If you had LIMIT 5 OFFSET 10 then your SQL query will skip the first 10 rows and return the next 5 rows. 
Let's apply LIMIT to our original query to return only the first 5 rows:
*/

SELECT customer_id,
       rental_date
FROM 
    rental
ORDER BY 
    customer_id, rental_date DESC
LIMIT
    5;

-- This returned the data for customer_id's 1 through 7, which are the first 5 rows expected in the data


SELECT customer_id,
       rental_date
FROM 
    rental
ORDER BY 
    customer_id, rental_date DESC
LIMIT
    5 OFFSET 10;

-- If we apply an OFFSET of 10, then rows then will get rows 11 - 15 returned.


/*
A note about quotes
When aliasing/selecting columns normally you would keep all column names in snake_case. There are times where a column represents an abbreviation or you want to produce a column that has spaces in the name. To do this you need to understand, SQL objects (tables, columns schemas) are referenced with double quotes (" ") and single quotes (' ') represent a string .

Let's look at an example, where you wanted to alias a total_customer_payments column as total customer payments. To do this you need to wrap the alias in double quotes. If you wanted the column to be capitalised or were referencing a column which has capitalisation you would need to do the same.

Total_customer_payments would create a column name of total_customer_payments (it ignores the capitalisation without quotes)
"Total_customer_payments" would create the column Total_customer_payments with capitalisation
total customer payments would result in an error since SQL is seeing total customer and payments as three separate objects
"total customer payments" creates the column total customer payments since the column name is wrapped in double quotes
So when referencing/aliasing a column with spaces always use double quotes and single quotes when referencing a string.
*/









