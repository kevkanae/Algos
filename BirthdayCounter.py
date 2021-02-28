# Write a python program that uses datetime module within a class , takes a birthday as
# input and prints user’s age and the number of days, hours ,minutes and seconds until
# their next birthday.
from datetime import date


class Birthdaytimer:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def findAge(self):
        self.age = date.today().year - self.year - ((date.today().month,
                                                     date.today().day) < (self.month, self.day))
        print(f'Current Age: {self.age}')

    def daysLeft(self):
        self.day = date(date.today().year, self.month, self.day) - date.today()
        print(f'{(self.day).days} days left for your birthday')


timer = Birthdaytimer(
    int(input('Enter the Year of Birth: ')),
    int(input('Enter the Month: ')),
    int(input('Enter the Day: ')),
)
timer.findAge()
timer.daysLeft()
