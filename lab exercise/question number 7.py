#you live 4 miles from university.the bus driver at 25mph but spends 2 minutes at each of the 10 stops on the way.
# How long will the bus journey take?alternatively,you could run to university.you jog the first miles at 7mph,then run
#the next two at 15mph;before jogging the last at 7mph again.will t5his be quicker or slower than the bus.
distance_from_university=4
bus_speed=25
time_taken=((distance_from_university/bus_speed)*60)
#2 minutes in each stop
time_spends=20
total_time=time_taken + time_spends
print(f"total time taken by the bus{total_time}")

jog_one=((1/7)*60)
jog_two=((2/15)*60)
jog_three=((1/7)*60)
total_walk_time=jog_one+jog_two+jog_three
print(f"total_walk_time{total_walk_time}")
if (total_time>total_walk_time):
    print("taking bus is slower than running")

else:
    print("taking bus is faster than running")










