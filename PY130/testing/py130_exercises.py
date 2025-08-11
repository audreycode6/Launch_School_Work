from time import perf_counter
from functools import lru_cache

@lru_cache
def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False

    return True

start_time = perf_counter()
is_prime(73729261)
end_time = perf_counter()
print(f"{end_time - start_time} seconds.")
# 2.0238720000052126 seconds.