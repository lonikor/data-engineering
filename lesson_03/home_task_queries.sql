/*
 Завдання на SQL до лекції 03.
 */


/*
1.
Вивести кількість фільмів в кожній категорії.
Результат відсортувати за спаданням.
*/
-- SQL code goes here...

SELECT c.name AS category, COUNT(f.film_id) AS film_count
FROM category AS c
JOIN film_category AS fc ON c.category_id = fc.category_id
JOIN film AS f ON fc.film_id = f.film_id
GROUP BY category
ORDER BY film_count DESC;

/*
2.
Вивести 10 акторів, чиї фільми брали на прокат найбільше.
Результат відсортувати за спаданням.
*/
-- SQL code goes here...

SELECT a.first_name, a.last_name, COUNT(*) AS films_rented
FROM actor AS a
JOIN film_actor AS fa ON a.actor_id = fa.actor_id
JOIN inventory AS i ON fa.film_id = i.film_id
JOIN rental AS r ON i.inventory_id = r.inventory_id
GROUP BY a.actor_id
ORDER BY films_rented DESC
LIMIT 10;

/*
3.
Вивести категорію фільмів, на яку було витрачено найбільше грошей
в прокаті
*/
-- SQL code goes here...

SELECT c.name AS category, SUM(p.amount) AS total_spent
FROM category AS c
JOIN film_category AS fc ON c.category_id = fc.category_id
JOIN film AS f ON fc.film_id = f.film_id
JOIN inventory AS i ON f.film_id = i.film_id
JOIN rental AS r ON i.inventory_id = r.inventory_id
JOIN payment AS p ON r.rental_id = p.rental_id
GROUP BY category
ORDER BY total_spent DESC
LIMIT 1;

/*
4.
Вивести назви фільмів, яких не має в inventory.
Запит має бути без оператора IN
*/
-- SQL code goes here...

SELECT f.title
FROM film AS f
LEFT JOIN inventory AS i ON f.film_id = i.film_id
WHERE i.film_id IS NULL;

/*
5.
Вивести топ 3 актори, які найбільше зʼявлялись в категорії фільмів “Children”.
*/
-- SQL code goes here...

SELECT a.first_name, a.last_name, COUNT(*) AS film_count
FROM actor AS a
JOIN film_actor AS fa ON a.actor_id = fa.actor_id
JOIN film_category AS fc ON fa.film_id = fc.film_id
JOIN category AS c ON fc.category_id = c.category_id
WHERE c.name = 'Children'
GROUP BY a.actor_id
ORDER BY film_count DESC
LIMIT 3;