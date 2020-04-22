/*
569. Median Employee Salary
The Employee table holds all employees. The employee table has three columns: Employee Id, Company Name, and Salary.

+-----+------------+--------+
|Id   | Company    | Salary |
+-----+------------+--------+
|1    | A          | 2341   |
|2    | A          | 341    |
|3    | A          | 15     |
|4    | A          | 15314  |
|5    | A          | 451    |
|6    | A          | 513    |
|7    | B          | 15     |
|8    | B          | 13     |
|9    | B          | 1154   |
|10   | B          | 1345   |
|11   | B          | 1221   |
|12   | B          | 234    |
|13   | C          | 2345   |
|14   | C          | 2645   |
|15   | C          | 2645   |
|16   | C          | 2652   |
|17   | C          | 65     |
+-----+------------+--------+
Write a SQL query to find the median salary of each company. Bonus points if you can solve it without using any built-in SQL functions.

+-----+------------+--------+
|Id   | Company    | Salary |
+-----+------------+--------+
|5    | A          | 451    |
|6    | A          | 513    |
|12   | B          | 234    |
|9    | B          | 1154   |
|14   | C          | 2645   |
+-----+------------+--------+
*/
-- Solution 1:               
select
  t1.Id as Id,
  t1.Company,
  t1.Salary
from Employee as t1
inner join Employee as t2 on t1.Company = t2.Company
group by
  t1.Id
having
  abs(
    sum(
      CASE
        when t2.Salary < t1.Salary then 1
        when t2.Salary > t1.Salary then -1
        when t2.Salary = t1.Salary
        and t2.Id < t1.Id then 1
        when t2.Salary = t1.Salary
        and t2.Id > t1.Id then -1
        else 0
      end
    )
  ) <= 1
order by
  t1.Company,
  t1.Salary,
  t1.Id