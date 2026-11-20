"""
Write the classes and methods that will be necessary to make this code run, and
log the output in the expected outcomde docstring below.
"""


class Pet:
    def __init__(self, species, name):
        self._species = species
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def species(self):
        return self._species


class Owner:
    def __init__(self, name):
        self._name = name
        self._pets = []

    @property
    def name(self):
        return self._name

    @property
    def pets(self):
        return self._pets

    def number_of_pets(self):
        return len(self.pets)

    def adopt(self, pet):
        self._pets.append(pet)

    def print_pets(self):
        print(
            f"{self.name} has the following pets: {
                ', '.join([pet.name for pet in self.pets])
            }."
        )


class Shelter:
    def __init__(self):
        self._adoptions = dict()

    def adopt(self, adopter, pet):
        if adopter not in self._adoptions:
            self._adoptions[adopter] = []
        self._adoptions[adopter].append(pet)
        adopter.adopt(pet)

    def print_adoptions(self):
        for adopter in self._adoptions:
            print(f"{adopter.name} has adopted the following pets:")
            for pet in self._adoptions[adopter]:
                print(f"a {pet.species} named {pet.name}")
            print()


cocoa = Pet("cat", "Cocoa")
cheddar = Pet("cat", "Cheddar")
darwin = Pet("bearded dragon", "Darwin")
kennedy = Pet("dog", "Kennedy")
sweetie = Pet("parakeet", "Sweetie Pie")
molly = Pet("dog", "Molly")
chester = Pet("fish", "Chester")

phanson = Owner("P Hanson")
bholmes = Owner("B Holmes")

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} adopted pets.")

phanson.print_pets()
bholmes.print_pets()

"""
EXPECTED OUTPUT:
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
"""
