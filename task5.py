class Stationery:
    title = 'прибор'
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Синяя черта от ручки')

class Pencil(Stationery):
    def draw(self):
        print('Толстая черта от карандаша')

class Handle(Stationery):
    def draw(self):
        print('Глубокий и пахнущий след от маркера')

common = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()

common.draw()
pen.draw()
pencil.draw()
pen.draw()
handle.draw()
