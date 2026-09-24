ALTER TABLE Students
ADD CONSTRAINT fk_students_department
FOREIGN KEY (DepartmentID)
REFERENCES Depertement(DepertementId);
