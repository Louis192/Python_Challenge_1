# Below is a code that will select items in tuples
def similar_pattern(input,n):
    iters=[iter(input)]*n
    return zip(*iters)
names=['Alfred','Black','Carey','Drake','Elena','Ferguson','Georgina','Harrison']
list(similar_pattern(names,2))