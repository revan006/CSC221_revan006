# Exercise 10-1: Learning Python
# Read and print the entire file
with open('learning_python.txt') as file:
    contents = file.read()
    print("Printing the entire file:")
    print(contents)

# Read and print the file by storing lines in a list
with open('learning_python.txt') as file:
    lines = file.readlines()
    print("\nPrinting the file line by line:")
    for line in lines:
        print(line.strip())

# Exercise 10-2: Learning C

with open('learning_python.txt') as file:
    lines = file.readlines()

modified_lines = [line.replace('Python', 'C') for line in lines]

print("\nModified content with 'Python' replaced by 'C:")
for line in modified_lines:
    print(line.strip())
