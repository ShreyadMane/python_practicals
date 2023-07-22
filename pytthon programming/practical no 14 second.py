class Rectangle:
    def get(self):
        self.length = int(input("Enter the length :- "))
        self.breadth = int(input("Enter the breadth :- "))
class Square:
    def get(self):
        self.side = int(input("Enter the side :- "))
class Area(Rectangle, Square):
    def showarea(self):
        r1 = Rectangle()
        s1 = Square()
        r1.get()
        s1.get()
        r_area = r1.length * r1.breadth
        s_area = s1.side * s1.side
        print("Area of Rectangle :- ",r_area)
        print("Area of Square :- ",s_area)
a1 = Area()
a1.showarea()
