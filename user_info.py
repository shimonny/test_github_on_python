class Dog:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"My name is {self.name}"


class Cat(Dog):
    def __init__(self, name):
        super().__init__(name)

    def hello(self):
        print(self.greet())


cat = Cat("John")
cat.hello()
