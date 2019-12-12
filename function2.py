# Given two integer inputs n and d, create a function that squares all numbers from 1 to n, then returns the count of all instances of d from the square results.

# Example:

# n: 5

# d: 1

# square of numbers from 1 to 5: 1, 4, 9, 16, 25

# returns: 2 (since there's 2 instances of the digit 1, in 1 and 16)

def sqr_values(n,d):
    sqr=[i**2 for i in range(1,n+1)]
    print(sqr)
    combine_values=''.join(map(str,sqr))
    second_value_count=combine_values.count(str(d))
    print(f' {d} appears on in the list {second_value_count} times')
sqr_values(21,3)