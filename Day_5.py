


def read_lin(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()
            
count = 0
for lines in read_lin("text.txt"):
    print(lines)
    print(count)
    count+=1
    
    
'''
with open( file_path , 'mode') as f:
    f.read()
    f.write()
    f.append()
mode = read (r), write(w), readwrite (r+)
writeRead(w+) , append(a)('/n sometext')

'''


class Animal:
    def __init__(self, name):
        self.name = name 
    
    def speak(self):
        return f"{self.name} makes a sound "
    
class Dog(Animal):
    def __init__(self , name , bread):
        super().__init__(name)
        self.bread = bread
    
    def speak(self):
        return super().speak() + " ----- Howwwooooooo !!!"
        
    def show_bread(self):
        return f"{self.bread} "
    
    
dog = Dog("King" , "Splits")
print(dog.speak())
print(dog.show_bread())


# with open("text.txt" , "r" ) as file 
'''

Global Interpreter LOCK (GLI) in python 
It is a mutex that protects access to python objects 
and ensures that one thread bython byte code at a time 

multi processing to achive multithreading

'''



# class method and static method

class Dog:
    species = "German"
    
    def __init__(self, name):
        self.name = name 
    
    @classmethod
    def set_species(cls , species_name):
        cls.species = species_name
        

Dog.set_species("Sheperered")
print(Dog.species)


class MathUtils:
    @staticmethod
    def add(x,y):
        return x + y

print(MathUtils.add(45,99))


# mutli threading in python is achive by multi ptocessing 

import threading 

def my_method():
    for i in range (10000,1000000):
        print(i)
        

thread = threading.Thread(target = my_method)
thread.start()















    
    
    
