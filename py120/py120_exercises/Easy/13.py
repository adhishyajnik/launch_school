"""
Write a class such that the following code prints the results indicated by the
comments:
"""


class Transform:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def lowercase(data):
        return data.lower()

    def uppercase(self):
        return self.data.upper()


my_data = Transform("abc")
print(my_data.uppercase())  # ABC
print(Transform.lowercase("XYZ"))  # xyz
