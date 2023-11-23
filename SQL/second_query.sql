SELECT customer_id, 
       SUM(amount) AS total_customer_payments,
       COUNT(rental_id) AS total_rentals_made,
       ROUND(SUM(amount) / COUNT(rental_id), 2) AS average_rental_payment
FROM
    payment
GROUP BY customer_id 
ORDER BY total_customer_payments DESC;

/*
Don't sacrifice readability with *, 
if you could make the query more understandable without it.
*/

/* The queries here will return the release year, description, title
of all films which actors who's first name is Nick. */

SELECT actor.first_name,
       actor.last_name,
       film.title AS film_title,
       film.release_year AS film_release_year, 
       film.description AS film_description
FROM 
    actor
JOIN 
    film_actor ON actor.actor_id = film_actor.actor_id
JOIN 
    film ON film_actor.film_id = film.film_id
WHERE 
    first_name = 'NICK';

-- is preferable to

SELECT * 
FROM 
    actor
JOIN 
    film_actor ON actor.actor_id = film_actor.actor_id
JOIN 
    film ON film_actor.film_id = film.film_id
WHERE 
    first_name = 'NICK';