"""First ten numbers in the Fibonacci Sequence"""

num_1 = 0
num_2 = 1
fib_list = [num_1, num_2]
for sequence in range(9):
    new_num = num_1 + num_2
    fib_list.append(new_num)
    num_1 = num_2
    num_2 = new_num

print(fib_list)
