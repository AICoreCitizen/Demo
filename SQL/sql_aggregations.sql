/*
Here are the most commonly used aggregation functions:

COUNT : To count how many rows are in a particular column
SUM : To SUM all rows in a particular column
MIN/MAX : To get the maximum or minimum values in a column
AVG : To return the average value in a column#


*/

-- COUNT
-- COUNT allows you to count the number of non-NULL values in a column, the syntax is:

-- COUNT({column name});
-- We can apply the COUNT to any column in our SELECT statement:


SELECT COUNT(address)
FROM address;

-- Which returns a value of 603. Remember that COUNT doesn't count NULL values so applying it to the address2 column we get a different answer:


SELECT COUNT(address2)
FROM address;

-- Which returns a value of 599. There are 603 records in the address table so we know that the address2 column has four NULL values in it.

-- total rows - COUNT(address2) = 4



-- SUM
-- SUM, sums all the values in a column, it only works on numerical data (we can't sum the address column for example). If there is a NULL value in the column it is ignored. The syntax is:

-- SUM({column name})

SELECT SUM(replacement_cost) 
FROM film;

-- Looks like the replacement value of all stock is 20k interesting to know for a business.

-- MIN/MAX
-- MIN returns the minimum value in a column and MAX returns the maximum value. 
-- They can be applied to numerical data, array or character columns. Both functions have the syntax:


-- MIN({column name})
-- MAX({column name})
-- Let's get the minimum replacement_cost and maximum replacement_cost of a film in the film table:


SELECT MIN(replacement_cost) AS minimum_replacement_cost,
       MAX(replacement_cost) AS maximum_replacement_cost
FROM
    film;

-- You'll often want to alias your aggregation columns, since by default, 
-- the aggregated column will be named by the name of the aggregation. 
-- So the intended result of the aggregation won't be clear. 
-- For example SUM(replacement_cost) creates a column called sum .

-- AVG
-- AVG returns the average value in a column. It ignores NULL's in both the numerator and denominator and only works on numerical values:


-- AVG({column name})
-- Getting the average_replacement cost of a film:

SELECT AVG(replacement_cost) AS average_replacement_cost
FROM film;

-- Calculations with aggregations
-- You can also perform arithmetic operations with the results of an aggregation to achieve complex analysis of data. This can be done with the standard operators + - / * %.

-- Calculating the range of cost between the maximum and minimum replacement_cost:


SELECT (MAX(replacement_cost) - MIN(replacement_cost)) AS replacement_cost_range
FROM film;

-- MAX and MIN can be performed on dates so we could calculate how long the business has been renting out movies for:


SELECT MAX(payment_date)- MIN(payment_date) AS payment_span
FROM payment;

-- Notice this returns an interval since we're getting the time span between two dates.
-- Let's calculate the average replacement_cost as a percentage of total stock replacement_cost:


SELECT ( AVG(replacement_cost) / SUM(replacement_cost) ) * 100 AS "average_replacement_cost(%)"
FROM film;

/*

-- DISTINCT
-- By default SQL will return all rows even duplicate rows. Sometimes you may want to return only the rows where column values are unique. This can be done by applying the keyword DISTINCT to a column. The syntax of DISTINCT is:


-- DISTINCT {column1, column2, column3 ....} 
-- Any column specified after the DISTINCT keyword will return only unique values from that column. This can be a great way to check a column to understand all the values the column contains. Imagine we want to check what the different types of ratings a movie could have, we could run the query:
*/

SELECT DISTINCT rating
FROM film;

-- Returning all the possible ratings a film could have. If we wanted to check for each of those ratings what are all the possible rental_rate's, we could add the rental_rate column to your distinct query. Returning distinct values which are a combination of rating and rental_rate:

SELECT 
    DISTINCT rating,
    rental_rate
FROM 
    film
ORDER BY
    rating;

-- This can be a great way to quickly summarise the data in columns when performing initial data analysis. 
-- DISTINCT can also be used in conjugation with aggregations like COUNT. Which would return a count of unique values in a column:

SELECT 
    COUNT(DISTINCT(rating)) AS Rating_Count,
    COUNT(DISTINCT(rental_rate)) AS Rental_Rate_Count
FROM 
    film;

-- Notice here, we apply COUNT individually to each column so we need to apply DISTINCT separately to each column.


/*
DATE TRUNC
DATE TRUNC stands for date truncate and can be a very useful function if you want to strip away values in a timestamp. This can help when you want to aggregate times together. The syntax is:


DATE_TRUNC({field}, {column})
With DATE_TRUNC you can remove values from the timestamp up to the specified field value. The options for the field value are:

microseconds
milliseconds
second
minute
hour
day
week
month
quarter
year
decade
century
millennium
If we specified DATE_TRUNC('day', {column}) the function would truncate(remove) all values up to the date value in a timestamp.

Imagine you want to group together all the days a rental was made by rental_date. In the rental table the rental_date has values such as, 2005-05-24 23:03:39 and 2005-05-24 22:54:33. Though rentals occurred on the same day, if we try to group the data by these values they won't belong to the same group since the times are different.

We can instead truncate the date up to the day value so that the value of these dates will be the same:

*/ 

SELECT DATE_TRUNC('day', rental_date)
FROM rental;

-- After running this query you can see the values 2005-05-24 23:03:39 and 2005-05-24 22:54:33 have both been stripped of their time values, so both have the value 2005-05-24 00:00:00. This could be useful when you want to group the entries together by day of the month. You will learn how to then group the data using a GROUP BY in the next lesson.


SELECT DATE_TRUNC('day', rental_date) AS rental_day,
       COUNT(rental_date) AS total_daily_rentals
FROM 
    rental
GROUP BY 
    rental_date
ORDER BY
    total_daily_rentals DESC;

/*
DATE PART/EXTRACT
The DATE_PART or EXTRACT allows us to extract a specific field from a timestamp or interval, with the following syntax:


DATE_PART({field}, {timestamp/interval})
EXTRACT({field from timestamp/interval})
There is a slight difference between EXTRACT and DATE_PART though in most cases they can be used interchangeably. Since PostgreSQL 14 EXTRACT returns a numeric type and DATE_PART returns a double precision type. Double precision has precision up to 15 digits after the decimal point and numeric is up to 16383 so they can round slightly differently in rare cases.

The field value allows you to specify which part of the interval or timestamp you would like to extract and has the same options as DATE_TRUNC plus additionally:

timezone: extract the timezone
timezone_hour: hour component of the time zone
timezone_minute: minute component of the time zone
dow: numerical value for the day of the week
doy: numerical value for the day of the year
epoch: number of seconds past since 1970-01-01 00:00:00

*/


-- An example of extracting the year from the payment_date in the payment table:

SELECT EXTRACT('year' from payment_date) as day_taken_payment
FROM payment;


/*

CASE

The CASE statement checks multiple conditional statements and returns a value when one is met. 
It evaluates each statement in order, and once one is met it will return the specified value from that statement. 
You will always find the CASE statement as part of the SELECT clause.

The CASE statement is created using the keywords WHEN, THEN, END and optionally ELSE or AS. Let's take a look at the syntax of the statement:

CASE 
    WHEN condition THEN result
    [WHEN ...]
    [ELSE result]
END AS {column alias}

First the CASE statement is created with the CASE keyword and ends when it reaches the END keyword. 
This can be followed by AS, to alias the newly created column from the CASE statement. Each condition in the CASE statement starts with WHEN condition. 
If this condition is met then its associated THEN result updates the new column with result.

You can think of CASE like if else statements in another programming language. The Pythonic way to view this is:

if condition_1:
    return value_1
elif condition_2:
    return value_2
else:
    return value_3 



*/

SELECT title, 
       release_year, 
       rental_rate,
CASE
    WHEN rental_rate > 0 AND rental_rate < 2.99 THEN 'discount'
    WHEN rental_rate >= 2.99 AND rental_rate < 4.99 THEN 'regular'
    ELSE 'premium'
END AS quality
FROM 
    film;


-- Notice we're using the rental_rate column to determine which quality category each film should belong to.

-- We have the ranges:

-- WHEN rental_rate > 0 AND rental_rate < 2.99 THEN 'discount'
-- WHEN rental_rate >= 2.99 AND rental_rate < 4.99 THEN 'regular'
-- ELSE premium
-- After the CASE statement is completed with END, we've aliased the column to create AS quality. 
-- So the first statement is saying if the rental_rate is between 0 and less than 2.99 then the value discount will be inserted into the new column quality. 
-- If it's between 2.99 and 4.99 then the value regular will be inserted. In all other cases the value premium will inserted into the column.

/*

PRACTICALS

*/

-- Using the Pagila database, answer the following questions:

-- How many rented films do not have a return date?
SELECT  COUNT(return_date) AS Count_return_date,
        COUNT(rental_id) AS Count_rental_id,
        ( COUNT(rental_id) - COUNT(return_date)) AS Count_film_no_return_date

FROM 
    rental

-- What is the total amount of payments that the business has received?

SELECT SUM(amount)
FROM payment

-- What is the total amount of payments that the business has received between the dates 25/01/2007 and 29/01/2007

SELECT SUM(amount)
FROM payment
WHERE payment_date BETWEEN '2007-01-25 00:00:00' AND '2007-01-29 23:59:59'

-- When was the earliest transaction made?

SELECT MIN(payment_date) AS Earliest_Transaction,
MAX(payment_date) AS Latest_Transaction
FROM payment

-- When was the last transaction over $10 made?

SELECT MAX(payment_date) AS Latest_Transaction
FROM payment
WHERE amount > 10.00


-- What is the price of the highest value film the business has?

SELECT MAX(amount) AS Highest_value
FROM payment

-- What is the average length of films?

SELECT AVG(length)
FROM film

-- What is the average length of films who's rental cost is under $2.99

SELECT AVG(length)
FROM film
WHERE rental_rate < 2.99























