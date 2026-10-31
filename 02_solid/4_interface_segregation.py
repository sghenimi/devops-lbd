from abc import ABC, abstractmethod
#Principe de ségrégation des interfaces :
# Il vaut mieux avoir plusieurs interfaces spécifiques que une seule interface générale.

class Worker:
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Human(Worker):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

    def sleep(self):
        print("Human sleeping")

class Robot(Worker):
    def work(self):
        print("Robot working")

    def eat(self):
        # Robots don't eat!
        raise NotImplementedError("Robots don't eat")

    def sleep(self):
        # Robots don't sleep!
        raise NotImplementedError("Robots don't sleep")

# Problems: Robot is forced to implement methods it doesn't need.
# Créer deux interfaces :
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass

class Human(Workable, Eatable, Sleepable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

    def sleep(self):
        print("Human sleeping")

class Robot(Workable):
    def work(self):
        print("Robot working")

# Usage
def manage_worker(worker: Workable):
    worker.work()

def feed_worker(worker: Eatable):
    worker.eat()

human = Human()
robot = Robot()

manage_worker(human)  # Works
manage_worker(robot)  # Works

feed_worker(human)    # Works
feed_worker(robot)  # Won't compile - Robot doesn't implement Eatable