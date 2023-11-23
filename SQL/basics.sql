-- Select Top 10 rows from table
SELECT * FROM actor LIMIT 10;
-- Consider this also as valid
-- SELECT * FROM actor FETCH FIRST 10 ROWS ONLY;
-- SELECT * FROM actor ORDER BY first_name DESC LIMIT 10;
-- SELECT * FROM actor ORDER BY first_name LIMIT 10; -- ascending order by default

-- Using wild card
SELECT * FROM film 
WHERE title LIKE '%AGENT%'
LIMIT 10;