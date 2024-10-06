create table Customer(
ID SERIAL PRIMARY KEY,
First_Name VARCHAR(50),
Last_Name VARCHAR(100) NOT NULL
)

Create Table CustomerProfile(
ID SERIAL PRIMARY KEY,
isLoggedIn Boolean,
CustomerID INT,
 CONSTRAINT fk_customer
        FOREIGN KEY(CustomerID) 
        REFERENCES Customer(ID)
)

INSERT INTO Customer(First_Name,Last_Name)
VALUES ('John','Doe'),('Jerome','Lalu'),('Lea','Rive')

INSERT INTO CustomerProfile (CustomerID, isLoggedIn)
VALUES ((select ID FROM Customer where First_Name ='John'),TRUE)

INSERT INTO CustomerProfile (CustomerID, isLoggedIn)
VALUES ((select ID FROM Customer where First_Name = 'Jerome'),FALSE)

SELECT First_Name
FROM Customer
WHERE ID IN (
SELECT CustomerID
FROM CustomerProfile
WHERE isLoggedIn = TRUE
)

SELECT First_Name, isLoggedIn
FROM Customer c
FULL JOIN CustomerProfile cp
on c.ID = cp.CustomerID

SELECT COUNT(CustomerID) as NumNotLoggedIn
FROM CustomerProfile
WHERE isLoggedIn = False

-- Part 2

CREATE TABLE Book(
book_id SERIAL PRIMARY KEY,
title VARCHAR(1000) NOT NULL,
author VARCHAR(1000) NOT NULL
)

INSERT INTO Book (title,author)
VALUES 
('Alice in Wonderland','Lewis Carrol'),
('Harry Potter','J.K Rowling'),
('To Kill a Mockingbird','Harper Lee')

CREATE TABLE Student(
student_id SERIAL PRIMARY KEY,
name VARCHAR (100) NOT NULL UNIQUE,
age int CHECK (age <= 15)
)

INSERT INTO Student (name,age)
VALUES 
('John',12),
('Lera',11),
('Patrick',10),
('Bob',14)

CREATE TABLE Library (
    book_fk_id INT,
    student_fk_id INT,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id),
    CONSTRAINT fk_book
        FOREIGN KEY (book_fk_id)
        REFERENCES Book (book_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_student
        FOREIGN KEY (student_fk_id)
        REFERENCES Student (student_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES ((SELECT book_id from Book WHERE title = 'Alice in Wonderland'),(SELECT student_id FROM Student WHERE name = 'John'),'2022/02/15'),
((SELECT book_id from Book WHERE title = 'To Kill a Mockingbird'),(SELECT student_id FROM Student WHERE name = 'Bob'),'2021/03/03'),
((SELECT book_id from Book WHERE title = 'Alice in Wonderland'),(SELECT student_id FROM Student WHERE name = 'Lera'), '2021/05/23'),
((SELECT book_id from Book WHERE title = 'Harry Potter'),(SELECT student_id FROM Student WHERE name = 'Bob'), '2021/08/12')

SELECT *
FROM Library

SELECT name, title
FROM Student s
RIGHT JOIN Library l on s.student_id = l.student_fk_id
RIGHT JOIN Book b on l.book_fk_id=b.book_id

with AliceInWonderland as
(
SELECT age, student_fk_id
FROM Student s
RIGHT JOIN Library l on s.student_id = l.student_fk_id
RIGHT JOIN Book b on l.book_fk_id=b.book_id
WHERE title='Alice in Wonderland') 

SELECT AVG(age)
FROM AliceInWonderland

DELETE FROM Student
WHERE name = 'Bob'