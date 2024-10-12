# Module 6 Lab: Hotdog Cookout Lab
# Marquies White
# 10/12/2024

# Variable for total hot dogs
total_hot_dogs = 0

# Function to find total hot dogs
def get_total_hot_dogs():
        # Initiliazing the variables
        attendees = 0
        hot_dogs = 0
        # Asking the user how many attendees there will be
        attendees = int(input("What is the maximum number of expected attendees?"))
        # Asking the user how many hot dogs each attendee should get
        hot_dogs = int(input("How many hot dogs for each attendee?"))
        # Multiplying to get the total number of hot dogs needed
        total = attendees * hot_dogs
        return total


# Call total hot dogs and assign it to total hot dogs
total_hot_dogs = get_total_hot_dogs()

# Fucntion to display the total hot dogs
def show_results(total_hot_dogs):
        print("Total hot dogs needed:", total_hot_dogs)

# Call the results (Display the total)
show_results(total_hot_dogs)

# Initializing constant DOGS for a pack of 10 hot dogs
DOGS = 10

# Initializing constant DOGS for a pack of 10 hot dogs
BUNS = 8

# Variable for leftover hot dogs
dogs_left = 0

# Variable for leftover buns
buns_left = 0

# Variable for minimum amount of hot dog packages
min_dogs = 0

# Variable for minimum amount of buns
min_buns = 0

# Finding the amount of hot dogs left over
def find_dogs_left():
        dogs_left = (DOGS - total_hot_dogs % DOGS) % DOGS
        return dogs_left
         

# Finding the minimum of hot dog packages needed
def find_min_dogs():
        min_dogs = (total_hot_dogs / DOGS) + (0 ** (0 ** dogs_left))
        return min_dogs

# Assign dogs left
dogs_left = find_dogs_left()

# Assign min dogs
min_dogs = find_min_dogs()

# Finding the amount of bunsleft over
def find_buns_left():
        buns_left = (BUNS - total_hot_dogs % BUNS) % BUNS
        return buns_left

# Finding the minimum of bun packages needed
def find_min_buns():
        min_buns = (total_hot_dogs / BUNS) + (0 ** (0 ** buns_left))
        return min_buns

# Assign buns left
buns_left = find_buns_left()

# Assign min buns
min_buns = find_min_buns()

print("Minimum packages of hot dogs needed:", min_dogs)
print("Minimum packages of hot dog buns needed:", min_buns)
print("Hot dogs remaining:", dogs_left)
print("Hot dog buns remaining:", buns_left)