# Below is a function that will take 3 variables and return the maximux,
# I have decided not use python's max function,but I will just use if statement.

def output_max(x,y,z):
    if x>y:
        print(x)
    elif y>z:
        print(y)
    else:
        print(z)
output_max(1000,20,5)