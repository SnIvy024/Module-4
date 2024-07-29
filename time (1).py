currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait"

currentTimeInt = int(current_time_str)
waitTimeInt = int(wait_time_str)

finalTimeInt = currentTimeInt + waitTimeInt
print(finalTime_Int)

#Ivette Mujica
#CSS-205 Module 4

 # Added missing parenthesis
currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait?") 

currentTimeInt = int(currentTimeStr) 
 # Fixed variable name
waitTimeInt = int(waitTimeStr) 

 # Fixed variable name

finalTimeInt = (currentTimeInt + waitTimeInt) % 24 

 # Use modulo to get the time within 0-23 range

print("The time after waiting is:", finalTimeInt)

  # Fixed variable name and added a message
