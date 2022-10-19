class Mammal:
    def walk(self):
        print('Walking...')
        

class Dog(Mammal):
    def bark(self):
        print('Barking...')


class Cat(Mammal):
    def meow(self):
        print('Meowing...')
        
cat1 = Cat()
cat1.walk()
cat1.meow()