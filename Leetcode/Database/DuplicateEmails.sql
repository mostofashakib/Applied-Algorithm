/*
LeetCode Problem: 182. Duplicate Emails
Link: https://leetcode.com/problems/duplicate-emails/
Written by: Mostofa Adib Shakib
Database: MySQL
*/

# Option 1


SELECT Email FROM Person Group BY Email Having Count(Email) > 1

# Option 2

SELECT DISTINCT p1.Email
FROM Person p1, Person p2
WHERE p1.Email = p2.Email AND p1.Id != p2.Id