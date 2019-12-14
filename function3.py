# The code below will read a file and print out a count of each name inside the file
list_of_names=[]
def Name_count():
    for line in open('file3.txt').readlines():
        list_of_names.append(line.strip())
        count_names=list(set(list_of_names))
    for name in count_names:
        print(name + ' occurred ' + list_of_names.count(name) + 'times')
Name_count()

    