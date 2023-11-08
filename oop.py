# object-oriented programming

class PartyAnimal:
    x = 0

    def __init__(self):
        print("I am constructed")

    # constructor
    def party(self):
        self.x = self.x + 1
        print("So far ", self.x)
    
    # destructor
    def __del__(self):
        print("I am destructed", self.x)

# create instance and assign it
an = PartyAnimal()

print("Type ", type(an))
print("Dir ", dir(an))

an.party()
an.party()
an.party()

an = 42
print("an contains ", an)