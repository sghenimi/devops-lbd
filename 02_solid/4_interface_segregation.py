#Principe de ségrégation des interfaces :
# Il vaut mieux avoir plusieurs interfaces spécifiques que une seule interface générale.

class Worker:
    def work(self):
        pass
    def eat(self):
        pass

class Robot:
    def work(self):
        pass
    def eat(self):## ??? un robot ne mande pas
        pass

# Si un robot n’a pas besoin de eat(), il ne doit pas implémenter cette méthode.
# Créer deux interfaces :
class Workable:
    def work(self) -> None:
        ...


class Feedable:
    def eat(self) -> None:
        ...


class Restable:
    def sleep(self) -> None:
        ...


class Human(Workable, Feedable, Restable):
    def work(self) -> None:
        pass

    def eat(self) -> None:
        pass

    def sleep(self) -> None:
        pass


class Robot(Workable):
    def work(self) -> None:
        pass

