from Dogs import Dogs
import random
class PetDog(Dogs):
    def __init__(self,name, age,weight,trained):
        super().__init__(name,age,weight)
        self.trained=False

    def train(self):
        print (self.bark())
        self.trained=True

    def play(*args):
        print(f"{args} all play together")

    def do_a_trick(self):
        random_num=random.randint(0,4)
        if self.trained:
            if random_num==1:
                print(f"{self.name} does a barrel roll")
            elif random_num==2:
                print(f"{self.name} stands on his back legs")
            elif random_num==4:
                print(f"{self.name} shakes your hand")
            else:
                print(f"{self.name} plays dead")

# dog1=PetDog("Spot",3,45,True)
# dog1.train()
# dog1.do_a_trick()

class Family:

    def __init__(self,members,last_name):
        self.members=members
        self.last_name=last_name

    def born(self,**kwargs):
        self.members.append(kwargs)
        print("Congrats on your new child")

    def is_18(self,name):
        for people in self.members:
            if name==people['name'] and people['age']>=18:
                return True
            else:
                return False
        
    def family_presentation(self):
        print (self.last_name)
        family=""
        for people in self.members:
            family+=str(people)+"\n"
        return family


klein = Family([
        {'name':'Michael','age':35,'gender':'Male','is_child':False},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False}
    ],"Klein")


# print(klein.is_18("Slice"))
# klein.born(name='Adam', age=2, gender='Male', is_child=True)
# klein.family_presentation()

class The_Incredibles(Family):

    def __init__(self,members,last_name):
        super().__init__(members,last_name)
       

    def use_power(self,name):
        if self.is_18(name):
            print(self.power)
        else:
            raise Exception ('Too Young') 
        
    def incredible_presentation(self):
        print("Here is our powerful family")
        #print (self.last_name)
        print (self.family_presentation())
    

family1 = The_Incredibles(    [
        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
    ], "Incredibles")

family1.incredible_presentation()
family1.born(name="Baby Jack",age=0,gender='male',is_child=True,power="Unknown",incredible_name='JackJack')
family1.incredible_presentation()