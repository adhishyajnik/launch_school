"""
What is the method resolution order and why is it important?

Method resolution order (MRO) is the order in which Python looks for a called
method, beginning by searching the called class for the method, followed by
searching each class in its inheritance list (including mix-ins) and their
superclasses from left to right in the inheritance list, until it either finds
the method and calls it -- which terminates the search -- or until it finally
searches the object class and can't find the called method, in which case it
raises an AttributeError.
"""
