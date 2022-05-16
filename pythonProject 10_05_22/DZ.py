# ООП. Принципы ООП. Abstraction (абстракция), Encapsulation (инкапсуляция),
# Polymorphism (полиморфизм), Inheritance (наследование)

class Animal:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'Animal name: {self.name}, age: {self.age}'

    @staticmethod
    def sound():
        print("Good sound")

class Dog(Animal):

    @staticmethod
    def sound():
        print("Woof Woof")


class Cat(Animal):

    @staticmethod
    def sound():
        print("Meow meow")
class Parrot(Animal):
    pass

animal = Animal("Mr Bean", 12)
cat = Cat("Vasy", 3)
dog = Dog("Shelbi", 2)
parrot = Parrot("Kesha", 1)

animal.sound()
cat.sound()
dog.sound()
parrot.sound()

print(animal)
print(cat)
print(dog)
print(parrot)

# Abstraction (абстракция)
class Animal:
    name: str
    age: int
    #....
    legs: int
    flying: bool
    color: str

# Encapsulation (инкапсуляция)
class User:
    username: str
    __password: str
    _email:str

    def __init__(self, nick: str, pwd: str, email: str):
        self.username=nick
        self.__password=pwd
        self._email = email
    def change_pass(self, pwd:str):
        self.__password=pwd
user = User("polyatodim", "dima1234", "polyatodim@tut.by")
user.change_pass("1234dima")
print(user.username)
# print(user.__password)

class MailUser(User):

    def p(self):
        print(self._email)
        print(self.__password)

user = MailUser("polyatodim", "dima1234", "polyatodim@tut.by")
user.p()

