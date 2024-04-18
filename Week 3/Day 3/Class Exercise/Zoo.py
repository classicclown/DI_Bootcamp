class Animal:
    def __init__(self,name,age,health,hunger,happiness):
        self.name=name
        self.age=age
        self.health=health
        self.hunger=hunger
        self.happiness=happiness

    def speak(self):
        print("Animals make noise!")

    def eat(self):
        if self.hunger >0:
            self.hunger-=1
            self.happiness+=1

class Lion (Animal):

    def __init__(self,name,age,health,hunger,happiness):
        super().__init__(name,age,health,hunger,happiness)

    def speak(self):
        print ("ROOAAARR")


    def play(self,animal):
        if animal =="Monkey":
              self.happiness+=5
        else:
            self.happiness+=2
        
    def eat(self):
        if self.hunger>0:
            self.hunger-=2
            self.happiness+=3
        else:
             print(f"{self.name} is full")

class Elephant (Animal):

    def __init__(self,name,age,health,hunger,happiness):
        super().__init__(name,age,health,hunger,happiness)

    def speak(self):
        print ("PPPFFFFTTTTTTT")

    def play(self,animal):
        if animal =="Lion":
              self.happiness+=5
        else:
            self.happiness+=2

    def eat(self):
        if self.hunger>0:
            self.hunger-=3
            self.happiness+=3
        else:
             print(f"{self.name} is full")

class Monkey (Animal):

    def __init__(self,name,age,health,hunger,happiness):
        super().__init__(name,age,health,hunger,happiness)

    def speak(self):
        print ("OOH OOHH AHHH AHHH")

    def play(self,animal):
        if animal =="Elephant":
              self.happiness+=5
        else:
            self.happiness+=2

    def eat(self):
        if self.hunger>0:
            self.hunger-=4
            self.happiness+=2
        else:
             print(f"{self.name} is full")

class ZooKeeper:
    pass
