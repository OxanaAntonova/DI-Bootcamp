-- select * from language;

-- select * from film LEFT JOIN language ON film.language_id=language.language_id;

-- select film.title, film.description, language.name 
-- from film INNER JOIN language ON film.language_id=language.language_id;

-- select * from language LEFT JOIN film on film.language_id=language.language_id;

-- create table new_film (
-- id serial PRIMARY KEY,
--	name varchar(100)
-- );
-- insert into new_film (name)
-- VALUES
-- ('Titanic'),
-- ('The Hobbit'),
-- ('Little Miss Sunshine')
-- ;

-- create table customer_rewiew(
-- 	review_id serial PRIMARY KEY NOT NULL,
-- 	film_id INT NOT NULL,
-- 	language_id INT NOT NULL,
-- 	title varchar(100) NOT NULL,
-- 	score INT NOT NULL,
--	review_text TEXT,
--	last_update TIMESTAMP,
	
-- CONSTRAINT fk_film_id FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
-- CONSTRAINT fk_language_id FOREIGN KEY(language_id) REFERENCES language(language_id),
-- CONSTRAINT score_value CHECK(score >0 and score <=10)	
	
--)

-- insert into customer_rewiew (film_id, language_id, title, score, review_text)
-- VALUES
-- (1, 1, 'Great movie', 10, 'The first movie I saw'),
-- (4, 1, 'Not bad', 9, 'A bit long but great story') RETURNING *
-- ;
-- DELETE FROM new_film where (name = 'Titanic') RETURNING *
-- ;


-- select * from film INNER JOIN language ON film.language_id=language.language_id;
-- UPDATE film SET language_id=2 WHERE ('Title'='Chamber Italien');
-- select * from customer;
-- INSERT into customer(first_name, last_name, store_id, address_id)
-- VALUES 
-- ('Abc', 'Def', 1, 1)
-- ;
-- select * from customer where (first_name = 'Abc');

-- DROP table customer_reviews;

-- select * from rental WHERE (return_date IS NULL);

-- select inventory.film_id, film.title, film.replacement_cost from inventory 
-- INNER JOIN film ON inventory.film_id=film.film_id;

-- select * from rental
-- INNER JOIN inventory ON rental.inventory_id=inventory.inventory_id  
-- LEFT JOIN film ON inventory.film_id=film.film_id
-- WHERE rental.return_date is NULL
-- ORDER BY replacement_cost DESC
-- LIMIT 30;

-- select film.film_id, film.title, film.fulltext from film_actor
-- INNER JOIN film on film.film_id=film_actor.film_id
-- WHERE (actor_id = 
-- (select actor_id from actor WHERE
-- (first_name='Penelope' and last_name = 'Monroe')
-- AND film.fuultext @@ to_tsquery('english', 'sumo')
-- ))	  
-- ;	  
-- select * from film;
-- INNER JOIN film_category ON film.film_id=film_category.film_id
-- INNER JOIN category ON category.category_id=film_category.category_id;
-- WHERE length < 60 and rating = 'R' and category.name = 'Documentory'
-- ;	  
	  
-- select * from inventory 
-- INNER JOIN film on film.film_id = inventory.film_id
-- INNER JOIN rental on rental.inventory_id = inventory.inventory_id
-- INNER JOIN customer ON customer.customer_id = rental.customer_id
-- WHERE customer.first_name='Matthew'
-- and customer.last_name = 'Mahan'
-- ;

















