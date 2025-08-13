import csv

# Writing CSV
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'London'],
    ['Charlie', 35, 'Paris']
]

with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading CSV
with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Using DictReader and DictWriter
with open('people.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old")

# Writing with DictWriter
fieldnames = ['Name', 'Age', 'City']
with open('people_dict.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'David', 'Age': 28, 'City': 'Berlin'})