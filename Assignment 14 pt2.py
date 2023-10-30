import random
import string

def make_files(my_name='Rolando Evangelista', record_count=100000):
    try:
        with open('as_received1.txt', 'w') as file1:
            for _ in range(record_count):
                file1.write(''.join(random.choice(string.ascii_letters) for _ in range(10)) + '\n')
    except Exception as e:
        print(f"Error while creating 'as_received1.txt': {e}")

    try:
        with open('as_received2.txt', 'w') as file2:
            for _ in range(record_count):
                file2.write(''.join(random.choice(string.ascii_letters) for _ in range(10)) + '\n')
    except Exception as e:
        print(f"Error while creating 'as_received2.txt': {e}")

    try:
        with open('as_received3.txt', 'w') as file3:
            for _ in range(record_count):
                file3.write(''.join(random.choice(string.ascii_letters) for _ in range(10)) + '\n')
    except Exception as e:
        print(f"Error while creating 'as_received3.txt': {e}")

# Create some corrupt files to test exception handling
make_files(my_name='Rolando Evangelista', record_count=100000)

try:
    with open('as_received1.txt', 'r') as file1, open('as_received2.txt', 'r') as file2, open('as_received3.txt', 'r') as file3:
        lines1 = file1.readlines()
        lines2 = file2.readlines()
        lines3 = file3.readlines()
except FileNotFoundError as e:
    print(f"Error while opening files: {e}")
except Exception as e:
    print(f"An error occurred while reading files: {e}")

try:
    all_lines = lines1 + lines2 + lines3
    unique_lines = list(set(all_lines))
    unique_lines.sort()
except Exception as e:
    print(f"Error while processing data: {e}")

try:
    with open('corrected.txt', 'w') as corrected_file:
        corrected_file.write(''.join(unique_lines))
except Exception as e:
    print(f"Error while writing 'corrected.txt': {e}")

try:
    with open('source.txt', 'r') as source_file:
        source_content = source_file.read()
except FileNotFoundError as e:
    print(f"Error while opening 'source.txt': {e}")
except Exception as e:
    print(f"An error occurred while reading 'source.txt': {e}")

try:
    with open('corrected.txt', 'r') as corrected_file:
        corrected_content = corrected_file.read()
except FileNotFoundError as e:
    print(f"Error while opening 'corrected.txt': {e}")
except Exception as e:
    print(f"An error occurred while reading 'corrected.txt': {e}")

if 'source_content' in locals() and 'corrected_content' in locals():
    if source_content == corrected_content:
        print("The corrected file is identical to the source file.")
    else:
        print("The corrected file is NOT identical to the source file.")
