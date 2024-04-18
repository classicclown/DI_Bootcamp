class Farm:
    def __init__(self,name):
        self.name=name
        self.animals={}

    def add_animal(self,animal,number):
       
        if animal.lower() in self.animals.keys():
            self.animals[animal]+=number
        else:
            self.animals[animal]=number

    def get_info(self):
        print (f"{self.name} farm")
        for key,value in self.animals.items():
            print (f"{key} : {value}")
        print ("E-I-E-I-O")

    def get_animal_types(self):
        animal_type=[]
        for animal,count in self.animals.items():
            if count==1:
                animal_type.append(animal)
            else:
                animal_type.append(animal+'s')
        return sorted(animal_type)

    def get_short_info(self):
        print (f"{self.name} farm has the following animals:\n {self.get_animal_types()}")

        

        

    
zoo=Farm("Old McDonald")
zoo.add_animal("cow",5)
zoo.add_animal("lion",6)
#zoo.get_info()
#zoo.get_animal_types()
zoo.get_short_info()