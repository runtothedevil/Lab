class Animal:
    name=''
    def Eat(self):
        print("Ам-Ням");

    def setName(self, newName):
        self.name=newName

    def getName(self):
        return self.name

    def makeNoize(self):
        print(self.name+ 'Говорит РРРррр')

    def __init__(self, newName):
        self.name=newName
        print('Родилось животное ', self.name)

Cat=Animal('Пушок')
print(Cat.getName())

Cat.setName('Пуша')
print(Cat.getName())

Cat.Eat()
Cat.makeNoize()