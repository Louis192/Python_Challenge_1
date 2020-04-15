if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #Get list by student name
    student_list=student_marks[query_name]
    sum=0
    for i in student_list:
        sum+=i
        average=(sum)/3
    #Out to 2 decimal place
    print('%.2f'% average)