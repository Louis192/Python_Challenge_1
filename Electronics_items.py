import os
import sys

#
# Complete the getMoneySpent function below.
#
def MoneySpent(keyboards, drives, b):
    under_budget=-1
    for k in keyboards:
        for d in drives:
            if (k+d<=b):
                under_budget=max(under_budget,k+d)
    return under_budget

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = MoneySpent(keyboards, drives, b)
    print(moneySpent)