""" Beer Song PEDAC:
P:
    -in: integer
    -out: string iwth lyric 
    -e:
    -i:
        -BeerSong class:
            - verse method: takes in 1 int arg and 
            returns string of that 1 verse
            - verses method:, takes in range 
                (2 args: 1st starts, and 2nd is final)
                - prob calls verse in a range and concates into a string
            - 0 has a unique verse but all others just need to replace
            - lyrics method: return whole song
    -?:
    
E: test_beer_song.py
D:
"""
class BeerSong:
    @classmethod
    def verse(cls, verse_num):
        return cls._build_verse(verse_num)

    @classmethod
    def verses(cls, start, end):
        concate_verses = [cls.verse(num)
                          for num in range(start, end-1, -1)]
        return "\n".join(concate_verses)

    @staticmethod
    def _build_verse(verse_num):
        if verse_num <= 0:
            return ("No more bottles of beer on the wall,"
                    " no more bottles of beer.\n"
                    "Go to the store and buy some more,"
                     " 99 bottles of beer on the wall.\n"
            )

        if verse_num == 1:
            return(
                "1 bottle of beer on the wall, 1 bottle of beer.\n"
                "Take it down and pass it around, "
                "no more bottles of beer on the wall.\n"
                )

        if verse_num == 2:
            return (
                "2 bottles of beer on the wall, 2 bottles of beer.\n"
                "Take one down and pass it around, "
                "1 bottle of beer on the wall.\n"
                )

        return (
                f"{verse_num} bottles of beer on the wall, "
                f"{verse_num} bottles of beer.\n"
                "Take one down and pass it around, "
                f"{verse_num - 1} bottles of beer on the wall.\n"
                )

    @staticmethod
    def lyrics():
        return BeerSong.verses(99,0)