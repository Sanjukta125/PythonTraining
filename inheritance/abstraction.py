from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def species(self):
        pass
class Dog(Animal):
    def species(self):
        return "DOG"
dog=Dog()
print(dog.species())