def sockMerchant(n, ar):
    ar.sort()
    result,initial=0,None
    for present in ar:
        if present==initial:
            result+=1
            initial=None
        else:
            present=initial
    return result
    
n = int(input())
    

ar = list(map(int, input().rstrip().split()))

result=sockMerchant(n, ar)
print(result)