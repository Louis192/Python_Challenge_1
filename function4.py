# Given a list of 5 floats, return a tuple of the average of the middle 3 floats and the lowest float of that list.
# Note that in the code below,mean is a built in python function.
a=[10.5, 20.6, 12.6, 7.5, 2.4]
def values(a):
    result=mean(a[1:4])
    print( round(result,2),min(a))
    

values(a)