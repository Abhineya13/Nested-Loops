# Read two integers: rows and cols
rows = int(input())
cols = int(input())

# Outer loop iterates through each row
for row in range(rows):
    line = ""
    # Inner loop builds each row with stars
    for col in range(cols):
        line += "*"
    # Print the completed row
    print(line)
