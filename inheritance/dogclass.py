'''class Dog:
    speices="canine"#static variable
    def __init__(self,name,age):
        self.name=name     #instance  variable
        self.age=age

d1=Dog("Tomy","3")
print(d1.name,d1.speices)
print(Dog.speices)'''

'''class Dog:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"{self.name}it eats")
class Labs(Dog):
    def sound(self):
        print("sound woof")
class GuideDog(Labs):
    def Guide(self):
        print(f"{self.name} they can guide")
class Friendly:
    def greet(self):
        print("they are very friendly in nature")
class GoldenRetriver(Friendly,GuideDog):
    def sound(self):
       print("golden ")
lab=Labs('buddy')
print(lab.eat())
print(lab.sound())
g=GoldenRetriver("piku")
print(g.sound())
g1=GuideDog('yell')
print(g1.Guide())'''
class Dog:
    def make_sound(self):
        print("Dog")
class Cat:
    def make_sound(self):
        print("Cat")
def any_make_sound(animal):
    animal.make_sound()
any_make_sound(Dog())
any_make_sound(Cat())
