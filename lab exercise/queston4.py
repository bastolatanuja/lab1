name= (input('enter the name'))
age= int(input('enter the age'))
add=name+str(age)
print(f"my name and age is{add}")
#next process
print("hello my name is"+name+"and i am"+str(age)+"years old")
#process num.3
print("hello my name is",name,"and i am",age,"years old")
#process4
print("hello my name is %s and i am %d years old" %(name,age))
#process5
print("hello my name is{} and i am {}years old".format(name,age))