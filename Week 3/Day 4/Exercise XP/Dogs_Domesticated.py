import Dogs

class PetDog(Dogs):
    def __init__(self,name, age,weight,trained):
        super().__init__(name,age,weight)
        self.trained=False

    def train(self):
        print(f'{self.name}')


dog1=PetDog()
dog1.train()