# object-oriented programming

class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z):
      self.name = z
      print(self.name, " constructed")

    # constructor
    def party(self):
      self.x = self.x + 1
      print(self.name, " party count ", self.x)
    
    # destructor
    def __del__(self):
        print("I am destructed", self.x)

# create instance and assign it
s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("John")
j.party()
s.party()