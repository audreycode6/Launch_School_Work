'''Write the classes and methods that will
be necessary to make this code run, 
and log the following output:
'''

'''STEPS:
create a Pet class that takes in animaltype and name to init
and method that returns f string of animal info: animaltpye and name'''

'''create Owner class that takes in name instance and 
creates pets list instance at init
create instance methods: 
	-add_pet: updates pets list to add pet to it
	- number_of_pets returns len of pets list , ie # of pets for owner
	- print_pets pet info for each pet in pets: (animal_type and name)
'''

'''create Shelter class, creates owners dict when init
create instance methods:
	- adopt: 
			take in owner and pet 
			call add_pet method and: 
				-add_pet if owner already in owners dict; 
				else add owner to owners dict
		-print_adoptions:
			-loop through owners dict, print f string of 
			ownername adopted following pets
			- call print_pets() method for owner
'''

class Pet:
    def __init__(self, animal_type, name):
        self.animal_type = animal_type
        self.name = name

    def info(self):
        return f"a {self.animal_type} named {self.name}"

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def number_of_pets(self):
        return len(self.pets)
    
    def print_pets(self):
        for pet in self.pets:
            print(pet.info())

class Shelter:
    def __init__(self):
        self.owners = {}

    def adopt(self, owner, pet):
        owner.add_pet(pet)
        if owner not in self.owners:
            self.owners[owner.name] = owner
        
    def print_adoptions(self):
        for name, owner in self.owners.items():
            print(f"{name} has adopted the following pets")
            owner.print_pets()
            print("")


cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")

'''Output:
P Hanson has adopted the following pets:
a cat named Cocoa
a cat named Cheddar
a bearded dragon named Darwin

B Holmes has adopted the following pets:
a dog named Molly
a parakeet named Sweetie Pie
a dog named Kennedy
a fish named Chester

P Hanson has 3 adopted pets.
B Holmes has 4 adopted pets.
'''