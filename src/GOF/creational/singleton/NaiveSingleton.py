class NaiveSingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]

class NaiveSingleton(metaclass=NaiveSingletonMeta):
    def go_with_signleton(self):
        print("Hello from go_with_signleton")


if __name__ == "__main__":
    # The client code.

    s1 = NaiveSingleton()
    s2 = NaiveSingleton()

    print(f"First Singleton works as : {id(s1)}")
    print(f"Second Singleton works as : {id(s2)}")