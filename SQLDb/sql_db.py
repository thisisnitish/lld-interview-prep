from models.column_factory import ColumnFactory
from models.table import Table

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
        
    return get_instance

@singleton
class SqlDb:
    def __init__(self):
        self.tables = {}

    def create_tables(self, table_name, columns):
        if table_name in self.tables:
            raise ValueError(f"{table_name} is already exists")
        
        self.tables[table_name] = Table(table_name, columns=columns)

    def insert_table(self, table_name, record):
        self.tables[table_name].insert_record(record)

    def filter_records(self, table_name, filter_strategy, column, value):
        return self.tables[table_name].filter_records(filter_strategy, column, value)

    def print_all(self, table_name):
        if table_name not in self.tables:
            raise ValueError(f"{table_name} Table doesn't exits")
        
        print(f"Information for {table_name}")
        self.tables[table_name].print_all()

    def delete_table(self, table_name):
        del self.tables[table_name]