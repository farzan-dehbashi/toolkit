### Create database:
```
CREATE DATABASE <name>;
```
### Show databases:
```
SHOW DATABASES;
```
### Drop database:
```
DROP DATABASE <name>
```
### Switch between databases:
```
USE <name>
```
### pwd the database:
```
SELECT database();
```
### Tables 
#### Data types
int
varchar(<number of chars>)
#### Creat a table
```
CREATE TABLE <table name>
(
<column name> <data type>, <column name2> <data type2>
);
```
To specify a default:
```
CREATE TABLE <table name>
(
<column name> VARCHAR(50) DEFAULT <default value>,
);
```
#### Show tables
```
SHOW tables;
```
##### Show columns of the table
```
SHOW COLUMNS FROM <table name>;
```
#### Delete a table
```
DROP TABLE <table name>
```
### Insert
```
INSERT INTO <table name> (<column name>, <column name2>)
VALUES(<val1>, <val2>);
```
Note that if you wanna have a VARCHAR value, put it in ''.
#### Multiple inserts
```
INSERT INTO <table name> (column_name1, column_name2)
VALUES(<val1>, <val2>) , (<val3>,<val4>);
```
### SQL Warnings
Show warnings
```
SHOW WARNINGS;
```

