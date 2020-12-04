/*
LeetCode Problem: 1350. Students With Invalid Departments
Link: https://leetcode.com/problems/students-with-invalid-departments/
Written by: Mostofa Adib Shakib
Database: MySQL
*/

# Option 1 - Faster Using LEFT JOIN
# LEFT JOIN returns all the rows from the left table even if there are no matches on the right table

SELECT Students.id, Students.name
FROM Students
LEFT JOIN Departments
ON Students.department_id  = Departments.id WHERE Departments.id IS NULL

# Option 2

SELECT Students.id, Students.name FROM Students
WHERE Students.department_id NOT IN (SELECT id FROM Departments)