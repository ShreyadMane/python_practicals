class Degree:
    def getDegree(self):
        print("I got a degree")
class Undergraduate(Degree):
    def getDegree(self):
        print("I am an Under-Graduate")
class Postgraduate(Degree):
    def getDegree(self):
        print("I am an Post-Graduate")
d = Degree()
d.getDegree()
u = Undergraduate()
u.getDegree()
p = Postgraduate()

