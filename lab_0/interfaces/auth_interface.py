# interfaces/auth_interface.py
from abc import ABC, abstractmethod


class AuthInterface(ABC):
    @abstractmethod
    def login(self, username: str, password: str) -> bool:
        pass

    @abstractmethod
    def logout(self) -> None:
        pass
