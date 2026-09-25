SELECT salary FROM Teacher ORDER BY salary DESC LIMIT 1,1;

SELECT * FROM Teacher;

SELECT * FROM Depertement;

SELECT * FROM Students;

SELECT AVG(salary) As AverageTeacherSalary FROM Teacher;

SELECT MIN(salary) As MinimunTeacherSalary, MAX(salary) AS MaximumTeacherSalary FROM Teacher;


SELECT s.StudentId, s.StudentFirstName, s.StudentLastName, d.DepertementName
FROM Students s INNER JOIN Depertement d ON s.DepartmentID = d.DepertementId;

SELECT d.DepertementId, d.DepertementName,s.StudentFirstName
FROM Depertement d LEFT JOIN Students s ON d.DepertementId = s.DepartmentID;

SELECT d.DepertementName,COUNT(s.StudentId) AS TotalStudents
FROM Depertement d LEFT JOIN Students s ON d.DepertementId = s.DepartmentID
GROUP BY d.DepertementId, d.DepertementName
ORDER BY TotalStudents DESC;

SELECT StudentFirstName, StudentLastName,
CASE
WHEN IsFeePaid = 1 THEN 'Paid'
WHEN IsFeePaid = 0 THEN 'Not Paid'
ELSE 'Unknown'
END AS FeeStatus
FROM Students;
