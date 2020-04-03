def breakingRecords(scores):
    maximum=scores[0]
    minimum=scores[0]
    maxcount=0
    mincount=0
    for i in range(len(scores)):
        
        if (scores[i]>maximum):
            maximum=scores[i]
            maxcount+=1
        if (scores[i]<minimum):
            minimum=scores[i]
            mincount+=1
    return(maxcount,mincount)
n=int(input())
scores=list(map(int,input().rstrip().split()))
result=breakingRecords(scores)
print(result)