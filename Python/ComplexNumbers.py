
class Complex:
    def readComplex(self):
        self.real = int(input())
        self.imag = int(input())

    def displayComplex(self):
        return(f'{self.real} + i{self.imag}')

    def addComplex(self, c1, c2):
        self.real = c1.real + c2.real
        self.imag = c1.imag + c2.imag


if __name__ == "__main__":

    '''Intializing Class Objects'''
    obj1 = Complex()
    obj2 = Complex()
    obj3 = Complex()

    '''Reading the Complex Numbers and Displaying them'''
    print('Enter First Complex Number: ')
    obj1.readComplex()
    print(f'The First Complex Number is: {obj1.displayComplex()}')

    print('Enter Second Complex Number: ')
    obj2.readComplex()
    print(f'The Second Complex Number is: {obj2.displayComplex()}')

    '''Adding the Complex Numbers and then Displaying'''
    obj3.addComplex(obj1, obj2)
    print(f'The Added Complex Number is: {obj3.displayComplex()}')
