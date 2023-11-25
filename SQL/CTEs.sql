
-- ***************************** COMMON TABLE EXPRESSIONS (CTEs)*************************

-- Common Table Expressions(CTEs)
-- A Common Table Expression or CTE for short, is a temporary named result set in a SQL statement that can be referenced within the same query. You can have multiple CTEs included in the same query. You can think of CTEs as temporary tables which can help solve your query.

-- The following is an example of syntax you can use to create CTEs:

-- [ ]
-- WITH {cte1_name} AS (
--     SELECT {column1, column2 ...}
--     FROM {table_name}
--     WHERE {VALUE OPERATOR}
-- ), 
-- {cte2} AS (
--     SELECT {column1, column2 ...}
--     FROM {table_name}
--     WHERE {VALUE OPERATOR}
-- )

-- Creating CTEs begins with the WITH keyword followed by an alias AS for the CTE. You then wrap the query which will return your resultant set inside parentheses. In the example syntax, we've created a second CTE, which is separated by , another alias and again parentheses. The query ends with the final statement retrieving the final dataset.

-- There are many benefits to use CTE's:

-- Code reuse and organization: By using a CTE, you can define a complex query once and then reference it multiple times within the same query. This can simplify the code and makes it easier to read and maintain.

-- Improving query performance: In some cases, a CTE can improve query performance by allowing the database engine to optimize the execution plan. This is especially true when the same subquery is repeated multiple times within a larger query.

-- Recursive queries: CTEs can be used to perform recursive queries that are not possible with standard SQL queries. For example, you can use a CTE to traverse a tree structure or hierarchical data.

-- Simplifying complex queries: When a query involves multiple levels of nested subqueries, using CTEs can make the code more readable and easier to understand.

-- ****************************************************************************************

-- Let's look at an example of how to replace a derived table with a CTE:

SELECT ROUND(AVG(payment_sums.sum_of_payments), 2) AS average_sum_of_payments
FROM
    (
        SELECT SUM(amount) AS sum_of_payments
        FROM 
            payment
        GROUP BY
            customer_id       
    ) AS payment_sums

-- This could be represented by CTEs in the following way:


WITH cte AS (
    SELECT SUM(amount) AS sum_of_payments
    FROM 
        payment
    GROUP BY
        customer_id
)
SELECT ROUND(AVG(sum_of_payments), 2) AS average_sum_of_payments
FROM cte

-- Here instead of deriving the table using a subquery we've just created a cte, 
-- which we can then reference in the final statement as though it was its own table.


-- **********************************Multiple CTEs******************************

-- Multiple CTEs can also be used to break down complex queries into stages, making it easier to retrieve the data you want. Let's count the amount of customers that rent movies at a higher than average rental_rate.

-- First create a CTE that returns the average of rental_rate in the film table
-- Create a CTE which contains information about the distinct costs of renting a movie
-- Create a third CTE which finds the average amount customers make to rent a movie
-- Create a the final query that only returns the customers with a higher than average payment amount
-- We could break the first two statements into two separate queries first, before joining them together using CTEs to get the final result.


-- Get the average of all rental_rate's from film:

SELECT AVG(rental_rate)
FROM film;

-- Get all distinct costs of renting a movie:

SELECT DISTINCT(rental_rate)
FROM film 

-- Now we can join them together with CTEs and to create the third CTE. 
-- Which will, get all amounts in the payment table where the amount exists in the distinct_rental_rates CTE.


WITH distinct_rental_rates AS (
    SELECT DISTINCT(rental_rate) AS rental_rates
    FROM film
),average_rental_rate AS (
    SELECT AVG(rental_rate)
    FROM film
),average_customer_rental_payment AS (
    SELECT customer_id,
       AVG(amount) AS average_rental_payment
    FROM 
        payment
    WHERE 
        amount IN 
        (
            SELECT rental_rates 
            FROM distinct_rental_rates
        )
    GROUP BY 
        customer_id
)

-- Notice in the last CTE, we have to use a subquery to check the amount exists in distinct_rental_rates, since we can't use a CTE in the WHERE clause. Now we just have to perform the final query as we have all the required information.

WITH distinct_rental_rates AS (
    SELECT DISTINCT(rental_rate) AS rental_rates
    FROM film
),average_rental_rate AS (
    SELECT AVG(rental_rate)
    FROM film
),average_customer_rental_payment AS (
    SELECT customer_id,
       AVG(amount) AS average_rental_payment
    FROM 
        payment
    WHERE 
        amount IN 
        (
            SELECT rental_rates 
            FROM distinct_rental_rates
        )
    GROUP BY 
        customer_id
)SELECT customer_id,
       ROUND(average_rental_payment, 2) AS average_rental_payment
FROM 
    average_customer_rental_payment
-- WHERE
--     average_rental_payment > 
--     (
--         SELECT average_rental_rate
--         FROM average_rental_rate
--     )
ORDER BY 
    average_rental_payment DESC;

-- This may look like a large and complicated query, but you can imagine how tangled it would be if we used nested subqueries. The logic here is easier to follow since we can break the complex query up into a series of steps using the CTEs, while not losing performance.

-- The third CTE could have even been broken further into two separate CTE's. One to filter all the records for payment amounts which don't exist in the distinct_rental_rates table. Then a further CTE to group all those records by customer_id before returning the final query.

-- You can see that CTEs can be very powerful to breakup the logic of a complex query making it easier to reach the result.


/*

PRACTICALS

*/

-- With the Pagila database:

-- Using JOINs, find the number of times each film was rented. Order by descending.
-- Using CTEs:
-- Define two tables (in the WITH): One which selects all films and film titles, the other which counts the amount of times each film was rented
-- Join these two tables together to return the equivalent result of 1.