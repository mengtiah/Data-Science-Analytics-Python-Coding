## 1. Introducing Joins ##

SELECT *
from facts f
join cities c
on f.id=c.facts_id
LIMIT 10

## 2. Understanding Inner Joins ##

SELECT c.*,f.name country_name
FROM cities c
JOIN facts f
on c.facts_id=f.id
LIMIT 5


## 3. Practicing Inner Joins ##

SELECT f.name country,c.name capital_city
FROM facts f
join cities c
on f.id=c.facts_id
WHERE c.capital=1

## 4. Left Joins ##

SELECT f.name country,f.population
from facts f
LEFT JOIN cities c
on f.id=c.facts_id
where c.name is NULL

## 6. Finding the Most Populous Capital Cities ##

SELECT c.name capital_city,f.name country, c.population
from facts f
JOIN cities c
on f.id=c.facts_id
WHERE C.capital=1
ORDER BY C.population DESC
LIMIT 10

## 7. Combining Joins with Subqueries ##

SELECT C.name capital_city,F.name country, C.population
FROM facts F
JOIN cities C
ON F.id=C.facts_id
WHERE C.capital=1 AND C.population>10000000
ORDER BY 3 DESC


## 8. Challenge: Complex Query with Joins and Subqueries ##

SELECT F.name country, C.urban_pop,F.population total_pop,
(C.urban_pop/CAST(F.population AS FLOAT)) urban_pct
FROM facts F
JOIN (
    SELECT facts_id, SUM(population) urban_pop
    FROM cities
    GROUP BY 1) C
    ON C.facts_id=F.id
WHERE urban_pct>0.5
ORDER BY 4 