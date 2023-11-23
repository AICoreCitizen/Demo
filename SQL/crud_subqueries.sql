-- *******************************CRUD Subquery Operations***********************************

-- Adding and removing records

-- Subqueries can be of great help with inserting and removing data from a table. Instead of manually entering the data into a INSERT, UPDATE or DELETE statement, a subquery can be used to add or remove data.
-- Note that running these queries will either add or remove data from your database. You may need to restore the original if you want it back to its default state.

-- INSERT
-- Data can be inserted into a table from the results of a subquery. 
-- Imagine we want a new table in our database solely to track payments coming from movie replacements not rental of movies

-- Let's created a new table to store the data, tracking the rental_id amount, payment_date and staff_id. 
-- We'll also add a replacement_id column as a PRIMARY KEY to track unique replacements.

CREATE TABLE IF NOT EXISTS rental_replacements (
    replacement_id SERIAL PRIMARY KEY,
    amount NUMERIC(8,2) NOT NULL,
    payment_date TIMESTAMP NOT NULL,
    staff_id INTEGER NOT NULL
)

-- That creates our table, now let's fill it with data using a subquery, the syntax to INSERT data using a subquery is:

-- [ ]
-- INSERT INTO table_name (column1, column2 )
-- (
--     SELECT column1, 
--            column2 
--     FROM 
--         table1, 
--         table2
--     WHERE 
--         {VALUE OPERATOR }
-- );
-- Note the subquery INSERT doesn't require the use of the VALUES keyword.


INSERT INTO rental_replacements (amount, payment_date, staff_id) 
(
    SELECT amount, payment_date, staff_id 
    FROM 
        payment 
    WHERE 
        amount >= 9.99
);

-- Which inserts all records into the new rental_replacements table with a payment amount >= 9.99.


-- *******************************UPDATE Subquery Operations***********************************

-- Updating a table can be done with the following syntax:

-- [ ]
-- UPDATE {table_name}  
-- SET 
--     column_name = new_value
-- WHERE 
--     {VALUE OPERATOR}
--     (
--         SELECT COLUMN_NAME
--         FROM {TABLE_NAME)     
--         WHERE {VALUE OPERATOR}
--     );
-- Let's imagine there is an error in our rental table. All payments taken for movies with amount = 0.99 were actually sold by the staff member with staff_id = 1. So we can use the payments table to get all the rental_id's WHERE the staff_id = 2. Then we match it with the rental_id's in the rental table since they're unique. This is how to perform the query:


UPDATE rental
SET 
    staff_id = 1
WHERE 
    rental_id IN
    (
        SELECT rental_id
        FROM 
            payment
        WHERE
    );
-- The inside query returns all rental_id's with amount = 0.99 and staff_id = 2, which are the records we want to UPDATE in the rental table. We then use the WHERE statement of the outer query to match all rental_id's found by the subquery. Finally we set the staff_id = 2 since these are the records we want to UPDATE.

-- *******************************DELETE Subquery Operations***********************************

-- Using subqueries to DELETE records has similar syntax to INSERT with subqueries, with the addition of a WHERE clause to filter the records to DELETE.

-- [ ]
-- DELETE FROM table_name (column1, column2 )
-- WHERE
--     {VALUE OPERATOR}
-- (
--     SELECT column1, 
--            column2 
--     FROM 
--         table1, 
--         table2
--     WHERE 
--         {VALUE OPERATOR }
-- );
-- Let's DELETE all rentals from the rental table where an amount hasn't been taken since the 28th of January 2007:


DELETE FROM rental
WHERE 
    rental_id IN
    (
        SELECT rental_id
        FROM 
            payment
        GROUP BY 
            rental_id
        HAVING
            MIN(payment_date) <=  '2007-01-29' 
    );

-- We actually get an error, that the records can't be deleted since they violate a constraint, which is good database design. This stops the records being removed as another table depends on them. We could remove the primary key constraint from the rental table with a CASCADE such that we can then DELETE the records.

-- First we need to find the name of the constraint. This can be done by querying the databases information_schema. The information schema holds metadata information about the database such as the name, tables, constraints and privileges among others.

-- In particular, the information_schema has a table called table_constraints, where we can view the names of all constraints in the database. We can query it like any other table:

SELECT * FROM information_schema.table_constraints
Notice one of the columns is named table_name, so we can query it to check for all constraints in the rental table:


SELECT * FROM information_schema.table_constraints
WHERE table_name = 'rental';

-- We can see that the primary key constraint is called rental_pkey. 
-- This is the constraint we need to drop. Since other tables rely on this constraint 
-- we will need to use CASCADE to drop the constraint and any foreign keys that rely on this column.


ALTER TABLE rental    
DROP CONSTRAINT rental_pkey CASCADE;

-- Now that the constraint has been removed we should be able to drop the records. Rerun the DELETE query and it should result in the records being removed.










