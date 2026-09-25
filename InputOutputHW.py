#Import Math Module for additional mathematical functions
import math

#Enter Inputs
PIZZA = 8

print("Enter number of slices each family member will eat")

Fam1 = int(input("Family Member 1: "))
Fam2 = int(input("Family Member 2: "))
Fam3 = int(input("Family Member 3: "))
Fam4 = int(input("Family Member 4: "))
FamSum = Fam1 + Fam2 + Fam3 + Fam4

#Processing
WholePizzas = math.ceil(FamSum/PIZZA)
LeftOver = int(WholePizzas*PIZZA-FamSum)

#Display Outputs
print(f"Whole pizzas required: {WholePizzas}")
print(f"Pizza slices left over: {LeftOver}")