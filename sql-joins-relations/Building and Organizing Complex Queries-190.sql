## 3. The With Clause ##

WITH playlist_info AS 
    (
     SELECT 
         p.playlist_id playlist_id,
         p.name playlist_name,
         t.name tname,
         (t.milliseconds/1000) seconds
     FROM playlist p
     LEFT JOIN playlist_track pt ON p.playlist_id=pt.playlist_id
     LEFT JOIN track t ON pt.track_id=t.track_id
    ) 
SELECT 
    playlist_id,
    playlist_name,
    COUNT(tname) number_of_tracks,
    SUM(seconds) length_seconds    
FROM playlist_info
GROUP BY playlist_id
ORDER BY playlist_id ASC

## 4. Creating Views ##

CREATE VIEW chinook.customer_gt_90_dollars AS
    SELECT c.* 
    FROM customer c
    INNER JOIN invoice i ON c.customer_id=i.customer_id
    GROUP BY 1
    HAVING SUM(i.total)>90;
SELECT * FROM chinook.customer_gt_90_dollars;

## 5. Combining Rows With Union ##

SELECT * FROM customer_usa
UNION
SELECT * FROM customer_gt_90_dollars

## 6. Combining Rows Using Intersect and Except ##

SELECT e.first_name||' '||e.last_name employee_name,COUNT(c.customer_id) customers_usa_gt_90
FROM
    employee e
    LEFT JOIN
    (
     SELECT * FROM customer_usa
     INTERSECT
     SELECT * FROM customer_gt_90_dollars
    ) c
    ON c.support_rep_id=e.employee_id 
WHERE e.title='Sales Support Agent'    
GROUP BY employee_name
ORDER BY employee_name


## 7. Multiple Named Subqueries ##

WITH 
    india AS
        (SELECT * FROM customer WHERE country='India'),
    tot AS
        (
         SELECT india.customer_id customer_id,SUM(i.total) tota
         FROM india 
         INNER JOIN invoice i ON india.customer_id=i.customer_id
         GROUP BY i.customer_id
        )

SELECT india.first_name||' '||india.last_name customer_name,tot.tota total_purchases
FROM india INNER JOIN tot ON india.customer_id=tot.customer_id
ORDER BY customer_name

## 8. Challenge: Each Country's Best Customer ##

WITH 
    cus_inv AS
        (SELECT * FROM customer c INNER JOIN invoice i ON c.customer_id=i.customer_id),
    cus_tot AS
        (
         SELECT customer_id,SUM(total) tot_pur
         FROM cus_inv
         GROUP BY customer_id
        ),
    cus_cou AS 
        (SELECT customer_id,country FROM customer),
    cou_max AS
        (
         SELECT cc.country country,MAX(ct.tot_pur) max_pur
         FROM cus_tot ct INNER JOIN cus_cou cc ON ct.customer_id=cc.customer_id
         GROUP BY cc.country
        )
SELECT c.country country,c.first_name||' '||c.last_name customer_name,ct.tot_pur total_purchased
FROM customer c 
INNER JOIN cou_max cm ON c.country=cm.country 
INNER JOIN cus_tot ct ON c.customer_id=ct.customer_id
WHERE ct.tot_pur=cm.max_pur
ORDER BY 1
         
     