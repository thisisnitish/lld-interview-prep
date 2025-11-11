from utils.singleton import singleton
from models.user import User

@singleton
class UserService:
    def __init__(self):
        self.users = {} # {username, User}

    def create_user(self, username, is_admin):
        if username in self.users:
            raise ValueError(f"Username {username} already exists!!")
        
        user = User(username=username, is_admin=is_admin)
        self.users[username] = user

    def get_user(self, username):
        if username not in self.users:
            raise ValueError(f"Username {username} doesn't exists!!")
        
        return self.users[username]
    
