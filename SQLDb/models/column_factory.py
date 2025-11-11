from models.string_column import StringColumn
from models.int_column import IntColumn

class ColumnFactory:
    @staticmethod
    def create_column(col_type, name, required):
        if col_type == "integer":
            return IntColumn(name=name, required=required)
        elif col_type == "string":
            return StringColumn(name=name, required=required)
        return ValueError(f"Unsupported column type, {col_type}")