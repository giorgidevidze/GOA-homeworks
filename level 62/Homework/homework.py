# #  Task 2

# Python-ში _ და __ prefix-ები (წინა ხაზები) გამოიყენება ველი ან მეთოდის სახელებში და ისინი განსაზღვრავენ მათი გამოყენების წესი და მიდგომები. განსხვავება ძირითადად დაკავშირებულია წვდომის კონვენციებთან და მონაცემთა ინკაფსულაციასთან:


#  Task 3
# Level 1
class MyClass:
    def __init__(self):
        self._level1_variable = 42  

    def get_level1_variable(self):
        return self._level1_variable  


obj = MyClass()
print(obj.get_level1_variable())  


print(obj._level1_variable) 


# Level 2
class MyClass:
    def __init__(self):
        self.__level2_variable = 42  

    def get_level2_variable(self):
        return self.__level2_variable  


obj = MyClass()
print(obj.get_level2_variable())  

print(obj._MyClass__level2_variable)  


#  Task 4

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"{self.name} makes a sound.")

class Prey(Animal):
    def __init__(self, name, species, habitat):
        super().__init__(name, species)  
        self.habitat = habitat

    def flee(self):
        print(f"{self.name} is fleeing from danger!")

class Predator(Animal):
    def __init__(self, name, species, hunting_skill):
        super().__init__(name, species)  
        self.hunting_skill = hunting_skill

    def hunt(self):
        print(f"{self.name} is hunting with a skill level of {self.hunting_skill}!")

class Rabbit(Prey):
    def __init__(self, name, habitat):
        super().__init__(name, "Rabbit", habitat)  

    def make_sound(self):
        print(f"{self.name} says: Squeak!")

class Hawk(Predator):
    def __init__(self, name, hunting_skill):
        super().__init__(name, "Hawk", hunting_skill)  

    def make_sound(self):
        print(f"{self.name} says: Screech!")


rabbit = Rabbit("Bunny", "forest")
hawk = Hawk("Eagle", "expert")

print(f"{rabbit.name} is a {rabbit.species} living in the {rabbit.habitat}.")
rabbit.make_sound()
rabbit.flee()

print(f"{hawk.name} is a {hawk.species} with {hawk.hunting_skill} hunting skills.")
hawk.make_sound()
hawk.hunt()
