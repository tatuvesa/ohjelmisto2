class Building:
    def __init__(self, address, floors):
        self.floors = floors
        self.address = address


class Apartment(Building):
    def __init__(self, unit_number, floor, address, num_floors):
        super().__init__(address, num_floors)
        self.unit_number = unit_number
        self.floor = floor

    def print_info(self):
        print(f" Address: {self.address} floor {self.floor}/{self.floors} unit: {self.unit_number} ")


apartment = Apartment(23, 6, "asd street 123", 7)
apartment.print_info()
