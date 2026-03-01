import sys
from abc import ABCMeta, abstractmethod
from io import StringIO

sys.stdin = StringIO("""The Alchemist
Paulo Coelho
248""")


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display():
        pass


class MyBook(Book):
    def __init__(self, title: str, author: str, price: int) -> None:
        self.title = title
        self.author = author
        self.price = price

    def display(self) -> str:
        print("Title:", title)
        print("Author:", author)
        print("Price:", price)


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
