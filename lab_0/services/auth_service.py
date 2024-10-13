# services/auth_service.py
from interfaces.auth_interface import AuthInterface


class AuthService(AuthInterface):
    def __init__(self):
        self.logged_in = False

    def login(self, username: str, password: str) -> bool:
        # Example authentication logic
        if username == "user" and password == "password":
            self.logged_in = True
            print("User authenticated!")
            return True
        print("Authentication failed.")
        return False

    def logout(self) -> None:
        self.logged_in = False
        print("User logged out.")
