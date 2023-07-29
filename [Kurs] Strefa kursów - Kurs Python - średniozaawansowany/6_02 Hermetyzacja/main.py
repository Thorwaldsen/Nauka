class Car:
    def __init__(self, liquid=0):
        self.tank = liquid

    def set_tank(self, liquid, unit="L"):
        if unit.upper() == "L":
            self.tank = liquid
        elif unit.upper() == "G":
            self.tank = liquid / 0.26416
        else:
            self.tank = liquid

    def get_tank(self, unit="L"):
        if unit.upper() == "L":
            return self.tank
        elif unit.upper() == "G":
            return self.tank * 0.26416
        else:
            return self.tank
