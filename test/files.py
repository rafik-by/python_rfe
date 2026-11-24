# система управления умный дом
# базовый класс умные устройства: название и защищенный атрибут по умолчанию выключен метод вкл/выкл и метод возвр статус
# классы наследники освещение отопление и тд дополнительные методы и атрибуты метод + получить статус + метод на доп параметр
# класс контроля список подключенных устройств + метод добавить девайс + выключить все + получить отчет
# пользовательский ввод
from abc import ABC
from abc import abstractmethod


class smart_house(ABC):
    def __init__(self, name: str):
        self.name: str = name
        self.__status = False

    @abstractmethod
    def get_status(self):
        return self.__status

    def setStatus(self):
        k = input("Введите on/off: ")
        if k == "on":
            self.__status = True
            print("Устройство включено")
        elif k == "off":
            self.__status = False
            print("Устройство выключено")

    def get_status(self):
        return self.__status

    @abstractmethod
    def set_spec_status():
        pass

    @abstractmethod
    def get_special_atribute():
        pass

    @abstractmethod
    def printing():
        pass


class light(smart_house):
    def __init__(self, name: str, brightness: int):
        super().__init__(name)
        self.brightness: int = brightness

    def set_spec_status(self):
        self.brightness = int(input("Введите степень яркости от 0 до 5: "))
        

    def get_special_atribute(self):
        return self.brightness

    def printing(self):
        print(f"Имя: {self.name}, Статус: {"вкл" if self.get_status() else "выкл"}, яркость: {self.brightness}")


class shtory(smart_house):
    def __init__(self, name: str, open: bool):
        super().__init__(name)
        self.open = open

    def set_spec_status(self):
            self.open =  True if int(input("Введите открыты ли шторы 0 - закрыты 1 - открыты: ")) == 1 else False

    def get_special_atribute(self):
        return self.open

    def printing(self):
        print(
            f"Имя: {self.name}, Статус: {"вкл" if self.get_status() else "выкл"}, яркость: {"открыты" if self.open else "закрыты"}"
        )


class control:
    def __init__(self):
        self.list_atribute: list = []

    def add_atribute(self):
        match (int(input("выберите атрибут 1-светильник 2-шторы: "))):
            case 1:  # светильник
                self.list_atribute.append(light(input("Введите имя устройства: "),int(input("Введите степень яркости от 0 до 5: "))))
                print("Светильник по умолчанию выключен!")
            case 2:  # шторы
                self.list_atribute.append(shtory(input("Введите имя устройства: "), True if int(input("Введите открыты ли шторы 0 - закрыты 1 - открыты: "))== 1 else False ))
                print("Шторы по умолчанию закрыты!")


kalina = control()
while True:
    print(
        "1. добавить атрибут умного дома",
        "2. включить/выключить атрибут умного дома",
        "3. изменить статус специально атрибута",
        "4. вывести отчет",
        "0. выход",
        sep="\n",
    )
    k = int(input("введите ключ: "))
    match (k):
        case 1:
            kalina.add_atribute()
        case 2:
            print("выберите из списка ниже устройства которое хотите вкл или выключить: ")
            k = 0
            for object in kalina.list_atribute:
                print(k, end=". ")
                object.printing()
                k += 1
            kalina.list_atribute[int(input("Выберите по порядковому номеру устройство: "))].setStatus()

        case 3:
            print("выберите из списка ниже устройства которое хотите вкл или выключить: ")
            k = 0
            for object in kalina.list_atribute:
                print(k, end=". ")
                object.printing()
                k += 1
            kalina.list_atribute[int(input("Выберите по порядковому номеру устройство: "))].set_spec_status()
            
        case 4:
            for object in kalina.list_atribute:
                print(k, end=". ")
                object.printing()
                k += 1
        case 0:
            break
