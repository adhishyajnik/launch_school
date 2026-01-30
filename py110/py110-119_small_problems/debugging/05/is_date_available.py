events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}


def is_date_available_buggy(date):
    if date in events:
        return True

    return False


print(is_date_available_buggy("2023-08-14"))  # should return False
print(is_date_available_buggy("2023-08-16"))  # should return True


"""
This is returning the opposite boolean it ought to be returning on lines 9 and 11. Swap these two.

Alternately, you can change line 8 to read if date not in events:
"""


def is_date_available(date):
    if date not in events:
        return True

    return False


print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True
