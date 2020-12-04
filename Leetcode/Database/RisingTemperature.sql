/*
LeetCode Problem: 197. Rising Temperature
Link: https://leetcode.com/problems/rising-temperature/
Written by: Mostofa Adib Shakib
Database: MySQL
*/

SELECT p2.id
FROM WEATHER p1, WEATHER p2
WHERE p1.Temperature < p2.Temperature AND DATEDIFF(p2.recordDate, p1.recordDate) = 1 