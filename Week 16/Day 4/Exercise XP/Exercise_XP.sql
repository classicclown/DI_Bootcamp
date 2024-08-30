--Task 1: Rank Movies by Popularity within Each Genre
--Use the RANK() function to rank movies by their popularity within each genre. Display the genre name, movie title, and their rank based on popularity.
set search_path to movies

select g.genre_name,m.title,
rank() over (partition by mg.genre_id order by popularity) as PopularityRank
from movie m
join movie_genres mg on m.movie_id = mg.movie_id
join genre g on mg.genre_id=g.genre_id

--Task 2: Identify the Top 3 Movies by Revenue within Each Production Company
--Use the NTILE() function to divide the movies produced by each production company into quartiles based on revenue. 
--Display the company name, movie title, revenue, and quartile.

with Quartile as(
select pc.company_name,m.title, m.revenue,
ntile(3) over (partition by pc.company_name order by m.revenue desc) as Quartile
from movie m
join movie_company mc on m.movie_id=mc.movie_id
join production_company pc on mc.company_id=pc.company_id)

select company_name,title,revenue,Quartile
from Quartile
where quartile =1
order by company_name, revenue desc

--Use the SUM() function with the ROWS frame specification to calculate the running total of movie budgets within each genre. 
--Display the genre name, movie title, budget, and running total budget.

select g.genre_name,m.title, m.budget,
sum(budget) over (partition by g.genre_name order by m.budget rows between 1 preceding and 1 following) as RunningTotal
from movie m
join movie_genres mg on m.movie_id = mg.movie_id
join genre g on mg.genre_id=g.genre_id

--Use the FIRST_VALUE() function to find the most recent movie within each genre based on the release date. 
--Display the genre name, movie title, and release date.

select distinct(g.genre_name),
first_value(title) over (partition by genre_name order by release_date desc) as Title,
first_value(release_date) over (partition by genre_name order by release_date desc) as ReleaseDate
from movie m
join movie_genres mg on m.movie_id = mg.movie_id
join genre g on mg.genre_id=g.genre_id
order by genre_name

--Exercise 2

--Use the DENSE_RANK() function to rank actors based on the number of movies they have appeared in. Display the actor’s name and their rank.

select person_name,
dense_rank() over (order by count(mc.person_id) desc) as NumMoviesRanked
from person p
join movie_cast mc on p.person_id = mc.person_id
group by person_name


--Use a CTE and the RANK() function to find the director with the highest average movie rating. 
--Display the director’s name and their average rating.



with HighestAvgRatings as(
select person_name, (avg(vote_average)) as AvgRating,
rank() over (order by avg(vote_average) desc) as RatingRank
from movie_crew mc
join person p on mc.person_id=p.person_id
join movie m on mc.movie_id=m.movie_id
where job='Director'
group by person_name)

select person_name, AvgRating, RatingRank
from HighestAvgRatings
where RatingRank=1

--Use the SUM() function to calculate the cumulative revenue of movies acted by each actor. 
--Display the actor’s name and the cumulative revenue.

select person_name, revenue,
sum(revenue) over (partition by mc.person_id order by revenue desc) as CumulativeRevenue
from person p
join movie_cast mc on p.person_id=mc.person_id
join movie m on mc.movie_id=m.movie_id

--Use a CTE and a window function to find the director whose movies have the highest total budget. 
--Display the director’s name and the total budget.

with TotalBudget as (
select person_name, 
sum(budget) over (partition by mc.person_id) as Budget
from movie_crew mc
join person p on mc.person_id=p.person_id
join movie m on mc.movie_id=m.movie_id
where job='Director')

select person_name, Budget
from TotalBudget
group by person_name, Budget
order by Budget desc




