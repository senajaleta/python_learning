class Complecxs:
    def __init__(self,real,imag):
        self.real =real
        self.imag =imag
    def add(self, number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result =Complecxs(real,imag)
        return result
n1 =Complecxs(5,6)
n2 =Complecxs(-4,2)
result =n1.add(n2)
print('real = ',result.real)
print("imag = ",result.imag)



