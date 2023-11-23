/*


SQL GROUP BY

Sometimes instead of aggregating a whole data column, it can be useful to aggregate a subset of that data
The syntax for GROUP BY is:

[ ]
SELECT {column}, {aggregation1, aggregation2 ...}
FROM {table}
GROUP BY {column}


*/

-- Example of grouping customers together in the rental table and counting the amount of movies they have rented. 
-- We could do this with the following query, returning the top five customers in descending order:


SELECT customer_id, 
       COUNT(rental_date) AS total_number_of_rentals
FROM 
    rental
GROUP BY 
    customer_id
ORDER BY
    total_number_of_rentals DESC
LIMIT 
    5;

-- We are using the GROUP BY to group the records by customer_id so wherever the customer_id's are the same, they will be grouped together in the same row. We've also selected another column as an aggregation COUNT(rental_date) AS total_number_of_rentals so that within each group the number of rentals are counted for each customer.
-- The results are then ordered by total_number_of_rentals in descending order, such that users with the highest amount of rentals are shown first. Finally the records are then limited to the top five users with the LIMIT 5 statement.

-- Multiple columns can also be added to the GROUP BY column to further group the data if required. 
-- Let's imagine we want to check, how many movies each staff member sold to a customer. 
-- We could first use a GROUP BY to group the data by the customer_id 
-- and then group by a secondary column staff_id to further group the data. 
-- The query is:

SELECT customer_id, 
       COUNT(rental_date) AS total_number_of_rentals,
       staff_id
FROM 
    rental
GROUP BY 
    customer_id, staff_id
ORDER BY
    customer_id DESC, staff_id DESC;

-- A common error you might run into when trying to perform GROUP BY statements is:

-- column x must appear in the GROUP BY clause or be used in an aggregate function

-- Where x is one of the columns in your SELECT statement, why does this happen? 
-- Let's try and use SELECT to also select the inventory_id column in our statement and investigate what SQL is trying to do:
-- This will generate an error ---

SELECT customer_id, 
       COUNT(rental_date) AS total_number_of_rentals,
       staff_id, 
       inventory_id
FROM 
    rental
GROUP BY 
    customer_id, staff_id
ORDER BY
    customer_id DESC, staff_id DESC;

-- column "rental.inventory_id" must appear in the GROUP BY clause or be used in an aggregate function
-- So we either need to aggregate that column or add the column to our GROUP BY clause. Let's add the COUNT of the inventory_id for each of our groups:


SELECT customer_id, 
       COUNT(rental_date) AS total_number_of_rentals,
       staff_id, 
       COUNT(inventory_id) AS number_of_unique_rentals
FROM 
    rental
GROUP BY 
    customer_id, staff_id
ORDER BY
    customer_id DESC, staff_id DESC;

-- Great, that solves our problem but might not be particularly useful since it should just return the same COUNT as the rental_date. What about if we add it to the GROUP BY:


SELECT customer_id, 
       COUNT(rental_date) AS total_number_of_rentals,
       staff_id, 
       COUNT(inventory_id) AS number_of_unique_rentals
FROM 
    rental
GROUP BY 
    customer_id, staff_id, inventory_id
ORDER BY
    customer_id DESC, staff_id DESC;


-- This give us something a little more useable, it returns the amount of times an item was rented by a particular customer from a particular staff member.


/*

HAVING
In the SQL order of execution the WHERE statement is performed filtering the data before the GROUP BY is applied. 
What if we want to filter the data after the GROUP BY?. We can apply a HAVING clause after the GROUP BY. 
HAVING comes after GROUP BY in the order of execution. 
This allows us to filter the data so that we only get results we are interested in.

The syntax for the HAVING statement is as follows:

HAVING {conditional}

The HAVING statement takes a conditional and if the result of the conditional evaluates to True, 
then the rows will become part of the returned query set. 

*/

SELECT customer_id, 
       COUNT(rental_date) AS total_number_of_rentals
FROM 
    rental
GROUP BY 
    customer_id
HAVING
    COUNT(rental_date) > 37
ORDER BY
    total_number_of_rentals DESC;


--  You can apply the same conditions you would apply in a WHERE statement. 
-- The important distinction is that WHERE is applied before the GROUP BY and HAVING is applied after the GROUP BY. 

