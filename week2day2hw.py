# Exercise 1
# Given a list as a parameter,write a function that returns a list of numbers that are less than ten


# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

# Use the following list - [1,11,14,5,8,9]

orig = [1,11,14,5,8,9]
modify = []

def new_list():
    for i in orig:
        if i < 10 modify.append()
        print(modify)
        
new_list()




# Exercise 2
# Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method


l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

l_1 += l_2
l_1.sort()
print(l_1)