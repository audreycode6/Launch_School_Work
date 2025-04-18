def say_hello():
    print("Hello from the greet module.")


def greet_user(name):
    print(f"Hello {name}!")


if __name__ == "__main__":
    print("I am running as a script") 
    # output only when run directly from greet.py (python3 greet.py)