"""Robot Name PEDAC:
P:
    -in: none
    -out: when robot is created it will be given a name
    -e:
        - manage robot factory settings:
            - first enters with no name and u generate a random name
            - method to reset a robot 
                (name gets wiped, 
                next time you ask it will respond with a new name)
            - names must be random; they should not follow
              a predictable sequence. 
            Random names means there is a risk of collisions. 
            our solution should not allow using the same name twice.
    -i:
        - Robot class
            - name property, returns name for instanc eof robot
            - reset() instance method, resets robots name
            -the randomly generated names seem to follow a 
                pattern of 2 uppercase alphabetic characters
                  followed by three digits.
    -?:
        - confused about the regex functions used in unittest
            -re.match:
                re.match(pattern, string, flags=0)
                If zero or more characters at the beginning of 
                string match the regular expression pattern, 
                return a corresponding Match. Return None if the string 
                does not match the pattern; note that this is different 
                from a zero-length match.

                Note that even in MULTILINE mode, re.match() will only
                match at the beginning of the string and not at 
                the beginning of each line.

                If you want to locate a match anywhere in string,
                  use search() instead (see also search() vs. match()).

                The expression’s behaviour can be modified by 
                specifying a flags
                value. Values can be any of the flags variables, combined
                 using bitwise OR (the | operator).

            -re.compile:
                re.compile(pattern, flags=0)
                Compile a regular expression pattern into a regular
                    expression object, which can be used for matching
                    using its match(), search() and other methods,
                    described below.
                The sequence:
                    prog = re.compile(pattern)
                    result = prog.match(string)
                is equivalent to result = re.match(pattern, string)
                but using re.compile() and saving the resulting 
                regular expression object for reuse is more efficient 
                when the expression will be used several times in 
                a single program.
            -random.seed:
                random.seed(a=None, version=2)
                    Initialize the random number generator.
                    If a is omitted or None, the current system
                    time is used. If randomness sources are provided
                    by the operating system, they are used instead 
                    of the system time (see the os.urandom() function
                    for details on availability).

                    If a is an int, it is used directly.
                    e seed must be one of the following types: 
                    None, int, float, str, bytes, or bytearray.


E: test_robot_name.py
D:
- random module
- @lrucache decorator fro, functools module or set of 

"""
import random

class Robot:
    LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    _in_use_names = [] # track robot names in use

    def __init__(self):
        self._name = None

    @property
    def name(self):
        if not self._name:
            while True:
                potential_name = self._generate_new_name()
                if potential_name not in Robot._in_use_names:
                    break
            self._name = potential_name
            Robot._in_use_names.append(self._name)
        return self._name
        # 2 leading upper letters + 3 digits

    def reset(self):
        Robot._in_use_names.remove(self.name)
        self._name = None


    @classmethod
    def _generate_new_name(cls):
        new_name = ""
        for _ in range(2):
            letter = random.choice(cls.LETTERS)
            new_name += letter

        for _ in range(3):
            digit = random.choice(cls.DIGITS)
            new_name += str(digit)

        return new_name