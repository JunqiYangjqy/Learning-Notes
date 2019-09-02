--LeetCode
--------------------------------------------------------------------------------
--Combine Two Tables
-- Write your MySQL query statement below
SELECT P.FirstName, P.LastName, A.City, A.State FROM
Person P
LEFT JOIN
Address A
USING(PersonId)
--------------------------------------------------------------------------------
--Second Highest Salary
-- Write your MySQL query statement below
SELECT
IFNULL(
    (SELECT Salary FROM Employee
     GROUP BY Salary
     ORDER BY Salary DESC
     LIMIT 1 OFFSET 1),NULL
) AS SecondHighestSalary

--Nth Highest Salary
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N=N-1;
  RETURN (
      -- Write your MySQL query statement below.
      SELECT
            IFNULL (
              (SELECT Salary FROM Employee E
               GROUP BY Salary
               ORDER BY Salary DESC
               LIMIT 1 OFFSET N
              ),NULL) AS getNthHighestSalary

  );
END
--------------------------------------------------------------------------------
--Rank Scores
-- Write your MySQL query statement below
--This rank is continously
SELECT Score,
(SELECT COUNT(DISTINCT Score) FROM Scores WHERE Score >=s.Score) Rank
FROM Scores s ORDER BY Score DESC;

--Another Answer
SELECT
    a.Score AS Score,
    COUNT(DISTINCT b.Score) AS Rank --DISTINCT
FROM Scores AS a, Scores AS b
WHERE b.Score >= a.Score    -- 表b中有x个非重复值大于等于表a当前值，则表a当前成绩排名为x
GROUP BY a.id   -- 由于成绩即使重复也要显示，故通过id分组
ORDER BY a.Score DESC

--If we want an uncontinously Rank
SELECT t.score,(SELECT COUNT(s.score)+1
FROM scores s
WHERE s.score>t.score) rank
FROM scores t
ORDER BY t.score DESC;
--------------------------------------------------------------------------------
--ConsecutiveNumber
--The official answer is not applicable for other situations
SELECT DISTINCT a.Num ConsecutiveNums FROM (
SELECT t.Num ,
       @cnt:=IF(@pre=t.Num, @cnt+1, 1) cnt,
       @pre:=t.Num pre
  FROM Logs t, (SELECT @pre:=null, @cnt:=0) b) a
  WHERE a.cnt >= 3
--Author:hy3300
--URL:https://leetcode-cn.com/problems/consecutive-numbers/solution/bu-shi-yong-idqing-kuang-xia-tong-ji-by-hy3300/
--------------------------------------------------------------------------------
--Duplicate Emails
-- Write your MySQL query statement below
SELECT P.Email
FROM Person P
GROUP BY P.Email
HAVING COUNT(P.Email)>=2
--------------------------------------------------------------------------------
--Customers Who Never Order
-- Write your MySQL query statement below
SELECT c.Name AS 'Customers' FROM
Customers c
WHERE c.Id NOT IN (
    SELECT o.CustomerId
    FROM Orders o
)
--Also, we can use Left JOIN
SELECT c.Name AS 'Customers'
FROM Customers c LEFT JOIN Orders o
ON c.Id = o.CustomerId
WHERE o.Id IS NULL
--------------------------------------------------------------------------------
--Department Highest Salary
-- Write your MySQL query statement below
SELECT d.Name AS 'Department', e1.Name AS 'Employee', c.msalary AS Salary
FROM Employee e1, Department d, (SELECT DepartmentId,MAX(Salary) as msalary FROM Employee GROUP BY DepartmentId ) AS c
WHERE c.DepartmentId=d.Id
AND e1.DepartmentId=d.Id
AND e1.Salary=c.msalary

--Official Answer
SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Salary
FROM
    Employee
    JOIN
    Department ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
	)
