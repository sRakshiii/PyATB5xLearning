#Triangle Classifier

s1 = int(input("Enter the length of side1"))
s2 = int(input("Enter the length of side2"))
s3 = int(input("Enter the length of side3"))

if s1 == s2 == s3:
    print("Equilateral triangle")
elif s1 == s2 or s2 == s3 or s3 == s1:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
