class Dog:
    def __init__(self, name, avility):
        self.name = name
        self.abil = avility

    def greet(self):
        return f"My name is {self.name}, I have {self.abil} skill!"


class Cat(Dog):
    def __init__(self, name, ability):
        super().__init__(name, ability)

    def hello(self):
        print(self.greet())


cat = Cat("Taro", "fly")
cat.hello()


def hello():
    return print("hello")


print("^-^")
print('---------')
hello()
print("aaaaa"
