CREATE DATABASE IF NOT EXISTS ssbm_db;

USE ssbm_db;

create table IF NOT EXISTS event_seat_UserBooked(id int,user_srno int,username varchar(45) ,useremail varchar(45),userseat LONGTEXT,no_seat int,seattotalprice int,eventname varchar(60));

create table IF NOT EXISTS event_seatRecord(id int,eventname varchar(45),seat_srno int,seatname varchar(45),seatstatus int,no_row int,no_col int,row_count
int);

create table IF NOT EXISTS event_record(id int,ename varchar(45),eorganization varchar(65),edate varchar(45),evenue varchar(30),estarttime TIME NOT NULL,eendtime TIME NOT NULL,edesc LONGTEXT,ecol int,erow int,seatprice int);

create table IF NOT EXISTS signup_db(id int,name varchar(45),email varchar(65),password varchar(45),repassword varchar(45),customer_fields varchar(45),Skey varchar(30));


