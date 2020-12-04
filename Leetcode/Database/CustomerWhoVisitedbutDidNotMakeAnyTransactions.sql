/*
LeetCode Problem: 1581. Customer Who Visited but Did Not Make Any Transactions
Link: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
Written by: Mostofa Adib Shakib
Database: MySQL
*/


SELECT customer_id
FROM Visits
LEFT JOIN Transactions
ON Transactions.visit_id = Visits.visit_id WHERE Transactions.visit_id IS NULL