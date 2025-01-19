class Vehicle():
    def __init__(self, owner:str, __model:str, __engine_power:int, color:str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.color = color

    def get_model(self):
        return print(f'Модель: {self.__model}')
    
    def get_horsepower(self):
        return print(f'Мощность двигателя: {self.__engine_power}')
    
    def get_color(self):
        return print(f'Цвет: {self.color}')
    
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print (self.get_color(self))
        return print(f'Владелец: {self.owner}')

class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5
    __COLOR_VARIANTS = ['red','white','black','grey']

    def print_info(self):
        Sedan.get_model(self)
        Sedan.get_horsepower(self)
        Sedan.get_color(self)
        return print(f'Владелец: {self.owner}')
    
    def set_color(self, new_color:str):
        self.new_color = new_color
        for items in Sedan.__COLOR_VARIANTS:
            if items == self.new_color:
                self.color = self.new_color
                return print(f'Цвет: {self.color}')  
        return print(f'Нельзя сменить цвет на {self.new_color} ')
    
    def owner(self,new_owner:str):
        self.owner = new_owner
        return print(f'Новый владелец:{self.owner}')
    
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('black')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()






