class Triangle:
    def triangel_perimeter(self,p):
        p = self.h + self.w + self.l
        return p

    def __init__(self,l,w,h):
        self.l = l
        self.w = w
        self.h = h
p1 =Triangle(2,4,5)
perimeter = p1.triangel_perimeter(p1)
print('perimeter =',perimeter)