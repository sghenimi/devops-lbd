# Principe de substitution de Liskov :
# Une sous-classe doit pouvoir être utilisée partout où la classe parent est attendue, sans casser le programme.

class Bird:
    def fly(self):
        pass

class Duck(Bird):
    def fly(self):
        print("Je vole")

class Penguin(Bird):
    def fly(self):
        raise Exception("Je ne vole pas !")
# ❌ Ici, Penguin viole LSP, car on ne peut pas l’utiliser comme un Bird sans problème.
# ✅ Solution : séparer les oiseaux volants et non-volants.

from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def eat(self) -> None:
        ...


class FlyingBird(Bird):
    @abstractmethod
    def fly(self) -> None:
        ...


class Sparrow(FlyingBird):
    def eat(self) -> None:
        pass

    def fly(self) -> None:
        pass


class Penguin(Bird):
    def eat(self) -> None:
        pass

