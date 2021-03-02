#given the integer N-the number of minutes that is passedsince midnight -how many hours and minutes are displayed on t
# the 24th digital clock?
#the program should print two number :the numbers of hours(o and 23)and the  number of minutes(between 0 and 59).
#for example, if N=150,then 150 minutes havepassed since midnight-i.e.now is 2;30 am.so,the program should print 2;30
N=int(input("enter the minutes passed since midnight: "))
hours=(N//60)
minutes=(N%60)
print(f"the hours is{hours}")
print(f"the minutes is{minutes}")
print(f"its {hours}:{minutes} now")