import uuid

class Group:
    def __init__(self, name, members):
        self.id = str(uuid.uuid4())
        self.name = name
        self.members = members

    def get_id(self):
        return self.id

    def get_members(self):
        return self.members.copy()