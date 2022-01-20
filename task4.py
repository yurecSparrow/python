class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехал')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        if direction.lower() == 'left':
            print(f'{self.name} повернул налево')
        elif direction.lower() == 'right':
            print(f'{self.name} повернул направо')
        else:
            print('Не правильное направление, можно только left и right')

    def show_speed(self):
        print(f'{self.name} едет со скоростью: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} едет со скоростью: {self.speed}')
        if self.speed > 60:
            print(f'Превышение максимальной скорости для машин в городе!')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'{self.name} едет со скоростью: {self.speed}')
        if self.speed > 40:
            print(f'Превышение максимальной скорости для спецтехники!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


john = TownCar(70, 'black', 'John', False)
fred = WorkCar(50, 'yellow', 'Fred', False)
michael = SportCar(200, 'red', 'Michael', False)
tenpeni = PoliceCar(10, 'Black & White', 'Tenpeni', True)

john.show_speed()
john.speed = 60
john.show_speed()
fred.show_speed()
michael.show_speed()
michael.turn('left')
john.turn('right')
tenpeni.stop()
tenpeni.go()
