#A School decided to replace the desk in three classroom.each desk sits two students.
# give the number of studentsw in each class.print the smallest poswsible number of desk that can be purchased.
#the program should read three integers;the number of students in each three classes a b and c respectivelty.
a=int(input('enter the number of student in class1: '))
b=int(input('enter the number of student in class2: '))
c=int(input('enter the number of student in class3: '))
d=a+b+c
print(f"the total no of students is{d}")
e=d//2
print(f"total no of desk is{e}")