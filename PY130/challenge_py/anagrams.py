'''Anagrams:
Write a program that takes a word and a list of possible 
    anagrams and selects the correct sub-list that contains 
    the anagrams of the word.

For example, given the word "listen" and a list of candidates
    like "enlists", "google", "inlets", and "banana", the program 
    should return a list containing "inlets". Please read the test 
    suite for the exact rules of anagrams.
'''
'''PEDAC:
P:
    in: string to find matching anagrams 
        (used to call the match method, 
        which takes in a list of strings to check if anagram)
    out: list of strings that are anagrams
        - empty list if none found
    e:
    i:
    - An anagram is a word or phrase formed by rearranging the 
        letters of a different word or phrase, typically using 
        all the original letters exactly once. (must be same len)
    - Anagram class
        - 'match' method, takes in list of strings and returns a list of strings that are anagrams
               - case insensiteve: "Orchestra is anagram to Carthorse
                - exact match != anagram (must have different order)
                - substrings (i.e goody != good) must hae exact count of distinct chars 
                    and in different order and same case as original
E: test_anagrams.py
D:
    - maybe use regex (?)
    - maybe loop through each char in input stirng and 
        check that its char count matches the char count of current stirng in list to check
    '''

class Anagram:
    def __init__(self, detector):
        self.detector = detector.casefold()
        self.detector_dict = self.get_sorted_char_count_dict(self.detector)

    def match(self, list_of_strings):
        '''return list of strings from the list_of_strings 
        that are anagrams to detector'''
        anagrams = []

        for string in list_of_strings:
            # ensure strings are same length as detector & not equal in value
            if (string.casefold() != self.detector and 
                len(string) == len(self.detector)):
                # make sorted dict: {char: count, ...} for current string
                current_string_dict = self.get_sorted_char_count_dict(string.casefold())

                # compare current_string_dict and detector_dict are == 
                #   (i.e current string is an anagram):
                if self.detector_dict == current_string_dict:
                    anagrams.append(string)

        return anagrams
    
    def get_sorted_char_count_dict(self, string):
        '''returns dict with keys (chars) sorted alphabetically'''
        # use casefold to ensure that it matches anagrams case insensitively
        unsorted_char_count_dict = {char : string.count(char) 
                                    for char in string.casefold()}

        # order keys by alphabetical order
        abc_order_keys = list(unsorted_char_count_dict.keys())
        abc_order_keys.sort()

        # new abc order dict: keys = char, value = char_count
        return {char: unsorted_char_count_dict[char] 
                for char in abc_order_keys}
