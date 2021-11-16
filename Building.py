class Building:
    def __init__(self, min_floor: int, max_floor: int, elevators: list):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.elevators = elevators

    def number_of_elevators(self):
        return len(self.elevators)

    def get_elevator(self, id: int):
        return self.elevators[id]
