# Implement a function that accepts 3 integer values a, b, c. 
# The function should return true if a triangle can be built with the sides of given length and false in any other case.
# 
# (In this case, all triangles must have surface greater than 0 to be accepted).
# 
# MATHS: Use the triangle inequality
# The sum of any two sides of a traingle is greater than or equal to the third side.
# a + b >= c
def check_triangle(a, b, c):
     return (a + b > c) and (a + c > b) and (b + c > a)