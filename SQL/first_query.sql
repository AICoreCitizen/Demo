/* This query returns the amount of rentals each customer
has made. The total amount they've paid overall and the average
of each payment. It then orders the customer by the amount they've 
paid historically in descending order */ 

SELECT customer_id, 
       SUM(amount) AS total_customer_payments,
       COUNT(rental_id) AS total_rentals_made,
       ROUND(SUM(amount) / COUNT(rental_id), 2) AS average_rental_payment
FROM
    payment
GROUP BY customer_id 
ORDER BY total_customer_payments DESC;

-- is preferable to

SELECT customer_id, 
       SUM(amount),
       COUNT(rental_id), 
       ROUND(SUM(amount) / COUNT(rental_id), 2) 
FROM
    payment
GROUP BY customer_id; 