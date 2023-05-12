class Restaurant:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors):
        super().__init__(restaurant_name)
        self.flavors = flavors

    def spisok_flavors(self):
        s = self.flavors
        print(*s)

NewIceCreamStand = IceCreamStand("Морожка", ["клубничное", "ванильное", "шоколадное", "фисташковое"])
NewIceCreamStand.spisok_flavors()
print()

def z2():
    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, location, time, flavors):
            super().__init__(restaurant_name)
            self.location = location
            self.time = time
            self.flavors = flavors

        def app_flavors(self):
            flavors = self.flavors
            print("в наличии такие сорта: ", *flavors)
            flavors.append(input("введите сорт мороженого, которое хотите добавить: "))
            print("с изменениями: ", *flavors)
            print()

        def del_flavors(self):
            flavors = self.flavors
            print("в наличии такие сорта: ", *flavors)
            flavors.remove(input("введите сорт мороженого, которое хотите убрать: "))
            print("с изменениями: ", *flavors)
            print()

        def count_flavors(self):
            flavors = self.flavors
            sort1 = input("какой сорт ищем?: ")
            if sort1 in flavors:
                print(sort1, "найдено в списке")
            else:
                print(sort1, "не найдено в списке")
                print("в наличии только эти:", *flavors)
                print()

    class IceCreamVstakane(IceCreamStand):
        def __init__(self, restaurant_name, location, time, flavors):
            super().__init__(restaurant_name, location, time, flavors)

        def kol(self):
            flavors = self.flavors
            leni = len(flavors)
            print()
            print(leni, "вкусов мороженного в стакане")
            print()

    class IceCreamNaPalke(IceCreamStand):
        def __init__(self, restaurant_name, location, time, flavors):
            super().__init__(restaurant_name, location, time, flavors)

        def found(self):
            print("вы можете купить мороженое на палочке здесь:")
            print(f"название кафе-мороженного: {self.restaurant_name} адрес: {self.location} время работы : {self.time}")

    NewIceCreamStand = IceCreamStand("Морожка;", "Decabristov 52;", "открыто с 10 до 21", ["клубничное", "ванильное", "шоколадное", "фисташковое"])
    NewIceCreamStand.app_flavors()
    NewIceCreamStand.del_flavors()
    NewIceCreamStand.count_flavors()
    vs = IceCreamVstakane("Морожка;", "Decabristov 52;", "открыто с 10 до 21", ["клубничное", "ванильное", "шоколадное", "фисташковое"])
    vs.kol()
    np = IceCreamNaPalke("Морожка;", "Decabristov 52;", "открыто с 10 до 21", ["клубничное", "ванильное", "шоколадное", "фисташковое"])
    np.found()

from tkinter import *
def z3():
    class IceCreamStand:
        def __init__(self, cafe_name, flavors):
            self.cafe_name = cafe_name
            self.flavors = flavors
            root = Tk() #окно присваиваем переменной
            root['bg'] = 'white'  # Фоновый цвет
            root.title("кафе мороженое")  # Название окна
            root.geometry('500x300')
            title = Label(root, text=cafe_name, bg='white', font=40)
            title.pack()
            vid = Label(root, text="Виды мороженого:", bg='white', font=40)
            vid.pack()
            for i in flavors:
                sort = Label(root, text=i, bg='pink', font=20)
                sort.pack()
            btn = Button(root, text='Ок', bg='grey')
            btn.pack()
            root.mainloop()

    primer = IceCreamStand("МОРОЖКА", ["клубничное", "ванильное", "шоколадное", "фисташковое"])

z2()
z3()