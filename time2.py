str_time = input("What time is it now?")
str_wait_time = input("What is the number of nours to wait?")
time = int(str_time)
wai_time = int(str_wait_time)

time_when_alarm_go_off = time + wait_time
print(time_when_alarm_go_off)

#Ivette Mujica
#CSS-205 Module 4 assignment

str_time = input("What time is it now? ")
str_wait_time = input("What is the number of hours to wait? ")  

# Corrected typo in 'hours'

time = int(str_time)
wait_time = int(str_wait_time)  

# Fixed variable name

time_when_alarm_go_off = (time + wait_time) % 24 

 # Use modulo to get the time within 0-23 range
 
print("The time when the alarm will go off is:", time_when_alarm_go_off) 

 # Added a message for clarity
