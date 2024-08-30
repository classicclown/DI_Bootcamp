-- Task 1: Calculate The Average Budget Growth Rate For Each Production Company
--Calculate the average budget growth rate for each production company across all movies they have produced. 
--Use window functions to determine the budget growth rate and then calculate the average growth rate.
set search_path to movies

with Budgets as (
select pc.company_name, m.release_date,budget,
(LEAD(budget, 1) OVER (PARTITION BY pc.company_name ORDER BY m.release_date)-budget) as Rate
from production_company pc
join movie_company mc on mc.company_id=pc.company_id
join movie m on m.movie_id=mc.movie_id
where budget!=0)

select company_name, round(avg(rate/budget*100),2) as AvgRate
from Budgets
where rate!=0
group by company_name

--Task 2: Determine The Most Consistently High-Rated Actor
--Identify the actor who has appeared in the most movies that are rated above the average rating of all movies. 
--Use window functions and CTEs to calculate the average rating and filter the actors based on this criterion.

with AvgRating as(
select avg(vote_average) as AvgRating
from movie),

HighestRatedMovies as(
select movie_id,title
from movie m, AvgRating
where vote_average>AvgRating)

select person_name, count(mc.movie_id) as CountMovies
from HighestRatedMovies hr
join movie_cast mc on hr.movie_id=mc.movie_id
join person p on p.person_id=mc.person_id
group by person_name
order by count(mc.movie_id) desc
limit 1

--Task 3: Calculate The Rolling Average Revenue For Each Genre
--Calculate the rolling average revenue for movies within each genre, considering only the last three movies released in the genre.
--Use window functions with the ROWS frame specification to achieve this

with RollingAvg as (
select genre_name,revenue, release_date,
avg (revenue) over (partition by genre_name order by release_date rows between 2 preceding and current row ) as RollingAverage,
row_number() over (partition by genre_name order by release_date desc) as RowNumber
from genre g
join movie_genres mg on mg.genre_id=g.genre_id
join movie m on m.movie_id = mg.movie_id
)

select genre_name, round(RollingAverage,0)
from RollingAvg
where RowNumber =1
group by genre_name, RollingAverage

--Task 4: Identify The Highest-Grossing Movie Series
--Identify the movie series (based on shared keywords) with the highest total revenue. 
--Use window functions and CTEs to group movies by their series and calculate the total revenue.

with KeywordSeries as(
select keyword_name,
sum(revenue) over (partition by mk.keyword_id) as Revenue
from movie m
join movie_keywords mk on m.movie_id=mk.movie_id
join keyword k on k.keyword_id=mk.keyword_id)

select distinct(keyword_name), revenue
from KeywordSeries
order by revenue desc