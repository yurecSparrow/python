class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def weight(self, density=25, thickness=5):
        return int(self._width * self._length * density * thickness  / 1000)


central = Road(20, 5000)
print(f'Mass of asphalt: {central.weight()}t')
