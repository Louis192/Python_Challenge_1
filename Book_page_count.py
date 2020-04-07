import os
import sys
#In below problem,I want to know how many pages I need to flip before I can get to a particular page.
# If I turning from first page,she needs to turn p//2
# If I to turning from the last page,she needs to turn n//2-p//2
def pageCount(n, p):
    return min(n//2-p//2,p//2)
    
    



n = int(input().strip())

p = int(input().strip())

result = pageCount(n, p)
print(result)