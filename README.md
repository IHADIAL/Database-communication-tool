# Database-communication-tool
A python program that connects to a database and allows SELECT, INSERT, UPDATE, and DELETE queries for a student database.

# Files
app.py: This is the program/application file that holds the whole communication part.
tables.sql: This is the SQL query file with the base test database skeleton with each table and value types.
info.sql: This is the SQL query file that holds base test information to insert into the database.

# Requirements
Install PostgreSQL and set it up. Install python via terminal and then install psycopg2-binary.

# Setup
In PostgreSQL create a database, name it, and run the tables.sql file and info.sql file in the query tool connected to the database. Now edit the app.py file at line 2 change database="name" to the name you set for the database, user="postgres" to your PostgreSQL username, and change the password="password" to what your PostgreSQL password is. Now you should be able to run the program in the terminal cd to the folder with the app.py and type "py app.py" and then use the program as needed.

# What does what
1. Prints all student info in the database row by row.
2. Insert a new student by information into the database.
3. Change a students email.
4. Remove a student from the database.
5. Exit program.

# Video instructions
[*link*](https://www.youtube.com/watch?v=fcUGAS5IyHw)
