## 1. Introducing Joins ##

SELECT * FROM facts INNER JOIN cities ON facts.id=cities.facts_id
LIMIT 10

## 2. Understanding Inner Joins ##

SELECT c.*,f.name country_name
FROM cities c inner join facts f on c.facts_id=f.id
LIMIT 5

## 3. Practicing Inner Joins ##

SELECT f.name country, c.name capital_city FROM cities c
INNER JOIN facts f ON f.id = c.facts_id
WHERE c.capital = 1

## 4. Left Joins ##

SELECT facts.name country,facts.population
FROM facts LEFT JOIN cities on facts.id=cities.facts_id
WHERE cities.name IS NULL

## 6. Finding the Most Populous Capital Cities ##

SELECT cities.name capital_city,facts.name country,cities.population population
FROM facts INNER JOIN cities ON facts.id=cities.facts_id
WHERE cities.capital=1
ORDER BY 3 DESC
LIMIT 10

## 7. Combining Joins with Subqueries ##

SELECT c.name capital_city,facts.name country,c.population population
FROM facts INNER JOIN (SELECT * 
                       FROM cities
                       WHERE population > 10000000 AND capital=1
                      ) c ON facts.id=c.facts_id
ORDER BY population DESC                      

## 8. Challenge: Complex Query with Joins and Subqueries ##

SELECT facts.name country,c.pop urban_pop,facts.population total_pop,(CAST(c.pop AS FLOAT)/CAST(facts.population AS FLOAT)) urban_pct
FROM facts INNER JOIN (SELECT facts_id,SUM(population) pop
                       FROM cities
                       GROUP BY facts_id
                      ) c ON facts.id=c.facts_id
WHERE urban_pct>0.5
ORDER BY urban_pct ASC