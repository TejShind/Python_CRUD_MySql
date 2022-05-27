show databases;
create database payroll_service;
use payroll_service;
CREATE TABLE employee_payroll(
ID INT PRIMARY KEY,
NAME VARCHAR(30) NOT NULL,
SALARY DOUBLE NOT NULL, AGE INT NOT NULL);
SHOW TABLES;
DESC employee_payroll;
SELECT * FROM payroll_service.employee_payroll;
INSERT INTO employee_payroll(ID,NAME,SALARY)
values(1,'Tejaswini','94000');
DESC payroll_service;
SELECT * FROM payroll_service.employee_payroll;
SELECT * FROM   employee_payroll WHERE NAME='Komal';
ALTER TABLE employee_payroll add GENDER char(1);
UPDATE employee_payroll SET GENDER='F' WHERE ID in(1) ;
UPDATE employee_payroll SET GENDER='F' WHERE ID in(3) ;

INSERT INTO employee_payroll(ID,NAME,SALARY)
VALUES(2,'AKASH','50000');
INSERT INTO employee_payroll(ID,NAME,SALARY)
VALUES(3,'KOMAL','70000');
INSERT INTO employee_payroll(ID,NAME,SALARY)
VALUES(4,'PRISHA','90000');
SELECT * FROM   employee_payroll WHERE NAME='KOMAL';
DELETE FROM employee_payroll WHERE NAME='AKASH';


