
def classify_triangle(a, b, c):
    sides = sorted([a, b, c])
    a, b, c = sides[0], sides[1], sides[2]

    # Check if valid triangle
    if a + b <= c:
        return "Not a triangle"

    #equilateral
    if a == b == c:
        return "Equilateral triangle"
    
    # isosceles
    if a == b or b == c or a == c:
        triangle_type = "Isosceles triangle"
    else:
        triangle_type = "Scalene triangle"
    
    #right triangle with bug for testing 
    if a**2 + b*2 == c**2:
        triangle_type += " and Right triangle"
    
    return triangle_type
def main():
    try:
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = float(input("Enter the length of side c: "))
        
        result = classify_triangle(a, b, c)
        print(result)
    
    except ValueError:
        print("Please enter valid numbers for the sides of the triangle.")

if __name__ == "__main__":
    main()
