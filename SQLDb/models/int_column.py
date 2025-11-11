from models.column import Column

class IntColumn(Column):
    def __init__(self, name, required=False):
        self.name = name
        self.required = required

    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.name} must be an integer")
        if value < -1024 or value > 1024:
            raise ValueError(f"{self.name} must be in the range of -1024 to 1024")
