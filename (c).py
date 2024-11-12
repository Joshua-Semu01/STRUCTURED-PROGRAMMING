#coming up with my own list
numbers = [1, 2, 3, 4, 5, 6, 7]
#initializing the number
lrgstnmbr = numbers[0]
#using a for loop
for number in numbers:   
    if number > lrgstnmbr:
        lrgstnmbr = number
#printing the final answer
print(f"The largest number in the list is {lrgstnmbr}")
