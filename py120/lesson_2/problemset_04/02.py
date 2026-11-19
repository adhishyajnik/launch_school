"""
We've added a few more methods for our Dog class.

Create a new class called Cat, which can do everything a dog can, except fetch.
Assume the methods do the exact same thing. Hint: don't copy and paste any
methods from Dog into Cat; come up with a class hierarchy instead.
"""


class Pet:
    def speak():
        pass

    def sleep(self):
        return "sleeping!"

    def run(self):
        return "running!"

    def jump(self):
        return "jumping!"


class Cat(Pet):
    def speak(self):
        return "meow!"


class Dog(Pet):
    def speak(self):
        return "bark!"

    def fetch(self):
        return "fetching!"


class Bulldog(Dog):
    def sleep(self):
        return "snoring!"


kitty = Cat()
print(kitty)
print(kitty.speak())  # bark!
print(kitty.sleep())  # sleeping!
print(kitty.run())  # running!
print(kitty.jump())  # jumping
# print(kitty.fetch())  # AttributeError

fido = Dog()
print(fido)
print(fido.speak())  # bark!
print(fido.sleep())  # sleeping!
print(fido.run())  # running!
print(fido.jump())  # jumping
print(fido.fetch())  # fetching!

buster = Bulldog()
print(buster)
print(buster.speak())  # bark!
print(buster.sleep())  # snoring!
print(buster.run())  # running!
print(buster.jump())  # jumping
print(buster.fetch())  # fetching!
