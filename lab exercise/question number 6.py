#solve each of the following problems using python scripts.make sure you use use approprite variable names and comments,
#when there is a final answer have python print it to the screen.
#a person's body mass index (BMI) is defined as:
#BMI=mass in kg/ (height in m)2
mass=float(input("enter the mass in kg: "))                     #mass in kg
height=float(input("enter the height in m: "))                  #height in m
bmi= mass/(height*height)
print(f"the bmi is{bmi}")