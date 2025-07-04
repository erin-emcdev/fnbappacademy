import calculate

l = float(input("enter the length of the rectangle: "))
w = float(input("enter the width of the rectangle: "))

area = calculate.area(l, w)
perimeter = calculate.perimeter(l, w)

print(f"area: {area}")
print(f"perimeter: {perimeter}")