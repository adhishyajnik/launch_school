"""
Add a method to the Car class that lets you spray paint the car a specific
color. Don't use a setter method for this. Instead, create a method whose name
accurately describes what it does. Don't forget to test your code.
"""


class Car:
    def __init__(self, year, color, model):
        self._year = year
        self._model = model
        self.color = color.lower()
        self._full_name = f"{self.color} {self.year} {self.model}"
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
        if isinstance(new_color, str) == False:
            raise TypeError("new_color must be a string.")

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

    def spray_paint(self, new_color):
        if isinstance(new_color, str) == False:
            raise TypeError("new_color must be a string.")

        print(
            f"The {self.full_name} has been spray-painted {new_color.lower()}."
        )
        self.color = new_color.lower()

    @property
    def full_name(self):
        return f"{self.color} {self.year} {self.model}"

    def turn_on(self):
        print(f"The {self.full_name} is now on.")

    def turn_off(self):
        self.speed = 0
        print(f"The {self.full_name} is now off.")

    def accelerate(self, amount):
        if isinstance(amount, int) == False:
            raise TypeError("amount must be an integer.")
        if amount <= 0:
            raise ValueError("amount must be positive.")

        self._speed += amount
        print(f"The {self.full_name} accelerated {amount} mph.")

    def brake(self, amount):
        if isinstance(amount, int) == False:
            raise TypeError("amount must be an integer.")
        if amount <= 0:
            raise ValueError("amount must be positive.")

        amount = min(self._speed, amount)
        self._speed = self._speed - amount
        print(f"The {self.full_name} braked {amount} mph.")


# Tests
insight = Car(2010, "black", "Insight")  # This car is a black 2010 Insight.
print()
print(f"Car color: {insight.color}")  # Car color: black
print()
insight.spray_paint("gold")  # The car has been spray-painted gold.
print()
print(f"Car color: {insight.color}")  # Car color: gold
print()
insight.accelerate(25)  # The gold 2010 Insight accelerated 25 mph.
print()
insight.turn_off()  # The gold 2010 Insight is now off.
