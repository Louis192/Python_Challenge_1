import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    count=0
    tall=max(ar)
    for i in range(len(ar)):
        if (ar[i]==tall):     #This is where the max value will  be identified
            
            count+=1            # this is where max value will be counted
            
    return count
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)
    print(result)