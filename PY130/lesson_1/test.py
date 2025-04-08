def foo(integer, callback):
    return callback(integer)

print(foo(5, lambda x: x * x))