CREATE TABLE Students (
    StudentId INT PRIMARY KEY,
    StudentFirstName VARCHAR(255) NOT NULL, 
    StudentLastName VARCHAR(255) NOT NULL, 
    DepartmentID INT,
    IsFeePaid BOOLEAN 
)