class Car:

    def __init__(self, economy: int, color: str, model: str, mileage: int = 0, fuel: int = 100):
        self._economy = economy
        self._color = color
        self._model = model
        self._mileage = mileage
        self._fuel = fuel

    def get_economy(self):
        return self._economy

    def set_economy(self, new_economy):
        self._economy = new_economy

    def get_mileage(self):
        return self._mileage

    def set_mileage(self, new_mileage):
        self._mileage = new_mileage

    def get_fuel(self):
        return self._fuel

    def set_fuel(self, new_count_of_fuel):
        self._fuel = new_count_of_fuel

    def drive(self, distance: int):
        if self.distance_left() < distance:
            return Exception("Not enough fuel")
        fuel_to_drive = distance / self._economy
        new_count_of_fuel = self.get_fuel() - fuel_to_drive
        self.set_fuel(new_count_of_fuel)
        new_mileage = self.get_mileage() + distance
        self.set_mileage(new_mileage)

    def distance_left(self):
        return self._fuel * self._economy

    def fuel_up(self):
        new_count_of_fuel = self.get_fuel() + 20
        self.set_fuel(new_count_of_fuel)

    def print_car(self):
        print(f"Economy: {self._economy}")
        print(f"Color: {self._color}")
        print(f"Model: {self._model}")
        print(f"Mileage: {self._mileage}")
        print(f"Fuel: {self._fuel}")