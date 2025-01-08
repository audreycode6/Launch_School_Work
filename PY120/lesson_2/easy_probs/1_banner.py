'''Complete this class so that the test cases shown below 
work as intended. You are free to add any methods or 
instance variables you need. However, methods prefixed with 
an underscore are intended for internal use and
should not be called externally.
'''
'''FE:
Modify this class so that the __init__ method  optionally 
lets you specify a fixed banner width when the Banner object
is created. The message in the banner should be centered
within the banner of that width. Decide for yourself how yo
u want to handle widths that are either too narrow or too wide.
'''

class Banner:
    def __init__(self, message, banner_width=None):
        self.message = message

        # validate banner_width
        if banner_width is not None:
            if not isinstance(banner_width, int):
                raise ValueError("banner_width must be an integer.")
            
        self._banner_length = (len(message) if 
                                    (banner_width == None) or (banner_width < len(message)) 
                                    else banner_width)
        

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return f'| {' ' * self._banner_length} |'

    def _horizontal_rule(self):
        return f'+-{'-'  * self._banner_length}-+'

    def _message_line(self):
        return f"| {self.message.center(self._banner_length)} |"

# Comments show expected output
banner = Banner('To boldly go where no one has gone before.')
print(banner)

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+
test_banner = Banner('To boldly go where no one has gone before.', 53)
print(test_banner._banner_length) #30
print(test_banner)