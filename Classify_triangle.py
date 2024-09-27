def Classify_triangle(a,b,c):
    if a+b <= c or a+c <= b or b+c <= a:

     return "Not a triangle"

    elif a == b  == c :
       return"Equilateral triangle"
    
    elif a == b or b == c or a == c :
       return"Isosceles triangle"
    else:
       return"Scalene triangle"



#Ilyas Oubousken    
