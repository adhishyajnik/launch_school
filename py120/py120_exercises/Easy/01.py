"""
Complete this class so that the test cases shown below work as intended. You are
free to add any methods or instance variables you need. However, methods
prefixed with an underscore are intended for internal use and should not be
called externally.

You may assume that the input will always fit in your terminal window.

Further Exploration:
Modify this class so that the __init__ method optionally
lets you specify a fixed banner width when the Banner object is created. The
message in the banner should be centered within the banner of that width. Decide
for yourself how you want to handle widths that are either too narrow or too
wide.
"""


class Banner:
    def __init__(self, message, width=0):
        self._message = message
        if not isinstance(width, int):
            width = 0
        if width >= len(message) + 2:
            self._width = width
        else:
            self._width = len(message) + 2

    @property
    def message(self):
        return self._message

    def __str__(self):
        return "\n".join(
            [
                self._horizontal_rule(),
                self._empty_line(),
                self._message_line(),
                self._empty_line(),
                self._horizontal_rule(),
            ]
        )

    def _empty_line(self):
        return f"|{' ' * self._width}|"
        # return f"| {' ' * len(self.message)} |"

    def _horizontal_rule(self):
        return f"+{'-' * self._width}+"
        # return f"+-{'-' * len(self.message)}-+"

    def _message_line(self):
        return f"|{self.message.center(self._width, ' ')}|"
        # return f"| {self.message} |"


# Comments show expected output

banner = Banner("To boldly go where no one has gone before.")
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner("")
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+

# width longer than message
c_banner = Banner("To boldly go where no one has gone before.", 55)
print(c_banner)

# width exactly as long as message
c_banner = Banner("To boldly go where no one has gone before.", 42)
print(c_banner)

# width exactly as long as message + 2
c_banner = Banner("To boldly go where no one has gone before.", 44)
print(c_banner)

# width longer than message + 2
c_banner = Banner("To boldly go where no one has gone before.", 46)
print(c_banner)

# no width provided
c_banner = Banner("To boldly go where no one has gone before.")
print(c_banner)

# width shorter than message
c_banner = Banner("To boldly go where no one has gone before.", 8)
print(c_banner)

# width is negative
c_banner = Banner("To boldly go where no one has gone before.", -25)
print(c_banner)

# width not an integer
c_banner = Banner("To boldly go where no one has gone before.", "long")
print(c_banner)

# width a float
c_banner = Banner("To boldly go where no one has gone before.", 55.0)
print(c_banner)
