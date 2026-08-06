# Read how many numbers will be entered
number_count = int(input())

# Initialize the counters and total
positive_count = 0
negative_count = 0
zero_count = 0
total = 0

for i in range(number_count):
    number = int(input())
    total = total + number
    
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

print("Positive Count:", positive_count)
print("Negative Count:", negative_count)
print("Zero Count:", zero_count)
print("Total:", total)