def simple(x):
    output = []
    while x!=0:
        temp, power = 1, 0   # here we assign 1 to temp and 0 to power
        while temp<x:        # loop through whenever 1 is less than x
            temp *= 3   # here multiply temp by 3 and assign to temp
            if temp>x:   # here if temp greater than 1 terminate
                break
            power += 1   # add 1 to power
        x -= 3**(power)          # substract power of 3 from x
        output.append(3**power)
    return output
print(simple(33)) 
print(simple(4))  
print(simple(9))