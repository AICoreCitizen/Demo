--********************************** Single row and scalar subqueries****************************


-- Example: get all films from the film table which have a greater than average runtime.

SELECT title,
       length
FROM
    film
WHERE
    length > 
    (
        SELECT AVG(length)
        FROM film
    )
ORDER BY 
    length DESC;

-- returns all movies with a length greater than the average runtime, note here the subquery:

(
    SELECT AVG(length)
    FROM film
);

-- Returns a scalar value 115.272

-- WHERE length > 115.272

-- what if we wanted to display the average length alongside the length column to visually validate our data?

SELECT title,
       length,
       (
            SELECT ROUND(AVG(length)) AS average_film_length
            FROM film
       )
FROM
    film
WHERE

    length > 
    (
        SELECT AVG(length)
        FROM film
    )
ORDER BY 
    length;

-- So we can actually use subqueries in SELECT statements to generate new columns if they return a scalar value.

-- use a subquery in the HAVING statement to filter the data:

SELECT AVG(length) AS film_rating_average_length,
       rating
FROM
    film
GROUP BY
    rating
HAVING
    AVG(length) > 
    (
        SELECT AVG(length)
        FROM film
    );


-- filtered the results after the GROUP BY statement using the HAVING statement. 
-- Let's group the films by rating and then determine which ratings have a higher than average replacement_cost.

SELECT rating,
       ROUND(AVG(replacement_cost), 2) AS avg_rating_replacement_cost,
       (
            SELECT ROUND(AVG(replacement_cost),2) AS avg_film_replacement_cost
            FROM film
       )
FROM
    film
GROUP BY
    rating
HAVING
    AVG(replacement_cost) > 
    (
        SELECT AVG(replacement_cost)
        FROM film
    );


-- This SQL query is doing a few things:

-- It's selecting the rating column and calculating the average replacement_cost for each rating by using the AVG() aggregate function and rounding it to 2 decimal places. This is being aliased as avg_rating_replacement_cost.
-- It's also selecting the overall average replacement cost for all films, calculated in the subquery by taking the AVG() of replacement_cost and rounding to 2 decimals. This is being aliased as avg_film_replacement_cost.
-- It's grouping the results by rating so that we get a separate average per rating.
-- It's using a HAVING clause to only include groups where the average replacement cost is greater than the overall average replacement cost. This filters to only ratings that have an above average replacement cost.

--********************************** Multiple row subquery****************************

-- Subqueries that return multiple rows of data to an outside query are called multiple-row subqueries. 
-- These are great for targeting a subsets of the data. 
-- They can be used in the SELECT, FROM, WHERE and HAVING just like single row subqueries. 
-- They can't be used with comparison operators, unless preceded with one of the keywords ANY, ALL, IN or NOT IN.


-- check which actors appeared in the film ACE GOLDFINGER in the film table, which has film_id = 2

-- We could do this by joining the two tables and then filtering the data in the WHERE statement. 
-- Or we could use a subquery to get the data:

SELECT actor_id,
       first_name,
       last_name
FROM 
    actor
WHERE 
    actor_id IN 
    (
        SELECT actor_id
        FROM film_actor
        WHERE film_id = 2
    );

-- First we evaluate the inner query which selects all rows from the film_actor table where the film_id = 2. 
-- This should give us a subset of the film_actor table since there are multiple rows meeting the condition. 

        SELECT actor_id
        FROM film_actor
        WHERE film_id = 2;

-- So after the subquery is evaluated, the WHERE statement would then become 
-- WHERE actor_id IN (19, 85, 90, 160) which allows us to produce the final result.

-- Ideally, we would like to SELECT the film_id column to be part of the final result, 
-- so we can verify the accuracy of the results. 
-- Unfortunately, the film_id column exists in the film_actor table, 
-- which the subquery selects from and does not exist in actor table used by the outer query.



--********************************** ANY, ALL, IN, NOT IN****************************

/*

ANY, ALL, IN, NOT IN can be used in conjunction with a comparison operator. In all cases the subquery must return at least one column to be used with these subquery expressions. They have the following use cases:

ANY/SOME: ANY or SOME can be used interchangeably. If the evaluated is True for any row returned by the subquery, then the statement will ultimately evaluate to True.
IN: Evaluates to True if the expression matches any rows in the subquery
NOT IN: Evaluates to True if the expression does not match any rows in the subquery
ALL: The statement will evaluate to True if the expression matches all rows in the subquery

{expression} {operator} [ ALL | ANY | IN | NOT IN] (subquery)

*/

SELECT title,
       release_year,
       replacement_cost
FROM 
    film
WHERE 
    replacement_cost IN 
    (
        SELECT DISTINCT(replacement_cost)
        FROM film
        WHERE replacement_cost < 12.99
        AND replacement_cost > 9.99
    );

-- In the query we're using the IN keyword to return all movies which have one of these rental ratings.

replacement_cost > ANY 
(
    SELECT DISTINCT(replacement_cost)
    FROM film
    WHERE replacement_cost < 12.99 
    AND replacement_cost > 9.99
);

-- This query is saying, if the film replacement_cost is greater than ANY of the results of the subquery, 
-- then return the movie. So that's all movies with replacement_cost > 10.99 or 11.99 which equates to replacement_cost >= 11.99

--NOTE: Just a small note about IN and ANY, if we had stated replacement_cost = ANY then this would be logically equivalent to replacement_cost IN and can be used interchangeably. 

