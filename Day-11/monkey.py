class Monkey:
    def __init__(self, name: str):
        self.name = name
        self.inventory  = list()
        self.operation = dict()
        self.check_divisor = int()
        self.throw_to = dict()
        self.number_of_inspections = 0