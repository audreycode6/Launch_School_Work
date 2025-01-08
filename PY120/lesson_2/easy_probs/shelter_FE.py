class Pet:
    def __init__(self, animal_type, name):
        self.animal_type = animal_type
        self.name = name

    def info(self):
        return f"a {self.animal_type} named {self.name}"

class Owner:
    def __init__(self, name='NotAdopted'): # NEW default param
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
        if owner.name not in self.owners:
            self.owners[owner.name] = owner

    def print_adoptions(self):
        for name, owner in self.owners.items():
            if owner == not_adopted:
                print(f'''The Animal Shelter has the following unadopted pets:''')
            else:
                print(f'''{name} has adopted the following pets:''')
            owner.print_pets()
            print("")

# NEW
asta = Pet('dog', 'Asta')
laddie = Pet('dog', 'Laddie')
fluffy = Pet('cat', 'Fluffy')
kat = Pet('cat', 'Kat')
ben = Pet('cat', 'Ben')
chatterbox = Pet('parakeet', 'Chatterbox')
bluebell = Pet('parakeet', 'Bluebell')

# OLD
cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')


phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')
not_adopted = Owner() #NEW

shelter = Shelter()
shelter.adopt(not_adopted, asta)
shelter.adopt(not_adopted, laddie)
shelter.adopt(not_adopted, fluffy)
shelter.adopt(not_adopted, kat)
shelter.adopt(not_adopted, ben)
shelter.adopt(not_adopted, chatterbox)
shelter.adopt(not_adopted, bluebell)

# OLD
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

#NEW
print(f"The Animal Shelter has {not_adopted.number_of_pets()} unadopted pets.")

'''TODO:
-add my own name as owner object + pets 
- create a shelter object: 'Animal Shelter'
-create instancd method to add dogs to a shelter object without being adopted
    - count # of pets w/out an owner
    - maybve change adopt method and set default to NotAdopted if empty
- add pets(unadopted): 'dog: asta, dog: laddie, 
    cat:fluffy, cat: Kat, cat: Ben
    parakeet: Chatterbox, parakeet:Bluebell'''


'''Add your own name and pets to this project.
Suppose the shelter has a number of not-yet-adopted pets, 
and wants to manage them through this same system. 
Thus, you should be able to add the following output
to the example output shown above:

The Animal Shelter has the following unadopted pets:
a dog named Asta
a dog named Laddie
a cat named Fluffy
a cat named Kat
a cat named Ben
a parakeet named Chatterbox
a parakeet named Bluebell
   ...

P Hanson has 3 adopted pets.
B Holmes has 4 adopted pets.
The Animal shelter has 7 unadopted pets.

Can you make these updates to your solution?
 Did you need to change your class system at all? 
 Were you able to make all of your changes without 
 modifying the existing interface?'''
