# main.py
from services.user_service import UserService
from services.auth_service import AuthService
from models.user import User

# Initialize services
user_service = UserService()
auth_service = AuthService()

# Add a user
new_user = User("user", "password", "user@example.com")
user_service.add_user(new_user)

# Authenticate user
username = "user"
password = "password"

user = user_service.get_user_by_username(username)

if user:
    if auth_service.login(user.username, password):
        print(f"Welcome, {user.username}!")
    else:
        print(f"Authentication failed for {user.username}")
else:
    print("User not found.")
