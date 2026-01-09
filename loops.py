# Loops.py

numbers = []

for i in range(5):
    num = float(input(f"Enter number { i + 1}: "))
    numbers.append(num)

total = 0 
for n in numbers: 
    total += n 

average = total / len(numbers)

print("Numbers entered: ", numbers)
print("Total: ", total)
print("Average: ", average)
