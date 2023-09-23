-- Database: Bootcamp

-- DROP DATABASE IF EXISTS "Bootcamp";

-- CREATE DATABASE "Bootcamp"
--     WITH
--    OWNER = postgres
--    ENCODING = 'UTF8'
--    LC_COLLATE = 'Russian_Russia.1251'
--    LC_CTYPE = 'Russian_Russia.1251'
--    TABLESPACE = pg_default
--    CONNECTION LIMIT = -1
--    IS_TEMPLATE = False;

-- create table student (
-- id serial primary key,
-- first_name varchar,
-- last_name varchar,
-- birth_date date
-- );

-- insert into student (first_name, last_name, birth_date)
-- values
-- ('Marc', 'Benichou', '1998-11-02'),
-- ('Yoan',	'Cohen','2010-12-03'),
-- ('Lea',	'Benichou',	'1987-07-27'),
-- ('Amelia',	'Dux',	'1996-04-07'),
-- ('David',	'Grez',	'2003-06-14'),
-- ('Omer', 'Simpson',	'1980-10-03'),
-- ('Oxana', 'Antonova', '1977-05-15')
-- ;
-- select * from student;
-- select first_name, last_name from student;
-- select * from student where first_name = 'Marc' or last_name = 'Benichou';
-- select * from student where first_name like 'A%';
-- select * from student where first_name like '%a';
-- select * from student where first_name like '%a%';
-- select * from student where id in (1, 3);
-- select * from student where birth_date >= '2000-01-01';




