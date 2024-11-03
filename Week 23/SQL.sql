CREATE TEMPORARY TABLE temp_table AS
SELECT *
from companies c
left JOIN salaries s on s.comp_name=c.company_name
left join employees e on e.employee_code_emp=s.employee_id
left join functions f on f.function_code=s.func_code;

--ALTER TABLE employees
--RENAME COLUMN "GEN(M_F)" TO gen_m_f;

CREATE TABLE df_employee AS
SELECT 
    employee_id || '_' || CAST(date AS TEXT) AS id,  -- Use || for concatenation and CAST date to TEXT 
       DATE(date) AS month_year, 
       employee_id,
       employee_name, 
	   gen_m_f, 
	   age,
       salary,
       function_group, 
       company_name, 
       company_city, 
       company_state, 
       company_type, 
       const_site_category
FROM temp_table;

UPDATE df_employee
SET
id = TRIM(id),
employee_name= TRIM(employee_name),
gen_m_f=TRIM(gen_m_f),
salary=TRIM(salary),
function_group=TRIM(function_group),
company_name=TRIM(company_name),
company_city=TRIM(company_city),
company_state=TRIM(company_state),
company_type=TRIM(company_type),
const_site_category=TRIM(const_site_category);


SELECT *
from df_employee
where 
id is NULL OR
month_year is null OR
employee_id is NULL OR 
employee_name is null OR
gen_m_f is NULL OR
age is NULL OR
salary is NULL OR
function_group IS NULL OR
company_name IS NULL OR
company_city IS NULL OR
company_state IS NULL OR
company_type is NULL OR
const_site_category IS NULL;

DELETE from df_employee
where salary is null;

select company_name, count(employee_id) as NumEmployees
from df_employee
group by company_name
order by NumEmployees desc;

select company_city, COUNT(employee_id), 
ROUND(COUNT(employee_id) * 100.0 / SUM(COUNT(employee_id)) OVER(), 2) AS Percentage
FROM  df_employee
group by company_city;

SELECT EXTRACT(day from month_year) as Month, count(employee_id) as NumEmployees
from df_employee
group by EXTRACT(day from month_year)
order by EXTRACT(day from month_year);

--Average number of employees per month

SELECT EXTRACT(day from month_year) as Month, count(employee_id)/count(DISTINCT month_year) as AVGEmployees
from df_employee
group by EXTRACT(day from month_year)
order by EXTRACT(day from month_year);

--What is the minimum and maximum number of employees throughout all the months?
--In which months were they?

SELECT EXTRACT(day from month_year) as Month, COUNT(DISTINCT employee_id) as MinEmployees
from df_employee
group by EXTRACT(day from month_year)
ORDER BY MinEmployees ASC
limit 1

SELECT EXTRACT(day from month_year) as Month, COUNT(DISTINCT employee_id) as MaxEmployees
from df_employee
group by EXTRACT(day from month_year)
ORDER BY MaxEmployees DESC
limit 1

--What is the monthly average number of employees by function group?
select *
from functions

select function_group, count(employee_id)/count(DISTINCT function_group) as AVGEmployees
from df_employee
group by function_group

--What is the annual average salary?

select sum(salary::float)/count(DISTINCT employee_id) as AverageSalary
from df_employee

select salary
from df_employee



