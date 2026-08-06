# Read the limit
limit = int(input())

number = 1
total = 0

# Initialize the loop variable and total
while number <= limit:
    # Examine every number from 1 to limit
    if number % 2 == 0:
        total = total + number
    
    # Increment the loop counter
    number = number + 1

# Display the result
print("Even Sum:", total)