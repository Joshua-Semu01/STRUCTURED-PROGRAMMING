
#SEMU JOSHUA M24D14/030



mylist = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26 ]

# List to store even numbers
evens = []

#if the if statement divides a number in the list and gives it a remainder 0, it will be returned as an even number
for number in mylist:
    if number % 2 == 0:
        evens.append(number)

# Print the even numbers in the list using an f string to concatenate
print(f"the even numbers are {evens}")
