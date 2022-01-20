class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name =name
        self.surname = surname
        self.position = position
        self._income = {'wage':wage, 'bonus':bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name.title() + ' ' + self.surname.title()

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


manager = Position('Michael', 'Jackson', 'manager', 15000, 10000)
print(f'Full name: {manager.get_full_name()}')
print(f'Total income: {manager.get_total_income()}')
