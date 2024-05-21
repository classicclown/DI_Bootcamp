-- select *
-- from students

-- select first_name,last_name
-- from students

-- select id, first_name, last_name
-- from students
-- where id=2

-- select first_name, last_name
-- from students
-- where first_name like 'Marc' and last_name like 'Benichou'

select first_name, last_name
from students
where first_name like 'Marc' or last_name like 'Benichou'

select first_name, last_name
from students
where first_name like '%a%'

select first_name, last_name
from students
where first_name like 'a%'

select first_name, last_name
from students
where first_name like '%a'

select first_name, last_name
from students
where first_name like '%a_'

select id, first_name, last_name
from students
where id=1 or id=3

select id,first_name, last_name, birth_date
from students
where birth_date>'01/01/2000'
