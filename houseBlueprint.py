# This script will have the blueprint of a house to explain encapsulation


class House:
    def __init__(self, size, color, num_of_windows, num_of_doors, backyard):
        self.size = size
        self.color = color
        self.num_of_windows = num_of_windows
        self.num_of_doors = num_of_doors
        self.backyard = backyard

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def get_windows(self):
        return self.num_of_windows

    def get_doors(self):
        return self.num_of_doors

    def get_bool_backyard(self):
        return self.backyard

    def do_We_Need_garage(self):
        return ""
