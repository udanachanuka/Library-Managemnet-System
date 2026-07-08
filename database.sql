CREATE DATABASE library_db;

USE library_db;

CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    category VARCHAR(100),
    quantity INT
);

INSERT INTO books (title, author, category, quantity)
VALUES
('GIS Fundamentals', 'Chanuka', 'Geography', 5),
('Introduction to Python', 'ABC', 'Programming', 3);
