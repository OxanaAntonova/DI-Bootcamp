-- Database: Public

-- DROP DATABASE IF EXISTS "Public";

-- CREATE DATABASE "Public"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'Russian_Russia.1251'
--     LC_CTYPE = 'Russian_Russia.1251'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- create table items (
-- id serial primary key,
-- name varchar,
-- price integer
-- );

-- create table customers (
-- id serial primary key,
-- first_name varchar,
-- second_name varchar
-- );

-- insert into items (name,  price)
-- values
-- ('Small Desk', 100),
-- ('Large Desk', 300),
-- ('Fan', 80)
-- ;

-- insert into customers (first_name, second_name)
-- values
-- ('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- (' Scott', 'Scott'),
-- ('Trevor', 'Green'),
-- ('Melanie', 'Johnson')
-- ;

select * from items;
select * from items where price > 80;
select * from items where price <= 300;
select * from customers where second_name = 'Smith';
select * from customers where second_name = 'Jones';
select * from customers where first_name != 'Scott';

