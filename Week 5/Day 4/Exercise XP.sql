select *
from items
order by price

select *
from items
where price>80
order by price

select first_name, last_name
from customers
order by first_name
limit 3

select last_name
from customers
order by last_name desc

select *
from customer

select (first_name,last_name) as Full_Name
from customer

select distinct create_date
from customer

select *
from customer
order by first_name desc

select film_id, title, description, release_year, rental_rate
from film
order by rental_rate

select address, phone, district
from address
where district like 'Texas'

select *
from film
where film_id = 15 or film_id = 150

select film_id, title,description, length, rental_rate
from film
where title like 'African Egg'

select film_id, title,description, length, rental_rate
from film
where title like 'Af%'

select title, replacement_cost
from film
order by replacement_cost 
limit 10

select title, replacement_cost
from film
order by replacement_cost
offset 10
fetch next 10 rows only

select first_name, last_name, amount, payment_date
from customer
inner join payment on customer.customer_id = payment.customer_id

select *
from film
left join inventory on inventory.film_id = film.film_id
where inventory_id is Null

select city, country
from city
inner join country on city.country_id = country.country_id

select rental.staff_id,customer.customer_id, first_name, last_name, amount, payment_date
from customer
inner join payment on customer.customer_id = payment.customer_id
inner join rental on customer.customer_id = rental.customer_id
order by staff_id

select staff_id, customer.customer_id, first_name, last_name, amount, payment_date
from payment
inner join customer on customer.customer_id = payment.customer_id
order by staff_id
