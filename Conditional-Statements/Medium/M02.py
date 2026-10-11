a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    
    if a == b == c:
        print("Equilateral")
    
    elif a == b or b == c or a == c:
        print("Isosceles")
    
    else:
        print("Scalene")

else:
    print("Not a triangle")