--Author：LeetCode
--URL：https://leetcode-cn.com/problems/department-highest-salary/solution/bu-men-gong-zi-zui-gao-de-yuan-gong-by-leetcode/
--------------------------------------------------------------------------------
-- Delete Duplicate Email
-- Write your MySQL query statement below
DELETE P1 FROM 
Person P1, Person P2
WHERE P1.Email=P2.Email
AND P1.Id>P2.Id
--OR
DELETE FROM Person
WHERE Id NOT IN (  
    SELECT id FROM
   (
       SELECT MIN(Id) AS Id 
       FROM Person
       GROUP BY Email
   ) AS temp    -- 此处需使用临时表，否则会发生报错
)
--------------------------------------------------------------------------------
-- Rising Temperature
-- My answer cannot pass the last test case 13/14
-- Write your MySQL query statement below
SELECT w1.Id FROM Weather w1, Weather w2
WHERE (w1.RecordDate - w2.RecordDate)=1
AND w1.Temperature>w2.Temperature
-- We can use DATEDIFF() function in MySQL
SELECT b.Id
FROM Weather as a,Weather as b
WHERE a.Temperature < b.Temperature and DATEDIFF(a.RecordDate,b.RecordDate) = -1;
-- Author: little_bird
-- URL: https://leetcode-cn.com/problems/rising-temperature/solution/shang-sheng-de-wen-du-by-little_bird/

--------------------------------------------------------------------------------
-- Trips and Users (Difficult)
SELECT T.request_at AS `Day`, 
	ROUND( --Round() is used to control fraction
			SUM(
				IF(T.STATUS = 'completed',0,1)
			)
			/ 
			COUNT(T.STATUS),
			2
	) AS `Cancellation Rate`
FROM trips AS T
WHERE 
T.Client_Id NOT IN (
	SELECT users_id
	FROM users
	WHERE banned = 'Yes'
)
AND
T.Driver_Id NOT IN (
	SELECT users_id
	FROM users
	WHERE banned = 'Yes'
)
AND T.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY T.request_at
-- OR 
SELECT T.request_at AS `Day`, 
	ROUND(
			SUM(
				IF(T.STATUS = 'completed',0,1)
			)
			/ 
			COUNT(T.STATUS),
			2
	) AS `Cancellation Rate`
FROM Trips AS T
JOIN Users AS U1 ON (T.client_id = U1.users_id AND U1.banned ='No')
JOIN Users AS U2 ON (T.driver_id = U2.users_id AND U2.banned ='No')
WHERE T.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY T.request_at

--------------------------------------------------------------------------------
-- Department top 3 salaries (Difficult)
-- Explaination for the answer
-- 当 e1 = e2 = [4,5,6,7,8]
-- e1.Salary = 4，e2.Salary 可以取值 [5,6,7,8]，count(DISTINCT e2.Salary) = 4
-- e1.Salary = 5，e2.Salary 可以取值 [6,7,8]，count(DISTINCT e2.Salary) = 3
-- e1.Salary = 6，e2.Salary 可以取值 [7,8]，count(DISTINCT e2.Salary) = 2
-- e1.Salary = 7，e2.Salary 可以取值 [8]，count(DISTINCT e2.Salary) = 1
-- e1.Salary = 8，e2.Salary 可以取值 []，count(DISTINCT e2.Salary) = 0
SELECT
    d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
FROM
    Employee e1
        JOIN
    Department d ON e1.DepartmentId = d.Id
WHERE
    3 > (SELECT
            COUNT(DISTINCT e2.Salary)
            FROM
            Employee e2
            WHERE
            e2.Salary > e1.Salary
            AND e1.DepartmentId = e2.DepartmentId
        )
-- Author: LeetCode
-- URL: https://leetcode-cn.com/problems/department-top-three-salaries/solution/bu-men-gong-zi-qian-san-gao-de-yuan-gong-by-leetco/

-- OR
SELECT D.Name AS `Department`,E.Name AS `Employee`,E.Salary
FROM Employee AS E join Department AS D ON (E.Departmentid = D.Id)
WHERE (
    SELECT COUNT(DISTINCT E1.Salary)
    FROM Employee AS E1
    WHERE E1.Departmentid = E.Departmentid AND E1.Salary > E.Salary
) <=2

--------------------------------------------------------------------------------
-- SWAP Salary
UPDATE salary
SET sex= (CASE sex   -- we can use CASE WHEN when using UPDATE
         WHEN 'f' THEN 'm'
         ELSE 'f'
         END)  

-- OR using IF()
UPDATE salary SET sex=IF(sex = 'f', 'm','f');
-- OR unbelivable ASCII and XOR 
UPDATE salary SET sex = CHAR(ascii('m') + ascii('f') - ascii(sex));
UPDATE salary SET sex = CHAR(ASCII(sex) ^ ASCII('m') ^ ASCII('f') ); --same value XOR itself = 0

--------------------------------------------------------------------------------

