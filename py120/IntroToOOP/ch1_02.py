"""
Given an instance of a Foo object, show two ways to print I am a
Foo object without hardcoding the word Foo.
"""


class Foo:
    pass


new_foo_obj = Foo()

print(f"I am a {new_foo_obj.__class__.__name__} object")
print(f"I am a {type(new_foo_obj).__name__} object")
