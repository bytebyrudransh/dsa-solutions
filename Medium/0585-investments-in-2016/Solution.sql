# Write your MySQL query statement below

select round(sum(i.tiv_2016) , 2) as tiv_2016
from Insurance i
where (select count(*) from Insurance where tiv_2015 = i.tiv_2015) != 1
and (select count(*) from Insurance where lat = i.lat and lon = i.lon) = 1;