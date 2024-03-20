# Python - Object-relational mapping

This project involves linking Python with databases using two different methods: directly using the MySQLdb module and using SQLAlchemy, an Object Relational Mapper (ORM). The first part focuses on executing SQL queries using MySQLdb, while the second part abstracts the storage using SQLAlchemy.

## Requirements

- Ubuntu 20.04 LTS
- Python 3.8.5
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x
- pycodestyle 2.7.*
- All files must end with a new line
- The first line of all files must be `#!/usr/bin/python3`
- README.md file is mandatory
- Modules must have documentation
- Classes must have documentation
- Functions must have documentation
- All files must be executable

## Tasks Examples

### Task 0: Get all states

Write a script that lists all states from the database hbtn_0e_0_usa:

- Script takes 3 arguments: MySQL username, password, and database name
- Connects to MySQL server on localhost at port 3306
- Results must be sorted in ascending order by states.id

### Task 9: Contains `a`

Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa:

- Script takes 3 arguments: MySQL username, password, and database name
- Connects to MySQL server on localhost at port 3306
- Results must be sorted in ascending order by states.id

