# Develop a function to read and return the student’s USN, Name, Total-Marks.
# Create a list of student’s record and sort the records in the descending order of total marks
# (use list of tuples).

def read(n):
    def sortMarks(elem):
        return elem[2]
    for i in range(0, n):
        usn = input('Enter USN: ')
        name = input('Enter Name: ')
        totMarks = float(input('Enter Total Marks: '))
        li.append((usn, name, totMarks))
        li.sort(key=takeSecond, reverse=True)
    return li


li = []
n = int(input('Enter the Number of Students'))
result = read(n)
print(result)
