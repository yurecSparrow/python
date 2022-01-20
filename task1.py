import time

class TrafficLight:

    def __init__(self):
        self.__color = 'red'

    def running(self):
        self.duration = {'red': 7, 'yellow': 2, 'green': 10}
        while True:
            print(f'Color: {self.__color}')
            time.sleep(self.duration[self.__color])
            if self.__color == 'red':
                self.__color = 'yellow'
            elif self.__color == 'yellow':
                self.__color = 'green'
            else:
                break
        print('End')


first = TrafficLight()
first.running()
