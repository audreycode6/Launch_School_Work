'''You have a function that should check whether a key
exists in a dictionary and returns its value. 
However, it's raising an error. Why is 
that? How would you fix this code?
'''

'''original to debug:

def get_key_value(my_dict, key):
    if my_dict[key]: # doesnt actually check if key exists 
        # so runs as true and then the return raises error when key doesnt exist
        return my_dict[key] 
    else:
        return None

print(get_key_value({"a": 1}, "b")) # KeyError: 'b'
'''

'''solution:
use .get() bc that will return None if not found'''
def get_key_value(my_dict, key):
    return my_dict.get(key)

print(get_key_value({"a": 1}, "b")) # None
print(get_key_value({"a": 1}, "a")) # 1
