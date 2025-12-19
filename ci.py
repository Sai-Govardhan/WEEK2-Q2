#24331A05I6

p=int(input("enter principal amount : "))
t=float(input("enter time in years : "))
r=float(input("enter rate of interest : "))
a = p * (1 + r/100) ** t
CI = a - p
print("Compound Interest : ",CI)
