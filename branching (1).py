# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year == int.input("Greetings! What is your year of origin? '))

if year <= 1900
    print ('Woah, that's the past!')
elif year > 1900 && year < 2020:
    print ("That's totally the present!")
elif:
    print ("Far out, that's the future!!")

#Ivette Mujica
#CSS-205 Module 4 

# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? "))

if year < 1900: 
    
     # Added colon

    print("Woah, that's the past!")
elif 1900 <= year <= 2020:  
    
    # Corrected logical operator

    print("That's totally the present!")
else: 
     
    # Changed `elif` to `else`
    
    print("Far out, that's the future!!")
