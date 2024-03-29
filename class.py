class circle:
    pi=3.14
    def __init__(self,radius):
        self.rad=radius
        
    def circum(self):
        return 2*circle.pi*self.rad

c1=circle(5)
print(c1.circum())