class House:
    def __init__(self, name, number):
        self.name = name
        self.number = int(number)


    def go_to(self,new_floor):
        int(new_floor)
        if new_floor > self.number or new_floor <1:
            print(f'Такого этажа в "{self.name}" не существует!')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number


    def __str__(self):
        return (f'Название:{self.name},кол-во этажей:{self.number}')



home_1 = House('ЖК Эльбрус', 10)
home_2 = House('ЖК Акция', 20)
print(home_1)
print(home_2)
print(len(home_1))
print(len(home_2))