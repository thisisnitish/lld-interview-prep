from models.column_factory import ColumnFactory

class Table:
    def __init__(self, name, columns):
        self.name = name
        self.records = []
        self.columns = {col["name"]: ColumnFactory.create_column(col["type"], col["name"], col["required"]) for col in columns}
        # print('cc: ', self.columns)

    def insert_record(self, record):
        # check for the validity for the columns before inserting
        for col_name, col in self.columns.items():
            if col.required and col_name not in record:
                raise ValueError(f"{col_name} is required!")
        
        validated_record = {}
        for col_name, value in record.items():
            if col_name not in self.columns:
                raise ValueError(f"Unknown column: {col_name} !!")
            
            col = self.columns[col_name] # get the column and validate it
            col.validate(value=value)
            validated_record[col_name] = value
        
        self.records.append(validated_record)

    def filter_records(self, filter_strategy, column, value):
        return filter_strategy.apply_filter(self.records, column, value)

    def print_all(self):
        for record in self.records:
            print(record)

    

    