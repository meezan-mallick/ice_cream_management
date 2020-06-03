show databases;


create database ice_creame;
use ice_creame;
create table products ( pro_id int  NOT NULL auto_increment,
pro_name varchar(30) NOT NULL,
pro_cat varchar(30) NOT NULL,
pro_quant int NOT NULL,
pro_price int NOT NULL,
decp varchar(200) NOT NULL,
primary key (pro_id)
 );

insert into products (pro_id,pro_name,pro_cat,pro_quant,pro_price,decp) 
values (101 ,"vanilla","ICE_CREAM",10,20,"made with pure sweet milk");


select pro_name,pro_cat from products where pro_cat='FROZEN_SWEETS' ;

select * from products;



insert into products (pro_name,pro_cat,pro_quant,pro_price,decp) 
values ("chocolate_chips","ICE_CREAM",10,20,"chocolate ice cream with chocolate chips");

insert into products (pro_name,pro_cat,pro_quant,pro_price,decp) 
values ("mango-shake","MILK_SHAKE",15,30,"yummy mango shake ");

insert into products (pro_name,pro_cat,pro_quant,pro_price,decp) 
values ("kesar_falooda","FALOODA",20,30,"kesar faoolda with ice cream");


insert into products (pro_name,pro_cat,pro_quant,pro_price,decp) 
values ("stawberry-sundae","SUNDAE",10,20,"stawberry sundae with cherry layers");


create table customer(name varchar(100),ph_no varchar(100));
insert into customer values('tavkim',55555);


create table bill_records ( bill_id int  NOT NULL auto_increment,
bill_date varchar(50) NOT NULL,
customer_name varchar(100) NOT NULL,
pro_name varchar(500) NOT NULL,
pro_quantity int NOT NULL,
sub_total int NOT NULL,
primary key (bill_id)
 );

select * from bill_records;






