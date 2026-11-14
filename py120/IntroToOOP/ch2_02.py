"""
Using decorators, add getter and setter methods to your Car class so you can
view and change the color of your car. You should also add getter methods that
let you view but not modify the car's model and year. Don't forget to write
some tests.
"""


class Car:
    AVAIL_COLORS = (
        "black",
        "gray",
        "silver",
        "white",
        "blue",
        "red",
        "yellow",
        "green",
    )

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self.color = color
        self.speed = 0
        print(
            f"This {self.__class__.__name__.lower()} is a {color} {year} {model}."
        )

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        if new_color.lower() not in Car.AVAIL_COLORS:
            raise ValueError(
                f"new_color must be {', '.join(Car.AVAIL_COLORS[:-2]) + ', or ' + Car.AVAIL_COLORS[-1]}, case-insensitive."
            )

        self._color = new_color.lower()

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_value):
        if isinstance(new_value, int) == False:
            raise TypeError("speed must be an integer.")
        if new_value < 0:
            raise ValueError("speed must be greater than zero.")

        self._speed = new_value

    def turn_on(self):
        print(f"The {self.color} {self.year} {self.model} is now on.")

    def turn_off(self):
        self.speed = 0
        print(f"The {self.color} {self.year} {self.model} is now off.")

    def accelerate(self, amount):
        if isinstance(amount, int) == False:
            raise TypeError("amount must be an integer.")
        if amount <= 0:
            raise ValueError("amount must be positive.")

        self._speed += amount
        print(
            f"The {self.color} {self.year} {self.model} accelerated {amount} mph."
        )

    def brake(self, amount):
        if isinstance(amount, int) == False:
            raise TypeError("amount must be an integer.")
        if amount <= 0:
            raise ValueError("amount must be positive.")

        amount = min(self._speed, amount)
        self._speed = self._speed - amount
        print(
            f"The {self.color} {self.year} {self.model} braked {amount} mph."
        )


# Tests
insight = Car("Insight", 2010, "black")  # This car is a black 2010 Insight.
print()
print(f"The car's year is {insight.year}.")  # The car's year is 2010.
print(f"The car's model is a {insight.model}")  # The car's model is a Insight.
print()
print(f"The car is {insight.color}.")  # The car is black.
insight.color = "Blue"
print(f"The car is {insight.color}.")  # The car is blue.
print()
print(f"The car is traveling at {insight.speed} mph.")
# The car is traveling at 0 mph.
print()
insight.turn_on()  # The blue 2010 Insight is now on.
print()
insight.speed = 50
print(f"The car is traveling at {insight.speed} mph.")
# The car is traveling at 50 mph.
print()
insight.accelerate(15)  # The blue 2010 Insight accelerated 15 mph.
print(f"The car is traveling at {insight.speed} mph.")
# The car is traveling at 65 mph.
print()
insight.brake(30)  # The blue 2010 Insight braked 30 mph.
print(f"The car is traveling at {insight.speed} mph.")
# The car is traveling at 35 mph.
print()
insight.brake(100)  # The blue 2010 Insight braked 35 mph.
print(f"The car is traveling at {insight.speed} mph.")
# The car is traveling at 0 mph.
print()
insight.speed = 25
print(f"The car is traveling at {insight.speed} mph.")
# The car is traveling at 25 mph.
print()
insight.turn_off()  # The blue 2010 Insight is now off.
print()
print(f"The car is traveling at {insight.speed} mph.")
# The car is traveling at 0 mph.
print()
print()

# tests below are primarily to ensure that the correct errors are raised
"""
camry = Car("Camry", 2023, "silver")  # This car is a silver 2023 Camry.
print()
camry.engine_state = "warm-up"  # TypeError

camry.engine_state = "on"

camry.color = "aquamarine"  # ValueError


camry.speed = "faster"  # TypeError
camry.speed = 15.5  # TypeError
camry.speed = -5  # ValueError
camry.speed = 0  # ValueError

camry.accelerate("faster")  # TypeError
camry.accelerate(15.5)  # TypeError
camry.accelerate(-5)  # ValueError
camry.accelerate(0)  # ValueError

camry.brake("faster")  # TypeError
camry.brake(15.5)  # TypeError
camry.brake(-5)  # ValueError
camry.brake(0)  # ValueError
"""
