import math

class complex_numbers:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def print(self):
        print(self.real,"+",self.imag,"i")
    
    def real(self):
        return self.real
    
    def imag(self):
        return self.imag
    
    def argument(self):
        return (math.atan2(self.imag,self.real))
    
    def conjugate(self):
        new_imag = 0 - self.imag
        print(self.real,"+",new_imag,"i")
    
Com = complex_numbers(3.9,-5.6)
Com.print()
real = Com.real
imag = Com.imag
arg = Com.argument()
print(real)
print(imag)
print (arg)
Com.conjugate()
