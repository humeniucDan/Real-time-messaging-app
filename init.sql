-- PostgreSQL database dump
-- Dumped from database version ?.?
-- Dumped by pg_dump version ?.?

-- Create schema p1
CREATE SCHEMA p1;

-- Table structure for table User in schema p1
CREATE TABLE p1.User (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Data for table User in schema p1
INSERT INTO p1.User (id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie'),
(4, 'David'),
(5, 'Eve');

-- Table structure for table Messages in schema p1
CREATE TABLE p1.Messages (
    senderId INT REFERENCES p1.User(id),
    receiverId INT REFERENCES p1.User(id),
    date TIMESTAMP NOT NULL,
    content TEXT NOT NULL,
    PRIMARY KEY (senderId, receiverId, date)
);

-- Data for table Messages in schema p1
INSERT INTO p1.Messages (senderId, receiverId, date, content) VALUES
(1, 2, '2024-08-22 10:00:00', 'Hello Bob!'),
(2, 1, '2024-08-22 10:05:00', 'Hi Alice!'),
(3, 1, '2024-08-22 11:00:00', 'Good morning, Alice!'),
(4, 5, '2024-08-22 12:00:00', 'Hey Eve, what’s up?'),
(1, 3, '2024-08-22 13:00:00', 'How are you, Charlie?');

-- Table structure for table Friends in schema p1
CREATE TABLE p1.Friends (
    friend1Id INT REFERENCES p1.User(id),
    friend2Id INT REFERENCES p1.User(id),
    PRIMARY KEY (friend1Id, friend2Id)
);

-- Data for table Friends in schema p1
INSERT INTO p1.Friends (friend1Id, friend2Id) VALUES
(1, 2),
(1, 3),
(2, 3),
(4, 5),
(2, 5);
