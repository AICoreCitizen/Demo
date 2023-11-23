-- The WHERE Clause
-- The WHERE statement allows you to specify the conditions which records in the database must meet, to be included in resultant set of data. The common conditionals are:

-- >, >=: greater than and greater than equal to
-- <, <=: less than less than or equal to
-- =: equal to
-- !=: not equal to

----------------------------------------------------------------

-- LIKE
-- The LIKE operator allows you to match patterns of data which can be useful when you don't know the exact value you're looking for. It does this with the use of two wildcards:

-- % this represents zero or more of any character
-- _ represents exactly one character

----------------------------------------------------------------

-- Pattern matching
-- Let's take a look at other common ways of matching patterns using % and _:

-- %er%: Will match any value that has er at any position in the word
-- %r: Checks the last letter of a word is r
-- %r_: Checks the second last letter of a word is r. Here _ represents exactly one character and since it is placed directly after r then it would represent the last character of the word.
-- ___: Finds words containing exactly three characters, using three underscores
-- We can also use the keyword NOT to find the inverse of these matches:

-- NOT LIKE '%er%' finds all words that don't contain er at any position etc.
-- AND, OR, BETWEEN and IN
-- AND, OR, BETWEEN and IN keywords allow you to add additional complexity when filtering with the WHERE statement.

-- AND
-- The AND keyword will only return rows where both conditions specified by the AND clause are True:

---------------------------------------------------------------

-- The above query filters the address table with three separate conditions that all must be True for the record to be returned:

-- '%Cal%': Looks for any district which has Cal at any place in the word
-- '%49': Checks for phone_number's ending in the number 49
-- '1%': Looks for addresses which start with the number 1


/*
Using the Pagila database:

Return 10 films who's lengths are under 120 mins
Return the 10 longest films who's rating are G (Hint: to search by string we need to wrap our query in SINGLE quotes (e.g. 'G'))
Return all transactions where payment has been above $10
Return the (replacement) cost per minute of every movie
Return the top 10 most expensive films to rent, based on the rental rate per hour of the movie

*/
-- Return 10 films who's lengths are under 120 mins
SELECT film_id, title, release_year, length, rating FROM film
WHERE length < 120
LIMIT 10;

--Return the 10 longest films who's rating are G (Hint: to search by string we need to wrap our query in SINGLE quotes (e.g. 'G'))
SELECT film_id, title, release_year, length, rating FROM film
WHERE
    rating = 'G'
ORDER BY length DESC
LIMIT 10;

-- Return all transactions where payment has been above $10
--SELECT film.*, payment.amount FROM film
SELECT film_id, title, release_year, length, rating, payment.amount FROM film
JOIN payment ON film.film_id = payment.rental_id
WHERE payment.amount > 10.00;


-- Return the (replacement) cost per minute of every movie
SELECT  film_id, 
        title, 
        release_year,  
        length, 
        rating,
        replacement_cost /(rental_duration*24*60) AS  replacement_cost_per_minute
FROM film

-- Return the top 10 most expensive films to rent, based on the rental rate per hour of the movie
SELECT  film_id, 
        title, 
        release_year,  
        length, 
        rating,
        (rental_rate/rental_duration*24) AS  rental_rate_per_day
FROM film
ORDER BY rental_rate_per_day DESC
LIMIT 10;


