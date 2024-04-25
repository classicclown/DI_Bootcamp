from collections import deque
class Human:

    def __init__(self, id_number,name,age,priority,blood_type):
        self.id_num=id_number
        self.name=name
        self.age=age
        self.priority=priority
        self.blood_type=blood_type
        self.family=[]

    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)


class Queue:

    def __init__(self):
        self.humans=[]

    def add_person(self,person):
        if person.age>60:
            self.humans.insert(0,person)
        else:
            self.humans.append(person)
    
    def find_in_queue(self,person):
       return self.humans.index(person.name)
    
    def swap (self,person1,person2):
        self.humans.insert(self.humans.index(person1),person2)
        self.humans.insert(self.humans.index(person2),person1)

    def get_next(self):
        if len(self.humans)>0:
            next_person = self.humans[0].name
            self.humans.pop(0)
        else:
            next_person = None
        return next_person
    
    def get_next_blood_type(self,blood_type):
        if len(self.humans)>0:
            for human in self.humans:
                if human.blood_type == blood_type:
                    person= human.name
                    self.humans.remove(human)
                    break
        else:
            return None
        return (person)
                

    def sort_by_age(self):
        priority=deque()
        old=deque()
        young=deque()

        for human in self.humans:
            if human.priority:
                priority.append(human)
            elif human.age>=50:
                old.append(human)
            else:
                young.append(human)

        for i in range(len(old)-1):
            for j in range (0, len(old)-i-1):
                if old[j].age < old[j+1].age:
                    old[j+1],old[j]=old[j],old[j+1]
        
        for i in range(len(young)-1):
            for j in range (0, len(young)-i-1):
                if young[j].age < young[j+1].age:
                    young[j+1],young[j]=young[j],young[j+1]

        sorted_list = priority+old+young
        for people in sorted_list:
            print (people.name)
                    
    def rearrange_queue(self):
        for i in range (len(self.humans)-1):
            for j in range (len(self.humans)-i-1):
                if self.humans[j].family == self.humans[j+1].family:
                    if j+2<len(self.humans):
                        self.humans[j+1],self.humans[j+2]=self.humans[j+2],self.humans[j+1]
                    else:
                        self.humans[j+1],self.humans[0]=self.humans[0],self.humans[j+1]
    
    def print (self):
        for people in self.humans:
            print (people.name)

    

       
if __name__=="__main__":
        human1 = Human(1, "John", 30, False, "A")
        human2 = Human(2, "Alice", 25, True, "B")
        human3 = Human(3, "Bob", 35, False, "O")
        human4 = Human(4, "Emily", 28, True, "AB")
        human5 = Human(5, "Michael", 40, False, "A")
        human6 = Human(6, "Sarah", 22, True, "O")
        human7 = Human(7, "David", 45, False, "B")
        human8 = Human(8, "Emma", 29, True, "A")
        human9 = Human(9, "James", 33, False, "O")
        human10 = Human(10, "Olivia", 27, True, "AB")
        human1.add_family_member(human2)
        human1.add_family_member(human3)
        human8.add_family_member(human9)
        human9.add_family_member(human10)



        queue1 = Queue()
        queue1.add_person(human1)
        queue1.add_person(human2)
        queue1.add_person(human3)
        queue1.add_person(human4)
        queue1.add_person(human5)
        queue1.add_person(human6)
        queue1.add_person(human7)
        queue1.add_person(human8)
        queue1.add_person(human9)
        queue1.add_person(human10)
        queue1.print()
        print("")
        queue1.rearrange_queue()
        print("")
        queue1.print()
       




        

       



            

        






            
            

    