# services/user_service.py
from models.user import User


class UserService:
    def __init__(self):
        self.users = []

    def add_user(self, user: User) -> None:
        self.users.append(user)
        print("User added successfully!")

    def get_user_by_username(self, username: str) -> User:
        for user in self.users:
            if user.username == username:
                return user
        return None
