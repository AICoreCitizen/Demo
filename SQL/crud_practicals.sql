

/*Creating tables
Let's look at the syntax of creating some tables with constraints:
*/

CREATE TABLE movies (
    title VARCHAR(30) PRIMARY KEY,
    release_date DATE NOT NULL,
    premier_access DATE,
    minutes INT CONSTRAINT positive CHECK (minutes > 0),
    CONSTRAINT valid_premier CHECK (release_date >
    premier_access)
);

-- PRIMARY KEY constraint applied to the title column to ensure that it is always unique since movies have unique names. 
-- Constraints applied to both the minutes and release_date to check the minutes is greater than 0 and release_date is not null.
-- We have the following constraint CONSTRAINT valid_premier CHECK (release_date >premier_access). Note we didn't define a column to apply the constraint to.
-- Define a table CONSTRAINT using the syntax CONSTRAINT <name of the constraint>, 
-- in our case it's defined with the name valid_premier and checks that the release date is greater than the premier access date.

CREATE TABLE IF NOT EXISTS employee_info (
    first_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(100),
    last_name VARCHAR(100) NOT NULL,
    staff_id CHAR(8) PRIMARY KEY,
    birth_date DATE CHECK (birth_date > (NOW() - INTERVAL '18 years')),
    date_joined DATE NOT NULL CHECK (date_joined < NOW()),
    monthly_hours SMALLINT NOT NULL CHECK (monthly_hours >= 8),
    salary INTEGER NOT NULL CHECK (salary >= (8 * 7.70 * 52))
);

-- With this statement we've used a combination of different constraints to ensure the data entered makes sense for the company:

