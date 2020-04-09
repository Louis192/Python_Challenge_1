def studentgrades(grades):
    #Below we are iterating through the grades
    for num in range(len(grades)):
        #Below its because we want to round grades that are above 38
        if grades[num]>37:
            #Below we want only multiples of 5 
            if grades[num]%5!=0:
                #Below we are substracting grades from subsequent multiples of 5 and making sure they are less than 3
                if 5-grades[num]%5<3:
                    # If above condition is true then the difference will be added to the existing grades.
                    grades[num]+=5-grades[num]%5
    return grades

grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)
        
result = studentgrades(grades)
print(result)