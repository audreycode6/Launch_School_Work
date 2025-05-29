"""Diamond PEDAC:
P:
    -in: string --> a letter (capital letter)
    -out: returns letter in a diamond shape, 
        with supplied letter at widest point
    -e:
        -"A" only returns "A"
        - all rows except 1st and last have 2 identical letters
        - horizontally and vertically symetrical
        - diamond has square shape, width == height
        - letters form a diamond shap
        -top hald has letters in ascending order
        -bottom half has letter in descending order
        - the four corners (contianined spaces) are triangles
    -i:
    - Diamond class:
        -make_diamond method, takes in string of letter to build 
        -even letter == diamond length 
        - odd letter == 
    -?:

E: test_diamond.py
D:
    - need a list/str for chars and their index 
    can be used to access its place(?)
"""

class Diamond():
    SPACING = " "
    LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    @classmethod
    def make_diamond(cls, letter):
        # ensure letter is uppercased
        if not letter.isupper():
            letter = letter.upper()

        if letter == "A":
            return "A\n"

        # build half of diamond
        diamond_half = cls._make_diamond_half(letter)

        # build final diamond into 1 list
        diamond_top = diamond_half[:-1]
        middle = diamond_half[-1]
        diamond_bottom = diamond_top[::-1]
        lst_diamond = diamond_top + [middle] + diamond_bottom

        return "\n".join(lst_diamond) + "\n"

    @classmethod
    def _make_diamond_half(cls, letter):
        diamond_half = []
        space_len = cls.LETTERS.index(letter)

        # all strings have same length:
        #   double the starting space length & + 1 for top letter
        total_str_len = (space_len * 2) + 1

        for char in cls.LETTERS:
            if space_len < 0:
                break

            outter_spacing = cls.SPACING * space_len
            if char == "A": # first line in diamond has only 1 letter
                string = outter_spacing + char + outter_spacing
            else:
                outer_str = outter_spacing + char
                middle_spacing = (
                    (total_str_len - len(outer_str * 2)) * cls.SPACING)
                string = outer_str + middle_spacing + outer_str[::-1]

            diamond_half.append(string)
            space_len -= 1

        return diamond_half