"""
Create a Car class that meets these requirements:

    - Each Car object should have a model, model year, and color provided at
      instantiation time.
    - You should have an instance variable that keeps track of the current
      speed. Initialize it to 0 when you instantiate a new car.
    - Create instance methods that let you turn the engine on, accelerate,
      brake, and turn the engine off. Each method should display an appropriate
      message.
    - Create a method that prints a message about the car's current speed.
    - Write some code to test the methods.
"""


class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self._speed = 0
        self._engine_state = "off"
        print(f"This is a {color} {year} {model}.")

    def turn_on_engine(self):
        if self._engine_state == "off":
            self._engine_state = "on"
            print(
                f"The {self.color} {self.year} {self.model}'s engine is now on."
            )
        else:
            print(
                f"The {self.color} {self.year} {self.model} is already running."
            )

    def turn_off_engine(self):
        if self._engine_state == "on":
            if self._speed == 0:
                self._engine_state = "off"
                print(
                    f"The {self.color} {self.year} {self.model}'s engine is now off."
                )
            else:
                print("Please brake to 0 mph before turning the engine off.")
        else:
            print(f"The {self.color} {self.year} {self.model} is already off.")

    def accelerate(self, speed):
        if self._engine_state == "on":
            if isinstance(speed, int) == False:
                raise TypeError("speed must be an integer.")
            elif speed <= 0:
                raise ValueError("speed must be greater than zero.")
            elif speed <= self._speed:
                raise ValueError(
                    f"speed must be greater than {self._speed} mph."
                )
            else:
                self._speed = speed
                print(
                    f"The {self.color} {self.year} {self.model} accelerated to {speed} mph."
                )
        else:
            print(
                f"Turn on the {self.color} {self.year} {self.model}'s engine to accelerate."
            )

    def brake(self, speed):
        if self._engine_state == "on":
            if isinstance(speed, int) == False:
                raise TypeError("speed must be an integer.")
            elif speed < 0:
                raise ValueError("speed cannot be negative.")
            elif speed >= self._speed:
                raise ValueError(f"speed must be less than {self._speed} mph.")
            elif self._speed > 0:
                self._speed = speed
                print(
                    f"The {self.color} {self.year} {self.model} decelerated to {speed} mph."
                )
            elif self._speed == 0:
                print(
                    f"The {self.color} {self.year} {self.model} is already at rest."
                )
        else:
            print(
                f"Turn on the {self.color} {self.year} {self.model}'s engine to brake."
            )

    def get_speed(self):
        if self._engine_state == "off":
            print(
                f"The {self.color} {self.year} {self.model} is turned off and at rest."
            )
        elif self._speed > 0:
            print(
                f"The {self.color} {self.year} {self.model} is currently traveling at {self._speed} mph."
            )
        else:
            print(
                f"The {self.color} {self.year} {self.model} is turned on and at rest."
            )


# Tests
insight = Car("Insight", 2010, "black")
insight.turn_on_engine()
insight.accelerate(45)
insight.brake(20)
insight.get_speed()
insight.turn_off_engine()  # should ask to decelerate to 0 mph first
insight.brake(0)
insight.get_speed()
insight.turn_off_engine()

camry = Car("Camry", 2023, "silver")
camry.accelerate(20)
# camry.brake(-1)  # ValueError
camry.turn_on_engine()
camry.accelerate(-5)  # ValueError
camry.brake(0)