SELECT SUM(rental_rate * rental_duration) AS total_rating_rental_rate,
       rating
FROM 
    film
WHERE 
    rental_rate > 0.99
GROUP BY 
    rating
HAVING
    (SUM(rental_rate * rental_duration)) > 2500;

--- Better way ---

SELECT  SUM(rental_rate * rental_duration) AS total_rating_rental_rate, 
        rating 
FROM film 
WHERE rental_rate > 0.99 
GROUP BY rating 
HAVING 
    SUM(rental_rate * rental_duration) IN 
    (SELECT DISTINCT SUM(rental_rate * rental_duration) 
    FROM film 
    WHERE rental_rate > 0.99 
    GROUP BY rating ) AND SUM(rental_rate * rental_duration) > 2500;




/*

PRACTICALS

*/



-- Using the Pagila database:

-- Find the unique special features of films

SELECT DISTINCT special_features 
FROM film;

-- TO isolate each distinct value we need to unnest

SELECT DISTINCT special_feature 
FROM 
    ( SELECT film_id, unnest(special_features) AS special_feature 
    FROM film ) AS features 
ORDER BY special_feature;

-- Which 3 days of the week are most profitable for the business?

SELECT
  TO_CHAR(payment_date, 'Day') AS week_day,
  SUM(amount) AS total_amount
FROM payment
GROUP BY week_day
ORDER BY total_amount DESC
LIMIT 3;

-- Return the total sales per day, along with the number of movies rented for that day

SELECT
  DATE_TRUNC('week', payment_date) AS week_start,
  TO_CHAR(payment_date, 'Day') AS week_day,
  SUM(amount) AS total_amount,
  COUNT(rental_id) AS total_daily_film_sales
FROM payment
GROUP BY week_start, week_day
ORDER BY week_start DESC

-- Find the id's of all customers who have spent over $100 over the course of their membership

SELECT
    customer.customer_id,
    first_name,
    last_name,
    SUM(amount) AS TOTAL_AMOUNT
FROM
    payment
INNER JOIN
    customer ON payment.customer_id = customer.customer_id

GROUP BY
    customer.customer_id, first_name, last_name
HAVING
    SUM(amount) > 100.00;




/*

PRACTICALS

*/


-- Using the Pagila database:

-- List the last names of actors, as well as how many actors have that last name.

SELECT
    last_name,
    COUNT(last_name) AS total_same_last_name
FROM
    actor

GROUP BY
		last_name

-- How many customers are there per store? Return the number of customers and the store id.

SELECT
    customer.store_id,
    COUNT(customer_id) As NUMBER_OF_CUSTOMERS
FROM
    store
	
INNER JOIN
	customer ON store.store_id = customer.store_id

GROUP BY
		customer.store_id

-- When was the earliest order placed per customer? Return the customer ids, the rental rates, and the names

SELECT
    c.customer_id,
	c.first_name,
	c.last_name,
    f.rental_rate,
	r.rental_date,
    f.title
FROM
    customer c
INNER JOIN (
    SELECT
        customer_id,
        MIN(rental_date) AS earliest_rental_date
    FROM
        rental
    GROUP BY
        customer_id
) AS earliest_rental ON c.customer_id = earliest_rental.customer_id
INNER JOIN rental r ON earliest_rental.earliest_rental_date = r.rental_date AND earliest_rental.customer_id = r.customer_id
INNER JOIN inventory i ON r.inventory_id = i.inventory_id
INNER JOIN film f ON i.film_id = f.film_id;

-- What was the largest order placed per customer? Return the customer ids and the amounts

SELECT
    DISTINCT c.customer_id,
    c.first_name,
    c.last_name,
    p.amount
FROM
    customer c
INNER JOIN (
    SELECT
        customer_id,
        MAX(amount) AS largest_order
    FROM
        payment
    GROUP BY
        customer_id
) AS largest_amount ON c.customer_id = largest_amount.customer_id
INNER JOIN payment p ON c.customer_id = p.customer_id AND largest_amount.largest_order = p.amount;

-- NOTE: I noticed duplicate rows aith same maximum payment.
--  Using DISTINCT will give a distinct set of customer details along with their largest payment amount, 
-- removing any duplicate rows that might have been introduced by multiple payments with the same maximum amount.

































