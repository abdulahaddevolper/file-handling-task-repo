# file_handling_tasks.py

# This file includes placeholders for file handling tasks.
# Students should complete each function according to the instructions.

def task1_create_file():
    # TODO: Create a new text file and write "Hello, world!" to it.
    pass
with open("hello.txt", "w") as file:
    file.write("Hello, World!\n")

def task2_read_file():
    # TODO: Read the contents of a file and print them to the console.
    pass
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)

def task3_append_file():
    # TODO: Append a new line of text to an existing file.
    pass
with open("hello.txt", "a") as file:
    file.write("My Name is John Doe\n")  # Change "John Doe" to your name

def task4_count_lines():
    # TODO: Count and print the number of lines in a file.
    pass
with open("hello.txt", "r") as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")

def task5_find_word():
    # TODO: Find whether a specific word exists in the file and how many times.
    pass
with open("hello.txt", "r") as file:
    content = file.read()
    count = content.count("Python")
    print(f"The word 'Python' appears {count} times.")

def task6_copy_file():
    # TODO: Copy the contents of one file to another.
    pass
with open("hello.txt", "r") as source_file:
    data = source_file.read()

with open("copy_hello.txt", "w") as destination_file:
    destination_file.write(data)
with open("hello.txt", "r") as source_file:
    data = source_file.read()

with open("copy_hello.txt", "w") as destination_file:
    destination_file.write(data)

def task7_replace_word():
    # TODO: Replace a specific word in the file with another word.
    pass
with open("hello.txt", "r") as file:
    content = file.read()

content = content.replace("Java", "Python")

with open("hello.txt", "w") as file:
    file.write(content)

def task8_read_csv():
    # TODO: Read a CSV file and print each row.
    pass
import csv

# Open and read the CSV file
with open("students.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"])

def task9_write_csv():
    # TODO: Write a list of dictionaries to a CSV file.
    pass
import csv

# Open a CSV file for writing
with open("students.csv", mode="w", newline='') as file:
    fieldnames = ["Name", "Score"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()  # Write the column names
    writer.writerows(students)  # Write each student's data

def task10_json_file():
    # TODO: Create a JSON file from a Python dictionary and read it back.
    pass
import json

# Read data back from the JSON file
with open("students.json", "r") as file:
    content = json.load(file)

print(content)
