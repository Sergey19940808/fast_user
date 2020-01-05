"""
This module for declaration a interface App
"""
from abc import ABCMeta, abstractmethod


class IApp(metaclass=ABCMeta):
    @abstractmethod
    def create_app(self) -> None:
        """
        Abstract method for creating instance of app
        """
        pass