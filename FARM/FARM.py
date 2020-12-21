class Ferma(object):
    def __str__(self):
        rep = "Объект класса Ferma\n"
        rep += "Имя: " + self.name + "\n"
        rep += "Показатель настроение: " + self.mood + "\n"
        rep += "Показатель тоски:" + str(self.boredom) + "\n"
        rep += "Показатель голода:" + str(self.hunger) + "\n"
        return rep

    def __init__(self, name, hunger=0, boredom=0):
        print("Появилась на свет новая зверюшка!")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def talk(self):
        print('Привет! Меня зовут ', self.name, " . Сейчас я мое настроение: ", self.mood, "\n")
        self.__pass_time()

    def play(self, fun=5):
        fun = int(input("Во сколько игр сыграть?"))
        print("Как интересно!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def eat(self, food=5):
        food = int(input("Сколько кусочков мяса дать?"))
        print("Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()


        def __pass_time(self):
            self.hunger += 1
            self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "могло быть и лучше"
        elif 10 < unhappiness <= 15:
            m = "пора поиграть!"
        else:
            m = "плохо"
        return m


def main():
    import random
    print("Приветствую Вас на ферме!")
    ferma = []
    crit_kol = input("Введите количество животных которых вы хотите завести: ")
    for i in range(int(crit_kol)):
        crit_name = input("На ферме появилось новое животное. Как вы его назовете? ")
        crit = Ferma(crit_name, hunger=random.randint(5, 10), boredom=random.randint(5, 10))
        ferma.append(crit)

    choice = None
    while choice != "0":
        print \
            ("""
        Моя зверюшка
        0 - Выйти
        1 - Узнать о самочувствиии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        4 - Полная информация о каждой зверушке 
        """)
        choice = input("Ваш выбор: ")
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            for crit in ferma:
                crit.talk()
        elif choice == "2":
            for crit in ferma:
                crit.eat()
        elif choice == "3":
            for crit in ferma:
                crit.play()
        elif choice == "4":
            for crit in ferma:
                print(crit)
        else:
            print("Извините, в меню игры нет такого пункта ", choice)


main()

input("\n\nНажмите Enter, чтобы выйти")