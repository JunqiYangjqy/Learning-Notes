#LeetCode
--------------------------------------------------------------------------------
#Combine Two Tables
# Write your MySQL query statement below
SELECT P.FirstName, P.LastName, A.City, A.State FROM
Person P
LEFT JOIN
Address A
USING(PersonId)
--------------------------------------------------------------------------------
#Second Highest Salary
# Write your MySQL query statement below
SELECT
IFNULL(
    (SELECT Salary FROM Employee
     GROUP BY Salary
     ORDER BY Salary DESC
     LIMIT 1 OFFSET 1),NULL
) AS SecondHighestSalary

#Nth Highest Salary
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N=N-1;
  RETURN (
      # Write your MySQL query statement below.
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
#Rank Scores
# Write your MySQL query statement below
#This rank is continously
SELECT Score,
(SELECT COUNT(DISTINCT Score) FROM Scores WHERE Score >=s.Score) Rank
FROM Scores s ORDER BY Score DESC;

#Another Answer
SELECT
    a.Score AS Score,
    COUNT(DISTINCT b.Score) AS Rank --DISTINCT
FROM Scores AS a, Scores AS b
WHERE b.Score >= a.Score    -- 表b中有x个非重复值大于等于表a当前值，则表a当前成绩排名为x
GROUP BY a.id   -- 由于成绩即使重复也要显示，故通过id分组
ORDER BY a.Score DESC

#If we want a uncontinously Rank
SELECT t.score,(SELECT COUNT(s.score)+1
FROM scores s
WHERE s.score>t.score) rank
FROM scores t
ORDER BY t.score DESC;
--------------------------------------------------------------------------------
#ConsecutiveNumber
--The official answer is not applicable for other situations
SELECT DISTINCT a.Num ConsecutiveNums FROM (
SELECT t.Num ,
       @cnt:=IF(@pre=t.Num, @cnt+1, 1) cnt,
       @pre:=t.Num pre
  FROM Logs t, (SELECT @pre:=null, @cnt:=0) b) a
  WHERE a.cnt >= 3
#Author:hy3300
#URL:https://leetcode-cn.com/problems/consecutive-numbers/solution/bu-shi-yong-idqing-kuang-xia-tong-ji-by-hy3300/
