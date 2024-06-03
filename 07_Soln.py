# Function with *args
# Write a function that takes variable number of arguments and return their sum.

def summ_all(*args): # arg for multiple arguments
    print(args)
    for i in args:
        print(i * 2)
    return sum (args)

print(summ_all(1, 2, 3))
print(summ_all(1, 2, 3, 4, 5))
print(summ_all(1, 2, 3, 4, 5, 6, 7, 8))
