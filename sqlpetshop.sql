create database petshop
use petshop

create table pet(
id int identity primary key,
nome varchar(30),
idade int
)