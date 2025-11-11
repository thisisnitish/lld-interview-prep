Design an in-memory sql database. Functionalities required were -

- It should be possible to create or delete tables in a database.
- A table definition comprises columns which have types. They can also have constraints
- The supported column types are string and int.
- The string type can have a maximum length of 20 characters.
- The int type can have a minimum value of -1024 and a maximum value of 1024.
- Support for mandatory fields (tagging a column as required)
- It should be possible to insert records in a table.
- It should be possible to print all records in a table.

Follow-ups -

- How can we add filter records whose column values match a given value?
- What design pattern would be used?

========
SQL DB
Table
    Columns = [col1, col2, col3....]

Operations
create table
    - constraints with columsn and all etc.
delete table
insert data/record to table
print data/record from table

======
Entities
Column
    - column interface
    - concerete classes, integer, string
    - attriubtes - > name, type, required, validate() [validate whether it is following constraint or not]
    - Factory Pattern
Table
    - Column (has-a)
    - attributes - name, records, columns
    - functionalities - insert_record(), print_all()
SQLDB
    - Table (has-a)
    - functionalities - create_table(), insert() => calls insert() from table class, delete_table()
    - Singleton Pattern

==========
Follow Up
We will have filteration strategy for different filter methods
For example => Equal Filter = if col valu is same, filter it