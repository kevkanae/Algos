# Write a python program that uses datetime module within a class , takes a birthday as
# input and prints user’s age and the number of days, hours ,minutes and seconds until
# their next birthday.

import datetime as D


class Birthdaytimer:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def findAge(self):
        self.age = D.datetime.now().year - self.year - ((D.datetime.now().month,
                                                         D.datetime.now().day) < (self.month, self.day))
        print(f'Current Age: {self.age}')

    def daysLeft(self):
        self.day = D.datetime(D.datetime.now().year,
                              self.month, self.day, 0, 0, 0, 0) - D.datetime.now()
        print(f'Time Left: {self.day}s')


timer = Birthdaytimer(
    int(input('Enter the Year of Birth: ')),
    int(input('Enter the Month: ')),
    int(input('Enter the Day: ')),
)
timer.findAge()
timer.daysLeft()
