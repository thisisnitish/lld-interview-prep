from models.column import Column

class StringColumn(Column):
    def __init__(self, name, required=False):
        self.name = name
        self.required = required

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.name} must be a string")
        if len(value) > 20:
            raise ValueError(f"{self.name} must be less than 20 characters")
