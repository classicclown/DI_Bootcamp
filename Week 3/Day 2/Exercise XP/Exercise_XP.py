class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1= Cat("Milo",7)
cat2=Cat("Spot",1)
cat3=Cat("Dan",5)

def find_oldest (*args):
    oldest_age=0
    oldest_cat=""
    for cat in args:
        if cat.age > oldest_age:
            oldest_cat=cat.name
            oldest_age=cat.age
    print (f"The oldest cat is {oldest_cat} who is {oldest_age} years old")


find_oldest(cat1,cat2,cat3)


#Ex. 2
class dog:

    def __init__(self,name,height):
        self.name=name
        self.height=height

    def bark(self):
        print (f"{self.name} goes woof")

    def jump(self):
        print(f"{self.name} jumps {self.height*2}cm high!")


davids_dog=dog("Rex",50)
sarahs_dog=dog("Teacup",20)
print(f"David's dog is {davids_dog.name} and is {davids_dog.height}cm tall")
davids_dog.bark()
davids_dog.jump()
print(f"David's dog is {sarahs_dog.name} and is {sarahs_dog.height}cm tall")
sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.height>davids_dog.height:
    print ("Sarahs dog is bigger")
else:
    print ("Davids dog is bigger")


#Ex.3 
class Song:

    def __init__(self,lyrics):
        self.lyrics=lyrics

    def sing_me_a_song(self):
        for lines in self.lyrics:
            print (lines)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

#Ex.4

from collections import defaultdict
class zoo:

    def __init__ (self, zoo_name):
        self.animals=[]
        self.name=zoo_name

    def add_animal(self,new_animal):
        for animal in new_animal:
            if not animal in self.animals:
                self.animals.append(animal)
        print("Animal added")

    def get_animals(self):
        for animal in self.animals:
            print (animal) 

    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print (f"{animal_sold} has been sold")
        else:
            print (f"We don't have that animal in the zoo")

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = defaultdict(list)

        for animal in sorted_animals:
            grouped_animals[animal[0].lower()].append(animal)
        print (grouped_animals)
        result = {}
        for i, (key, value) in enumerate(grouped_animals.items(), start=1):
            result[i] = value 

        return result
    
    def get_groups(self,sorted_animals):
        for key,value in sorted_animals.items():
            print(f"Group {key} has {value}")

    def ramat_gan_safari(self):
        action=input(f"You can add,get or sell an animal. You can also sort the animals and get their groupings.")
        if action =="add":
            animals=input("Enter the animal/s you want to add to the zoo")
            new_zoo.add_animal(animals)

        elif action =="get":
            animals=input("Enter the animal you want to get from the zoo")
            print(new_zoo.get_animal(animals))

        elif action=="sell":
            animals=input("Enter the animal you want to get from the zoo")
            new_zoo.sell_animal(animals)

        elif action=="sort":
            print(new_zoo.sort_animals())
        elif action=="get groups":
            new_zoo.get_groups(new_zoo.sort_animals())




# Example usage:
new_zoo = zoo("Ryans zoo")
new_zoo.ramat_gan_safari()
#new_zoo.add_animal(["ape","bear","cat","emu","cougar","baboon"])





