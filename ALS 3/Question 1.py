"""Get the smallest number out of three inputs"""

iteration = 0
min = int()
for num in range(3):
    if iteration == 0:
        first_num = int(input("Please enter an integer to be set as the lowest value: "))
        min = first_num
        iteration += 1
        continue
    new_num = int(input(f'Please enter an integer to compare to the lowest value: '))
    if new_num <= min:
        min = new_num

print(f'The smallest number is {min}')