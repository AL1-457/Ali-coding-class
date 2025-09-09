class Dog:
    # Class Variable
    animal = 'dog'

    # The init method or costructor
    def __init__(self, bred, colour):

    # Instance Variable
        self.breed = bred
        self.color = colour

# Objects of Dog class
Rodger = Dog("pug", "brown")
Buzo = Dog("Bulldog", "blsck")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('color: ',Rodger.color)

print()
print('Buzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('color: ', Buzo.color)