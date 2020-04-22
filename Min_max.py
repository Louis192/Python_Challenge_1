def minmax(arr):
    maximum=max(arr)
    minimum=min(arr)
    maxi=arr.copy()
    maxi.remove(minimum)
    mini=arr.copy()
    mini.remove(maximum)
    min_sum=sum(mini)
    max_sum=sum(maxi)
    print(min_sum,max_sum)
    
    
arr=list(map(int,input().rstrip().split()))
    
minmax(arr)