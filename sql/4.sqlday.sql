SELECT * FROM orders;

select * from customers;

-- Inner Join

select * from customers join orders on customers.customer_id = orders.customer_id;


-- Left Join
select * from customers left join orders on customers.customer_id = orders.customer_id;


-- Right Join

CREATE TABLE `orders2` (
  `order_id` int NOT NULL,
  `customer_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `order_date` date DEFAULT NULL);


select * from orders2;

insert into orders2 values(500,2000,100,5,"2026-07-25"),
(501,3001,105,5,"2026-07-25"),
(502,2001,100,3,"2026-07-25"),
(503,3002,100,4,"2026-07-25");


select * from customers right join orders2 on customers.customer_id = orders2.customer_id;

-- Self join

select * from employees;

select * from employees as pt left join employees as st on pt.manager_id = st.emp_id;

select pt.emp_id as 'Employee ID',
pt.emp_name as 'Employee Name',
st.emp_id as 'Manager ID',
st.emp_name as 'Manager Name'
from employees as pt join employees as st on pt.manager_id = st.emp_id
order by pt.emp_id; 

-- Cross Join

select * from orders cross join customers;

select * from customers left join orders2 on customers.customer_id = orders2.customer_id

union

select * from customers right join orders2 on customers.customer_id = orders2.customer_id;


-- Case Statement

select * from employees;

select
emp_id,
emp_name,
experience,
CASE
WHEN experience > 10 then 'Legend'
WHEN experience > 5 then 'Pro'
else 'Noob'
END as 'Exp_Level'
from employees;

-- class task

select * from products;

1L -> 5000voucher
50k - 1L -> 2500 voucher
10k - 50k -> 1000 voucher
less No voucher

order_id, product id, product_name, qty, unit_price, total_price, voucher_type;

select * from orders as o join products as p on o.product_id = p.product_id;

-- class task solution

select 
o.order_id,
p.product_id,
p.product_name,
o.quantity,
p.price,
(o.quantity * p.price) as Total_price,
CASE
when (o.quantity * p.price) > 100000 then "Voucher - 5000"
when (o.quantity * p.price) > 50000 then "Voucher - 2500"
when (o.quantity * p.price) > 10000 then "Voucher - 1000"
else 'No Voucher'
End as Voucher
from 
orders as o join products as p on o.product_id = p.product_id;

-- Error: using alias name of column in case statement

select 
o.order_id,
p.product_id,
p.product_name,
o.quantity,
p.price,
(o.quantity * p.price) as Total_price,
CASE
when Total_price > 100000 then "Voucher - 5000"  -- total less 1,00,000
when Total_price > 50000 then "Voucher - 2500"   -- total less 50,000
when Total_price > 10000 then "Voucher - 1000"
else 'No Voucher'
End as Voucher
from 
orders as o join products as p on o.product_id = p.product_id;

-- joining tables from multiple databases

select * from mydb.employee;

select * from mydb.employee as emp1
left join myfirstdb.employees emp2
on emp1.EmployeeID = emp2.emp_id;