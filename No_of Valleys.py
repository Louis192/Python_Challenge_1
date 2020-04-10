# in the below problem,Ben went for hiking and we want to know how many valleys he completed at the end of hiking.
## A valley is formed when Gary goes below the sea level and later come up to touch the sea level 
# So our main focus is when Garry makes an upward movement and touches the sea level
# So whenever Garry goes down and comes up to touch the sea level,a valley is formed.
# Downward trend is -1
# According to a number line,0 is the sea level,so whenever there is an upward trend and Garry touches the sea level or 0 
# then a valley is formed.
# Now According to the question,we have two characters U(Upward trend) and D(downwards trend),and our focus is on character U.
# So our focus now is if the altitude is 0 or touches the sea level upwards then a valley is formed.
# Level or altitude is +1 for U and -1 for D
#n==no of steps
#s=string of n characters
def No_of_Valleys(n,s):
    Altitude=valley=0
    for i in range(n):
        if s[i]=='U':
            Altitude=+1
            if Altitude==0:
                valley=+1
        else:
            Altitude=-1
    return valley
n=int(input())
s=input()
result=No_of_Valleys(n,s)
print(result)