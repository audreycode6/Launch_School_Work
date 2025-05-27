"""Series PEDAC:
P:
    -in: string of digits
    -out: return all possible consecutive
      num series of a specified length in that stirng
        -list with list elems : each list elem has # of elems
          == to int passed in to slices()
    -e:
    -i:
        - Series class:
            - init takes in number we will be slicing up
            - slices: instance method, takes in a int num 
                - find  all possible num combos of that len
                - if int == 1 
                    return a list with list of each num
                - if int > # of digits: raise ValueError
    -?:
E: test_series.py
D:
"""

class Series:
    def __init__(self, digits):
        self.digits = digits

    def slices(self, series_length):
        if series_length > len(self.digits):
            raise ValueError(
                "Slice length must not be greater than string length"
                )

        return self._build_series(series_length)

    def _build_series(self, series_length):
        series = []
        start = 0
        end = series_length
        max_start = len(self.digits) - series_length

        while start <= max_start:
            list_slice = [int(digit)
                          for digit in self.digits[start:end]]
            series.append(list_slice)
            start += 1
            end += 1

        return series