#Calculate CGPA of 3 Semesters

sem = int(input('Enter the Number of Semesters: '))
for _ in range(0,sem):

d = {}
ls = marks.split('\n')

for i in range(1,len(ls)):
    line = ls[i]
    columns = line.split(' ')
    usn = columns[0].strip()
    mark = columns[2].strip()
    d[usn] = d.get(usn,0) + int(mark)
print(mark)