# Principe de substitution de Liskov :
# Une sous-classe doit pouvoir être utilisée partout où la classe parent est attendue, sans casser le programme.

#Definition: Objects of a superclass should be replaceable with objects of a subclass without breaking the application.

# ❌ Violating LSP
class Bird:
    def fly(self):
        print("Flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")

class Eagle(Bird):
    def fly(self):
        print("Eagle flying")

def make_bird_fly(bird: Bird):
    bird.fly()  # This breaks with Penguin

# Usage
sparrow = Sparrow()
eagle = Eagle()
penguin = Penguin()

try:
    make_bird_fly(sparrow)  # Works fine
    make_bird_fly(penguin)  # Throws exception!
    make_bird_fly(eagle)
except Exception as e:
    print(e)
# Problems: Penguin cannot substitute Bird without breaking functionality.

from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        self.fly()

    def fly(self):
        print("Flying")

class SwimmingBird(Bird):
    def move(self):
        self.swim()

    def swim(self):
        print("Swimming")

class Sparrow(FlyingBird):
    def fly(self):
        print("Sparrow flying")

class Penguin(SwimmingBird):
    def swim(self):
        print("Penguin swimming")

def make_bird_move(bird: Bird):
    bird.move()

# Usage
sparrow = Sparrow()
penguin = Penguin()

make_bird_move(sparrow)  # Sparrow flying
make_bird_move(penguin)  # Penguin swimming


