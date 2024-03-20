from functools import reduce

file = open("inputs\\task8.txt", "r")
nums = file.readline()
numbers = [int(char) for char in nums]

i, largest = 0, 0

for i in range(len(numbers)-13+1):
    currentSubset = numbers[i: i+13]
    if 0 in currentSubset:
        i += 13
    else:
        a = reduce(lambda x, y: x*y, currentSubset)
        largest = max(largest, a)
        i += 1

print(largest)