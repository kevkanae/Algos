import re
#r stands for raw string input
pattern = r"[a-zA-Z]+ \d+" #this regex means that a substring must b followed by a space and numbers
string = 'LXI 2013, VXI 2015, VDI 2014 are some of the variants of Maruti Suzuki Cars in India'
match = re.findall(pattern,string)
for i in match:
    print(i, end = ' ')