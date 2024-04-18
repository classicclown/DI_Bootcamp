import Dogs

class PetDog(Dogs):
    def __init__(self,trained):
        self.trained=False

    def train(self):
        print(self.Dogs.bark())


dog1=PetDog()
dog1.train()