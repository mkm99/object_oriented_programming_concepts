from houseBlueprint import House


class SummerHouse(House):
    def __init__(self, size, color, num_of_windows, num_of_doors, backyard):
        super().__init__(size, color, num_of_windows, num_of_doors, backyard)

    def do_We_Need_garage(self):
        return "Yes, we need a garage!"


#capeMay = SummerHouse("Small", "Red", 3, 5, False)
#print("Garage?::", capeMay.do_We_Need_garage())


class WinterHouse(House):
    def __init__(self, size, color, num_of_windows, num_of_doors, backyard):
        super().__init__(size, color, num_of_windows, num_of_doors, backyard)

    def do_We_Need_garage(self):
        return "No, we do not need a garage!"


#london = WinterHouse("Large", "Blue and Red", 18, 16, True)

#print("Doors", london.num_of_windows)
#london.get_garage()
#print("Garage?: ", london.do_We_Need_garage())