replacement_cost NOT IN 
(
    SELECT DISTINCT(replacement_cost)
    FROM film
    WHERE replacement_cost < 12.99
    AND replacement_cost > 9.99
);

-- This returns all movies where their replacement_cost is not one of 10.99, 11.99. So would return all rows where replacement_cost < 10.99 and replacement_cost > 11.99.

replacement_cost <= ALL
(
    SELECT DISTINCT(replacement_cost)
    FROM film
    WHERE replacement_cost < 12.99
    AND replacement_cost > 9.99
);

-- The ALL keyword is checking that the current row is less or equal to all of 10.99 and 11.99. The query would then return all movies with replacement_cost <= 10.99


--********************************** Multiple Column subquery****************************

SELECT title,
       rental_duration,
       rental_rate
FROM 
    film
WHERE
    (rental_duration, rental_rate) IN
    (
        SELECT MAX(rental_duration),
               MAX(rental_rate)
        FROM
            film
    );

-- Since our outer query is checking that the rental_rate and rental_duration 
-- exist within the subquery results, it will return all films which match those values. 
-- Which is to say the outer query is returning all results where the rental_duration and rental_rate are both at their maximum.


--********************************** Correlated subqueries****************************


-- Correlated subqueries are named as such, since the output of the subquery depends on the results form the 
-- boutside query, hence the two queries are correlated. 
-- A correlated subquery refers to a column which is not in the table of its FROM clause. 
-- These subqueries are used within the SELECT, WHERE, HAVING and FROM clauses.

--using a JOIN:

SELECT customer.customer_id,
       first_name,
       last_name,
       ROUND(AVG(payment.amount), 2) AS average_customer_payment
FROM
    customer
INNER JOIN
    payment ON payment.customer_id = customer.customer_id
GROUP BY
    customer.customer_id, first_name, last_name
ORDER BY
    customer_id;


-- Let's take a look at an example of using a correlated query in the SELECT statement:

SELECT customer_id,
       first_name,
       last_name,
       (
            SELECT ROUND(AVG(amount), 2) AS average_customer_payment
            FROM payment 
            WHERE customer.customer_id = payment.customer_id
        )
FROM
    customer; 

-- In the SELECT statement we've used the subquery to return the average payment made by each customer and included this as a column in our results. We've used the subquery to get the average amount paid by each customer. Notice that in the WHERE statement of the subquery we've matched the columns on the customer_id from payment and customer columns.
-- So, the inner query is referencing the outer query, this creates the correlation between the two tables.

-- NOTE: With correlated queries you can often get the same information using a JOIN. In most cases a JOIN is more efficient, as subqueries are executed on every row of the table whereas a JOIN is performed once. It is rare a subquery outperforms a JOIN so when given the choice, try and write the statement with a JOIN


--********************************** Nested subqueries subquery****************************

SELECT title,
       description
FROM
    film
WHERE 
	film_id IN 
	(
		SELECT film_id
		FROM film_actor
		WHERE actor_id IN 
		(
			SELECT actor_id
			FROM actor
			WHERE first_name = 'CHRISTIAN'
		)
	);


-- Let's take a look at what this nested query is performing, the innermost query is executed first:

SELECT actor_id
FROM actor
WHERE first_name = 'CHRISTIAN'

-- The outside query then becomes:

SELECT film_id
FROM film_actor
WHERE actor_id IN (10, 58, 61)

-- Then finally the outer most query results in:

SELECT title,
       description
FROM
    film
WHERE 
	film_id IN (1, 9, 191, 236, ....)

-- This returns all movies where the actors first_name is CHRISTIAN


--********************************** Derived tables****************************


-- A derived table is a table which is derived from an expression in the FROM clause of a SQL query. 
-- Derived tables can be useful for applying SQL logic to a subset or aggregations of a table. 
-- One important thing to remember when creating derived tables is, they need to have an aliases, such that they can be referenced in the outside query. 
-- An example of a query using a derived table:

SELECT ROUND(AVG(payment_sums.sum_of_payments), 2) AS average_sum_of_payments
FROM
    (
        SELECT SUM(amount) AS sum_of_payments
        FROM 
            payment
        GROUP BY
            customer_id       
    ) AS payment_sums

-- Here the subquery derives a table from the payments table, grouping all the customer_id's and summing all their payments. Notice the subquery table is also aliased as payment_sums, which the outside query can then reference to get the average of all customer payments.

-- If we evaluate the inside query and add the customer_id column to it, it's clear it's summing up the total payments for all customers:

SELECT SUM(amount) AS sum_of_payments,
       customer_id
FROM 
    payment
GROUP BY
    customer_id;

-- We then get the average and ROUND the results by referencing the table in the SELECT statement, ROUND(AVG(payment_sums.sum_of_payments),




/*


PRACTICALS


*/


-- Using the Pagila database:

-- Return the ids, title and release year of all films which have the category 'Animation'

SELECT 	film_id,
		language_id,
		original_language_id,
		title,
		release_year
FROM film
WHERE film_id IN
	(
		SELECT film_id
		FROM film_category
		WHERE category_id IN
			(
				SELECT category_id
				FROM category
				WHERE name ='Animation'
			)
	)
ORDER BY title


-- Return the first name, last name, and email of all customers in Canada


-- Return the titles of films with movies starting with A or I and are not in the Italian, French or Spanish Language (all films are in English, but write the query as the practical requests)



-- Return the average film length per rating


-- Find the average number of sales per day for each staff