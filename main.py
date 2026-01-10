#Clean + professional 

def get_number(count):
    numbers = []
    for i in range(count):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    return numbers  

def calculate_average(numbers):
    total = 0 
    for n in numbers:
        total += n
    return total / len(numbers)

nums = get_number(5)
avg =  calculate_average(nums)
print("Average: ", avg)
