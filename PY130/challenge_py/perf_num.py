"""Perfect Number PEDAC:
P:
    in: integer (positive)
    out: string classification of whether a number
      is perfect, abundant, or deficient.
    e:
    i:
    - PerfectNumber class:
        - init: doesnt allow negative numbers (try catch)
        - classify class(?) method: takes in num and 
            returns string classification
            ("deficient", "perfect", "abundant" or rais)
            - need to find divisors
            - if, elif, else conditions of sum of divisors:
                    - == num: "perfect
                    - > num: "abundant"
                    - < num : "deficient"
        -
    ?: can it take in 0
    -self.fail("Expected exception not raised")
         --> do i need to create as instance var
    - what is a divisor:
      (a number that divides into another without a remainder.
    - how to find all the divisors of a num: 
    for num in range(1,num+1: if number % num == 0 add num to list 
E: test_perf_num.py
D:
"""

class PerfectNumber():

    @classmethod
    def classify(cls, number):
        if number <= 0:
            raise ValueError("Input must be a positive integer")

        divisors = [num
                    for num in range(1, number)
                    if number % num == 0]
        sum_divisors = sum(divisors)

        if sum_divisors == number:
            return "perfect"
        if sum_divisors > number:
            return "abundant"
        return "deficient"
