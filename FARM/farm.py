class loshad(object):
    def __init__(self, name,hunger = 0,boredom = 0):
        print("Появилась лошадь")
        self.name= name
        self.hunger=hunger
        self.boredom=boredom
    def __pass_time(self):
        self.hunger +=1
        self.boredom +=1

    def talk(self):
        print("Меня зовут", self.name,"\n","У меня настроение",self.feel)
        self.__pass_time()
    def __yeah(self):
        print("yeah")
    def neyeah(self):
        print("neyeah")
        self.__yeah()
    def eat(self,food = 4,boredom = 4):
        print("Thanks")
        self.boredom -= food
        if self.boredom < 0:
            self.boredom = 0
        self.hunger-=food
        if self.hunger < 0:
            self.hunger=0
        self.__pass_time()
    def play(self,fun =4):
        print("OMG!")
        self.__pass_time()
    def golos(self):
        print("Фырк-фырк")
        self.__pass_time()
    @property
    def feel(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness <5:
            m="Все супер!"
        elif 5<= unhappiness <=10:
            m="Нормально"
        elif 10<=unhappiness<15:
            m="Бывало и лучше"
        else:
            m="Ужасно"
        return m

class pig(object):
    def __init__(self, name,hunger = 0,boredom = 0):
        print("Появилась свинья")
        self.name= name
        self.hunger=hunger
        self.boredom=boredom
    def __pass_time(self):
        self.hunger +=1
        self.boredom +=1

    def talk(self):
        print("Меня зовут", self.name,"\n","У меня настроение",self.feel)
        self.__pass_time()
    def __yeah(self):
        print("yeah")
    def neyeah(self):
        print("neyeah")
        self.__yeah()
    def eat(self,food = 4,boredom = 4):
        print("Thanks")
        self.boredom -= food
        if self.boredom < 0:
            self.boredom = 0
        self.hunger-=food
        if self.hunger < 0:
            self.hunger=0
        self.__pass_time()
    def play(self,fun =4):
        print("OMG!")
        self.__pass_time()
    def golos(self):
        print("Хрю-хрю")
        self.__pass_time()
    @property
    def feel(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness <5:
            m="Все супер!"
        elif 5<= unhappiness <=10:
            m="Нормально"
        elif 10<=unhappiness<15:
            m="Бывало и лучше"
        else:
            m="Ужасно"
        return m

class cow(object):
    def __init__(self, name,hunger = 0,boredom = 0):
        print("Появилась корова")
        self.name= name
        self.hunger=hunger
        self.boredom=boredom
    def __pass_time(self):
        self.hunger +=1
        self.boredom +=1

    def talk(self):
        print("Меня зовут", self.name,"\n","У меня настроение",self.feel)
        self.__pass_time()
    def __yeah(self):
        print("yeah")
    def neyeah(self):
        print("neyeah")
        self.__yeah()
    def eat(self,food = 4,boredom = 4):
        print("Thanks")
        self.boredom -= food
        if self.boredom < 0:
            self.boredom = 0
        self.hunger-=food
        if self.hunger < 0:
            self.hunger=0
        self.__pass_time()
    def play(self,fun =4):
        print("OMG!")
        self.__pass_time()
    def golos(self):
        print("Муу")
        self.__pass_time()
    @property
    def feel(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness <5:
            m="Все супер!"
        elif 5<= unhappiness <=10:
            m="Нормально"
        elif 10<=unhappiness<15:
            m="Бывало и лучше"
        else:
            m="Ужасно"
        return m

def main():
    f = None
    while f != 0:
        x = int(input("Напишите цифру чтобы выбрать животного: 1 - корова,2 - лошадь, 3 - свинья "))
        if x == 1:
            crit_name = input("Дай имя корове \n")
            crit1 = cow(crit_name)
        elif x == 2:
            crit_name = input("Дай имя лошади \n ")
            crit1 = loshad(crit_name)
        elif x == 3:
            crit_name = input("Имя свинье \n ")
            crit1 = pig(crit_name)
        else:
            f = 0
        if f !=0:
            zapusk(crit1)
def zapusk(u):
    choice = None
    while choice != 0:
        print("""
          Моя зверюшка
          0 - Выйти
          1 - узнать о самочувствии зверюшки
          2 - покормить зверюшку
          3 - поиграть со зверюшкой
          4 - попросить голос  
     """   )
        choice=int(input("Выбирайте "))
        if choice==0:
            print("Пока")
        elif choice ==1:
            u.talk()
        elif choice == 2:
            u.eat()
        elif choice==3:
            u.play()
        elif choice==5:
            print(u.name)
            print(u.boredom)
            print(u.hunger)
        elif choice == 4:
            u.golos()
        else:
            print("Такого пункта нет")
main()

input("Enter,чтобы выйти")