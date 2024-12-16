'''Create a Car class that makes the following code work as indicated:'''

class Car:

    def __init__(self, car_id, year, color):
        self.car_id = car_id
        self.year = year
        self.color = color

    def __str__(self):
        return  f"{self.color.capitalize()} {self.year} {self.car_id}"

    def __repr__(self):
        color = repr(self.color)
        car_id = repr(self.car_id)
        year = repr(self.year)
        return f"Car({car_id}, {year}, {color})"


vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')