-- IF NOT EXISTS : Creates the table only if the table doesn't already exist
-- first_name/last_name : Are both varying character lengths and not nullable (of a good size for names 100)
-- middle_name : Varying character length and nullable as not everyone has a middle name
-- staff_id : Is of fixed length (8 characters) and primary key as this will be an unique non-nullable identifier for each employee
-- birth_date : Is a date value of the year of birth. We have also in included a CHECK here to ensure the staff member is over 18 years of age, (birth_date > (NOW() - INTERVAL '18 years'). NOW(), represents the current time as a timestamp and with the interval INTERVAL '18 years' subtracted to check the birth_date > is greater than 18 years.
-- date_joined DATE NOT NULL CHECK (date_joined < NOW()) : Checking the join date is less than the exact current time
-- monthly_hours SMALLINT NOT NULL CHECK (monthly_hours >= 8) : The hours are of type SMALLINT and we're checking the monthly_hours is at least 8 hours, since the companies minimum contract is 8 hours
-- salary INTEGER NOT NULL CHECK (salary > 0) : Salary is an INTEGER not SMALLINT since it could potentially be greater than 32767. We also added a check to ensure it's greater than 8 hours * 7.70 minimum wage * 52 weeks since this is the minimum an employee can earn.
-- The constraints you apply to data will be different depending on the use case. When creating constraints you should think what constraints would best model the particular data you expect in the table.


-- Creating tables using SELECT (Where data already exists, creating tables using the SELECT statement can be a better option to create a table. )

CREATE TABLE budget_films AS (
    SELECT title,
           description,
           release_year,
           rental_duration,
           replacement_cost,
           rating,
           rental_rate
    FROM 
        film
    WHERE 
        rental_rate = 0.99
);

/* PRACTICALS
Use a SELECT statement to create a table called payments_this_year
SELECT all columns from the payment table
Only take the payments from the year 2007
*/

CREATE TABLE payments_this_year AS (
    SELECT *
    FROM
        payment
    WHERE
        payment_date >  '2007-01-01 00:00:00'


);








/*Reading tables
Let's look at the syntax of creating some tables with constraints:
*/



/*Updating tables


the UPDATE keyword is used to modify data already existing in the database. When combined with the WHERE statement you can accurately target rows or data you want to update.

The syntax to update rows has the structure:

[ ]
UPDATE {table_name}
SET 
    {column_1} = {column_value_1}
    {column_2} = {column_value_2}
    ...
WHERE {condition}

We tell SQL which columns we want to change the values of with the SET keyword. 
Which specifies the column to change and the value to change it to. 
Notice in the structure of the query we can change multiple columns at once.

The WHERE keyword is then used as a conditional to check for the correct rows to update.

WHERE conditions can match multiple rows, so there's the possibility you might update multiple rows by accident when this wasn't intended. 
This is more likely to happen when using a LIKE statement to pattern match the rows. 
It's preferable to use the explicit WHERE column = '<value>' statements to ensure targeting of the correct information.

*/

SELECT title 
FROM film
WHERE title LIKE 'AIR%';

-- This query actually returned two films AIRPLANE SIERRA and AIRPORT POLLOCK, let's be more specific to avoid updating with incorrect information.


SELECT title
FROM film
WHERE title = 'AIRPLANE SIERRA';


-- Perfect, we got an exact match, so we can use this in our UPDATE statement. Let's use the condition to update the rental_rate and the release_year columns. There was an error with the original data, the release year it was actually 2008 and the price has dropped to 2.99.

UPDATE film
    SET rental_rate = 2.99,
        release_year = 2010
WHERE 
    title = 'AIRPLANE SIERRA';
-- Since we confirmed that we were selecting the correct data using the SELECT/WHERE query, the UPDATE has been applied to the desired row.

-- UPDATE can also be used if the constraints allow, to clear the values in the rows using NULL:

UPDATE film
    SET rental_rate = NULL,
        release_year = NULL
WHERE 
    title = 'AIRPLANE SIERRA';



-- For example, if you have a table called APP with a column called DT that contains dates in the format yyyy-MM-dd, and you want to change it to dd-MM-yyyy, you can write:

-- SELECT FORMAT (DT, ‘dd-MM-yyyy’) AS new_date FROM APP;

-- This will return a new column called new_date with the dates in the format dd-MM-yyyy. 
-- SELECT FORMAT (‘2007-01-24 21:40:19.996577’, ‘yyyy-MM-dd HH:mm:ss’) AS new_date;


/* PRACTICALS
Using the Pagila database:

In the payments_this_year table you create in the previous notebook
Alter the payment_date column and remove the millisecond from the timestamp
Drop the payment_id column
Set the staff_id to 1 where amount = 3.99 and customer_id = 87 and 137`
There was a service charge of 50 pence added after '2007-03-22'. Update the amount columns rows with the service charge after this date.
rename the amount column to total_payment_taken
*/
-- Alter the payment_date column and remove the millisecond from the timestamp
ALTER TABLE payments_this_year
    ALTER COLUMN payment_date TYPE TIMESTAMP USING payment_date::timestamp(0);
-- Drop the payment_id column   
ALTER TABLE payments_this_year
    DROP COLUMN payment_id;
-- Set the staff_id to 1 where amount = 3.99 and customer_id = 87 and 137
UPDATE payments_this_year
    SET staff_id = 1
WHERE 
    amount = 3.99 AND
    customer_id IN (87, 137);

-- There was a service charge of 50 pence added after '2007-03-22'. 
-- Update the amount columns rows with the service charge after this date.
UPDATE payments_this_year
    SET amount = amount + 0.50
WHERE 
    payment_date >= '2007-03-23 00:00:00'
    
-- rename the amount column to total_payment_taken
ALTER TABLE payments_this_year
    RENAME amount TO total_payment_taken



-- OR

-- ALTER TABLE payments_this_year ALTER COLUMN DT varchar (10);

-- UPDATE payments_this_year SET payment_date = CONVERT (varchar (10), payment_date, 103);

/*Deleting tables
In some case you may want to completely drop a table of data, maybe it's outdated, or can't be kept any longer for data protection reasons.
Additionally you might have made a mistake when creating the table and just want to start from scratch.
  You can drop tables with the following syntax:
  DROP TABLE [IF EXISTS] table_name [CASCADE | RESTRICT]
*/

-- Remove table data

-- When being tasked with dropping tables, always try to drop the table in restricted mode first, 
-- even though it will throw an error. The error returned will tell you the reasons why you can't drop the table 
-- and what relationships it has with other objects. 
-- By doing this, you will understand the impact of dropping table 
-- could have on your database and make a decision whether you can drop it safely.

-- We can specify only to drop the table if SQL can find it using IF EXISTS.
-- RESTRICT: This is the default, unless specified otherwise. It can help to include it for code readability though. 
-- With RESTRICT SQL will not drop the table if the table depends on or has a relationship with another table.

-- CASCADE: If the table to be dropped has a relationship with or depends on another table then dropping the table 
-- will also destroy all objects and relationships that depend on that table. 

-- For instance if you had table A which referenced table B by FOREIGN KEY dropping table B with CASCADE would destroy the FOREIGN KEY constraint in table A.
-- Table A would still keep its data but the relation between the tables will be destroyed.

-- TRUNCATE: You also have the option to remove the data from the table without completely destroying the table. 
-- TRUNCATE {table_name} [ RESTART IDENTITY | CONTINUE IDENTITY ] [CASCADE | RESTRICT]

-- This can be helpful if you want to insert fresh data into a table or maybe remove the original contents due to data protection.



-- This can be helpful if you want to insert fresh data into a table or maybe remove the original contents due to data protection. The CONTINUE IDENTITY and RESTART IDENTITY keywords options either continue a sequence from the last known value or restart a sequence.
-- A sequence is an increasing or decreasing set of values which can be inserted into a column automatically. Sequenced columns do not reset when the table is truncated, the default is CONTINUE IDENTITY. If you had a column increasing in values 1,2,3... and set RESTART IDENTITY the sequence would begin again from 1,2,3... 1 or if CONTINUE IDENTITY was set it would start from the the next known value.
-- Sequences can be created with the syntax:

-- CREATE SEQUENCE [IF NOT EXISTS] {TEMP | TEMPORARY} {sequence name} {data_type} {increment} {minvalue} {maxvalue} {start} {CYCLE | NO CYCLE}

-- IF NOT EXISTS: To ensure to only create the sequence if it doesn't exists

-- TEMP | TEMPORARY: The sequence will only exist while connected to the database for the current session

-- data type: Represents the data type of the sequence

-- increment: How to increment the sequence on the next value. The default is increment by 1.

-- minvalue: The minimum value the sequence can hold

-- maxvalue: The maximum value the sequence can hold
-- start: What value to start the sequence at (doesn't have to be the minvalue)
-- CYCLE | NO CYCLE: Whether the sequence repeats after reaching the maxvalue
-- For instance if we wanted a cyclical sequence ending in 10 and starting at 1, we could do so with the following statement:


CREATE SEQUENCE staff_id_counter AS INTEGER increment BY 1 minvalue 1 maxvalue 10 CYCLE

-- The next value in the sequence can be selected in the following way:

SELECT nextval('staff_id_counter')

-- The current value can be retrieved with:

SELECT currval('staff_id_counter')


/*
Adding/removing columns
*/

-- Manipulations of columns are done using the ALTER TABLE statement with the following syntax:
-- ALTER TABLE {table_name} 
--     ADD COLUMN {column name} {data_type} {constraint};

ALTER TABLE rental
    ADD COLUMN available BOOLEAN NOT NULL DEFAULT True;

-- Notice the additional statement keyword DEFAULT was added with the value set to True. Since we set column constraint to be NOT NULL, we needed to set the default value as the column can't contain NULL values. SQL would throw an error if we didn't set this default value.

-- Dropping columns can also be done using the syntax:
-- ALTER TABLE {table_name}
--     DROP COLUMN {column_name} [ RESTRICT | CASCADE ];

ALTER TABLE rental
    DROP COLUMN available;

-- Again we can choose to cascade the dropping of constraints and relationships if another table depends on the column.

/*
Renaming columns and tables
*/

-- To change this name of a table use the following syntax:

-- [ ]
-- ALTER TABLE {table_name}
--     RENAME TO {new_table_name};


-- Column renaming can be done with:

-- [ ]
-- ALTER TABLE {table_name}
--     RENAME {previous_column_name} TO {new_column_name};

-- Changing column types

-- The syntax to alter the column data type is:


-- ALTER TABLE {table_name}
--     ALTER COLUMN {column_name} TYPE {data type};
-- We could remove the time zone from the rental_date column in the rental table by casting it to a timestamp without time zone:


ALTER TABLE rental
    ALTER COLUMN rental_date TYPE TIMESTAMP without TIME ZONE;


-- Although casting is great for quickly converting column types, it won't work in all cases. 
-- The current data type to be cast has to be of the correct form to be cast to the new value. 
-- For example you can't cast a timestamp to an integer, but casting an integer to another numerical type like a real would be possible.

/*
Adding/Removing constraints
*/

-- To remove constraints use the following syntax:

-- [ ]
-- ALTER TABLE {table_name}
--     DROP CONSTRAINT {name_of_the_constraint} [ RESTRICT | CASCADE]
-- Table constraints can be added with:

-- [ ]
-- ALTER TABLE {table_name}
--     ADD {table_constraint}


-- For example adding a constraint that the staff_id > 0 to the staff table:


ALTER TABLE staff
    ADD CHECK (staff_id > 0)

-- Or with a named constraint, always better to name your constraint as best practice

ALTER TABLE staff
    ADD CONSTRAINT min_staff_id CHECK (staff_id > 0)

/*
Adding new rows
To add new rows to a table we can use the following syntax:

[ ]
INSERT INTO {table_name} 
    ({column_1}, {column_2}, ....)
VALUES 
    ({column_1 value}, {column_2 value}, ......);


*/

-- Let's insert a new film category into the category table:


INSERT INTO category
    (name, last_update)
VALUES 
    ('Thriller', NOW());

-- Important to note here that the order of (name, last_update) only matters when referencing the values to be inserted. 
-- In the VALUES clause we have input ('Thriller', NOW()) to insert the category 'Thriller' at the current datetime NOW(). 
-- Since name comes first in the INSERT INTO clause Thriller will be inserting into the name column first and the timestamp NOW() inserted into the last_update column as it comes second.

-- Inserting rows with SELECT

-- Rows can be inserted with the SELECT statement using the syntax:

-- [ ]
-- INSERT INTO {table_name} 
--     ({column_1}, {column_2}, ....)
-- (SELECT query);

CREATE TABLE b_films (
    title VARCHAR(300) UNIQUE NOT NULL,
    description TEXT NOT NULL,
    release_year YEAR NOT NULL,
    rating CHAR(5) NOT NULL
);

-- Now we can insert the data using SELECT. 
-- NOTE: When selecting the data we need to select the same number of columns we want to insert and of the correct data type to insert or SQL will cause an error.

INSERT INTO B_films(title, description, release_year, rating)
(SELECT title, 
        description, 
        release_year,
        rating
    FROM
        film
    WHERE 
        title LIKE 'B%'
);


/*
Removing rows

*/

-- The syntax to delete a row from a table is:

-- DELETE FROM {table_name} 
-- WHERE {condition};

-- Remember you might want to verify you're going to delete the correct rows by first performing a SELECT statement before running a DELETE statement. In this case we will delete all rows in the actor table where the actors first_name is Ben. Since this query is so specific we can be sure we get the result we want and may not require the SELECT first. If you're ever unsure remember to use the SELECT first before the DELETE.

DELETE FROM actor
WHERE first_name = 'Ben';

















