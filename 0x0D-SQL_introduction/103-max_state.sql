-- display max temperatures of each state
-- order by statename

SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
