select 
visited_on, 
avg(time_spent) over(order by visited_on asc ROWS  3 ) from


select t1.`visited_on`, AVG(t2.`time_spent`) as MV_AVG
from traffic t1
left outer join traffic t2 
    on t2.`visited_on` between DATE_ADD(t1.`visited_on`, INTERVAL -6 DAY) 
        and t1.`visited_on`
group by t1.`visited_on`