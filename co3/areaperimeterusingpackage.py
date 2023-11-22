from graphics import rectangle
from graphics import circle
from graphics.secondgraphics import cuboid
from graphics.secondgraphics import sphere
length=int(input("enter length"))
breadth=int(input("enter breadth"))
print("area of rectangle is:",rectangle.area(length,breadth))
print("perimeter of rectangle is:",rectangle.perimeter(length,breadth))
radius=int(input("enter radius"))
print("area of circle is:",circle.area(radius))
print("perimeter of circle is:",circle.perimeter(radius))
length=int(input("enter lentgth of cuboid"))
breadth=int(input("enter breadth  of cuboid"))
height=int(input("enter height of cuboid"))
print("area of cuboid is:",cuboid.surfacearea(length,breadth,height))
print("perimeter of cuboid is:",cuboid.perimeter(length,breadth,height))
radius=int(input("enter radius of sphere"))
print("area of sphere is:",sphere.surfacearea(radius))
print("perimeter of sphere is:",sphere.perimeter(radius))


