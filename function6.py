#Below is a function that takes an integer and returns
#  the sum of the multiples of 7

def sum_mult_7(n):
    return(sum(x for x in range(n) if x%7==0))
sum_mult_7(35)