from functools import wraps

# First, create the authenticate decorator
def authenticate(func):
    @wraps(func)
    def wrapper(user_id, *args, **kwargs):
        # Simulate authentication check
        print("AUTHENTICATING")
        authenticated_users = [101, 102, 103]
        if user_id not in authenticated_users:
            return "Authentication failed: Access denied"
        return func(user_id, *args, **kwargs)
    return wrapper

# Next, create the log_calls decorator
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"CALLING: {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"RESULT: {result}")
        return result
    return wrapper

# Now apply both decorators to a function

@log_calls
@authenticate
def get_user_data(user_id, data_type="basic"):
    # Simulate retrieving user data
    if data_type == "basic":
        return f"Basic data for user {user_id}"
    else:
        return f"Advanced data for user {user_id}"

# Test the function with various inputs


# print(get_user_data(101))
print(get_user_data(101, "Advanced"))
# print(get_user_data(420))
# print(get_user_data(420, "Advance"))