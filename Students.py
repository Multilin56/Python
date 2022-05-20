class Student:
    def __init__(self, name = "Ivan", groupNumber = "10A", age = 18):
        self.__name = name
        self.__groupNumber = groupNumber
        self.__age = age

    def get_name(self):
        return self.__name


    def get_groupNumber(self):
        return self.__groupNumber

    def set_groupNumber(self, groupNumber):
        self.__groupNumber = groupNumber


    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
    

    def get(self):
        return [self.__name, self.__groupNumber, self.__age]
    
    def set(self, name = "Ivan", groupNumber = "10A", age = 18):
        self.__name = name
        self.__groupNumber = groupNumber
        self.__age = age

S1 = Student()
S2 = Student()
S3 = Student()
S4 = Student()
S5 = Student()
print('Спрака: если ввести команду "help" выведится список всех команд')
b = True
while b:
    print("1. " + str(S1.get()))
    print("2. " + str(S2.get()))
    print("3. " + str(S3.get()))
    print("4. " + str(S4.get()))
    print("5. " + str(S5.get()))
    a = input("Введите команду: ")
    if a == "help":
        print('''
    1."изменить" что-бы изменить обьект
    2."очистить" что-бы очистить обьект
    3."выйти" чтобы закончить программу
        ''')
    if a == "изменить":
        Numder = input("Введите номер обьекта: ")
        a1 = input("Введите имя: ")
        a2 = input("Введите номер группы: ")
        a3 = input("Введите возраст: ")
        if Numder == "1":
            S1.set(a1, a2, a3)
        elif Numder == "2":
            S2.set(a1, a2, a3)
        elif Numder == "3":
            S3.set(a1, a2, a3)
        elif Numder == "4":
            S4.set(a1, a2, a3)
        elif Numder == "5":
            S5.set(a1, a2, a3)
        else:
            print("Неверная команда")

    elif a == "очистить":
        Numder = input("Введите номер обьекта: ")
        a1 = ""
        a2 = ""
        a3 = ""
        if Numder == "1":
            S1.set(a1, a2, a3)
        elif Numder == "2":
            S2.set(a1, a2, a3)
        elif Numder == "3":
            S3.set(a1, a2, a3)
        elif Numder == "4":
            S4.set(a1, a2, a3)
        elif Numder == "5":
            S5.set(a1, a2, a3)
        else:
            print("Неверная команда")

    elif a == "выйти":
        b = False
    
    elif a != "help":
        print("Неверная команда")