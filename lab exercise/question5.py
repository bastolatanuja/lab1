#A School decided to replace the desk in three classroom.each desk sits two students.
# give the number of studentsw in each class.print the smallest poswsible number of desk that can be purchased.
#the program should read three integers;the number of students in each three classes a b and c respectivelty.
#in the first test there are three groups,the first group has 20 students and thus needs 10 desk.
# the second group has 21 students,so they can get by with no fewer than 11 desk.11 desks are also enough for the third
#grop of 22 students.so,we need 32 desk in total.
a=int(input('enter the number of student in class1: '))
b=int(input('enter the number of student in class2: '))
c=int(input('enter the number of student in class3: '))
desk_class1=(a//2)
print(f"the required number of desk in first class{desk_class1}")

desk_class2=(b//2)
print(f"the required number of desk in second class{desk_class2}")
desk_class3=(c//2)
print(f"the required number of desk in third class{desk_class3}")

remain_class1=(a % 2)
print(f"remaining desk for first class is {remain_class1}")
remain_class2=(b % 2)
print(f"remaining desk for second class is {remain_class2}")
remain_class3=(c % 2)
print(f"remaining desk for third class is {remain_class3}")
total_desk=desk_class1+ desk_class2+ desk_class3+remain_class1+ remain_class1+ remain_class2+ remain_class3
print(f"total number of desks that can be purchased is {total_desk}")