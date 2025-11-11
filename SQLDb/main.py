"""
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
"""

from sql_db import SqlDb
from models.filter_strategy import EqualFilterStrategy

def run():
    sqlInstance = SqlDb()

    columns = [
        {"type": "string", "name": "Name", "required": True},
        {"type": "integer", "name": "Age", "required": True},
        {"type": "integer", "name": "Roll No", "required": False},
    ]

    sqlInstance.create_tables("Table1", columns=columns)

    record1 = {"Name": "Nitish", "Age": 26, "Roll No": 123}
    record2 = {"Name": "Akshay","Age": 23, "Roll No": 345}
    sqlInstance.insert_table("Table1", record=record1)
    sqlInstance.insert_table("Table1", record=record2)

    sqlInstance.print_all("Table1")

    filter_records = sqlInstance.filter_records("Table1", EqualFilterStrategy(), "Age", 23)
    print("Filtered Records...")
    print(filter_records)

    # sqlInstance.delete_table("Table1")
    
    # sqlInstance.print_all("Table1")

if __name__ == "__main__":
    run()