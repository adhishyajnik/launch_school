"""
Going back to your solution to exercise 1, refactor the code to replace any
methods that can be converted to static methods. Once you have done that, ask
yourself whether the conversion to a static method makes sense.
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

    @staticmethod
    def average_mpg(gallons, miles):
        mpg = miles // gallons
        print(f"This car drives {mpg} miles per gallon.")

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

    @staticmethod
    def turn_on():
        print("The car is now on.")

    def turn_off(self):
        self.speed = 0
        print("The car is now off.")

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
insight.average_mpg(9, 350)  # This car drives 38 miles per gallon.
print()
Car.average_mpg(10, 350)  # This car drives 35 miles per gallon.
print()
insight.turn_off()
print()
Car.turn_on()
