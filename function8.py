#Lets say I want an integer to be returned in binary format,below is the code:
def binary(n):
    output=bin(n)
    result=output[2:]
    return result
binary(4)