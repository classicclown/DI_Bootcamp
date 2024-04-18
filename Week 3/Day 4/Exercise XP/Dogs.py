class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing (self,sounds):
        return f'{sounds}'
    
all_cats = [Bengal("Ben",1),Chartreux("Fluffy",4),Siamese("Winston",5)]
sara_pets = Pets(all_cats)
sara_pets.walk()
    
class Dogs:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight

    def bark(self):
        return (f'{self.name} is barking')
    def run_speed(self):
        return (self.weight/self.age*10)
    def fight(self,other_dog):
        dog_a = self.run_speed()*self.weight
        dog_b=other_dog.run_speed()*other_dog.weight
        if dog_a>dog_b:
            return f'{self.name} won the fight'
        else:
            return f'{other_dog.name} won the fight'
        
dog1 = Dogs("Ruff",2,20)
dog2=Dogs("Mucho",4,10)
dog3=Dogs("Spot",6,40)

print(dog1.fight(dog3))

