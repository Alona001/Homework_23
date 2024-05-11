import random

from Car import Car

cars = []

models = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
colors = ["blue", "green", "yellow", "violet"]
economies = [4, 6, 10]

for car in range(1, 11):
    random_model = random.choice(models)
    random_color = random.choice(colors)
    random_economy = random.choice(economies)

    new_car = Car(random_economy, random_color, random_model)
    cars.append(new_car)

for car in cars:
    car.drive(200)
    car.fuel_up()
    car.drive(100)

max_fuel_car = Car(0, "", "", 0, 0)

for car in cars:
    if max_fuel_car.get_fuel() < car.get_fuel():
        max_fuel_car = car

print(max_fuel_car.print_car())

