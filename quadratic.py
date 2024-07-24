import math

def find_roots(a,b,c):
    d = b ** 2 - 4 * a * c
    sqrt_dis=math.sqrt(d)
    root1 = (-b + sqrt_dis) / (2*a)
    root2= (-b - sqrt_dis) / (2*a)
    root1=round(root1,2)
    root2=round(root2,2)
    return root1,root2
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
roots=find_roots(a,b,c)
print("the roots are :",roots)






