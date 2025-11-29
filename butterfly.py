# Butterfly Pattern using For Loop

n = 5  # Number of rows

# Upper half of butterfly
for i in range(n):
    # Left wing
    for j in range(i + 1):
        print("*", end=" ")
    
    # Middle space
    for j in range(2 * (n - i - 1)):
        print(" ", end=" ")
    
    # Right wing
    for j in range(i + 1):
        print("*", end=" ")
    
    print()

# Lower half of butterfly
for i in range(n - 1, -1, -1):
    # Left wing
    for j in range(i + 1):
        print("*", end=" ")
    
    # Middle space
    for j in range(2 * (n - i - 1)):
        print(" ", end=" ")
    
    # Right wing
    for j in range(i + 1):
        print("*", end=" ")
    
    print()
