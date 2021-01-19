class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def sub(self, r):
        return sum(self.r * 2)


x = Complex
x.sub(2)
print(x.sub)