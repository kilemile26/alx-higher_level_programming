-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).using imported table dump.
SELECT city, AVG(temperature) AS average_temperature FROM temperatures GROUP BY city ORDER BY average_temperature DESC;
