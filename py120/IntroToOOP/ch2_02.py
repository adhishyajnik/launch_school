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
        self._color = color
        self._speed = 0
        self._engine_state = "off"
        print(
            f"This {self.__class__.__name__.lower()} is a {color} {year} {model}."
        )

    @property
    def engine_state(self):
        return self._engine_state

    @engine_state.setter
    def engine_state(self, new_state):
        if new_state.lower() in ["on", "off"]:
            if self._speed == 0:
                self._engine_state = new_state.lower()
            else:
                print(
                    "Please brake or set speed to 0 mph before turning the engine off."
                )
        else:
            raise ValueError("new_state must be on or off, case-insensitive.")

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_value):
        if self.engine_state == "on":
            if isinstance(new_value, int) == False:
                raise TypeError("speed must be an integer.")
            elif new_value <= 0:
                raise ValueError("speed must be greater than zero.")
            else:
                self._speed = new_value
        else:
            print(
                f"Turn on the {self.color} {self.year} {self.model}'s engine to set its speed."
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
        if new_color.lower() in Car.AVAIL_COLORS:
            self._color = new_color.lower()
        else:
            raise ValueError(
                f"new_color must be {', '.join(Car.AVAIL_COLORS[:-2]) + ', or ' + Car.AVAIL_COLORS[-1]}, case-insensitive."
            )

    def accelerate(self, amount):
        if self._engine_state == "on":
            if isinstance(amount, int) == False:
                raise TypeError("amount must be an integer.")
            elif amount <= 0:
                raise ValueError("amount must be positive.")
            else:
                self._speed += amount
                print(
                    f"The {self.color} {self.year} {self.model} accelerated to {amount} mph."
                )
        else:
            print(
                f"Turn on the {self.color} {self.year} {self.model}'s engine to accelerate."
            )

    def brake(self, amount):
        if self._engine_state == "on":
            if isinstance(amount, int) == False:
                raise TypeError("amount must be an integer.")
            if amount <= 0:
                raise ValueError("amount must be positive.")
            else:
                amount = min(self._speed, amount)
                self._speed = self._speed - amount
                print(
                    f"The {self.color} {self.year} {self.model} braked {amount} mph."
                )
        else:
            print(
                f"Turn on the {self.color} {self.year} {self.model}'s engine to brake."
            )


insight = Car("Insight", 2010, "black")  # This car is a black 2010 Insight.
print()
print(insight.year)  # 2010
print(insight.model)  # Insight
print()
print(insight.color)  # black
insight.color = "Blue"
print(insight.color)  # blue
print()
print(insight.speed)  # 0
insight.speed = 50  # turn on engine first
print(insight.speed)  # 0
print()
print(insight.engine_state)  # off
insight.engine_state = "ON"
print(insight.engine_state)  # on
print()
print(insight.speed)  # 0
insight.speed = 50
print(insight.speed)  # 50
print()
insight.engine_state = "off"  # decelerate to 0 mph first
print()
insight.accelerate(15)  # The blue 2010 Insight accelerated to 65 mph.
print(insight.speed)  # 65
insight.brake(30)  # The blue 2010 Insight braked to 35 mph.
print(insight.speed)  # 35
insight.brake(100)  # The blue 2010 Insight braked to 0 mph.
print(insight.speed)  # 0
print()
insight.engine_state = "off"
print(insight.engine_state)  # off
print()
print()

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
