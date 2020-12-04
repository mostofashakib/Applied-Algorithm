/*
LeetCode Problem: 1173. Immediate Food Delivery I
Link: https://leetcode.com/problems/immediate-food-delivery-i/
Written by: Mostofa Adib Shakib
Database: MySQL
*/

SELECT ROUND ( COUNT(*)/ ( SELECT COUNT(*) FROM Delivery ) * 100, 2) AS immediate_percentage
FROM Delivery
WHERE order_date = customer_pref_delivery_date