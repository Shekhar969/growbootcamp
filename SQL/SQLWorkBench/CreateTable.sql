CREATE TABLE Students (
    StudentId int PRIMARY KEY,
    StudentFirstName VARCHAR(255) NOT NULL, 
    StudentLastName VARCHAR(255) NOT NULL, 
    DepartmentID int,
    IsFeePaid BOOLEAN 
)