import time

# Ask for user input
n = int(input("n? "))
if n <= 0:
    print("Invalid input. Please enter a positive integer.")
    exit()

# Start time
start_time = time.time()

# O(n) calculation
for i in range(1, n+1):
    pass  # Do some operation here

# End time
end_time = time.time()

# Calculate and print elapsed time in milliseconds
elapsed_time = (end_time - start_time) * 1000
print(elapsed_time)
