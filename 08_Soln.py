# Function with **kwargs
# Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_kwargs(**kwargs): # to pass multiple value
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name = "Rohit", power="good")
print_kwargs(name="Rohit Man Singh")
print_kwargs(name="Rohit", power="good", enemy="Java")