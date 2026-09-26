# s="GRIET College Nizampet Hyderabad" #the output should be TEIRG EGELLOC TEPMAZIN DABAREDYH
# l=[1,2,3]
# s.upper().reverse().

# l.reverse()

# s="GRIET College Nizampet Hyderabad"
# print(" ".join(word[::-1]for word in input().split()))


# #pick every alternate odd number from the given input in single line
# s=list(filter(lamba x: x%2,[int(num) for num in input().split()]))
import csv
import numpy as np
APP="Instagram"
insta_list = []
study_time = []

# Load the data from CSV file
with open("digital_behaviour.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        insta_list.append(int(row["Instagram_Minutes"]))
        study_time.append(int(row["Study_Minutes"]))

# Take only the first 7 values
insta_list = insta_list[:7]
study_time = study_time[:7]

# Convert lists into NumPy arrays
insta_array = np.array(insta_list)
study_array = np.array(study_time)

# Part C — Basic calculations

# Add everything up
total = np.sum(insta_array)
print("Total:", total)

# Find the average
average = np.mean(insta_array)
print("Average:", average)

# Find the largest value
largest = np.max(insta_array)
print("Largest:", largest)

# Find the smallest value
smallest = np.min(insta_array)
print("Smallest:", smallest)

# Count how many values
count_values = len(insta_array)
print("Number of values:", count_values)


# Part D — Indexing

# First day
print("First day:", insta_array[0])

# Last day
print("Last day:", insta_array[-1])

# Third day
print("Third day:", insta_array[2])


# Part E — Slicing

# First three days
print("First three days:", insta_array[:3])

# Last two days
print("Last two days:", insta_array[-2:])

# Days two, three and four
print("Days 2, 3 and 4:", insta_array[1:4])


# Part F — Array operations

# Convert Instagram minutes into hours
hours = insta_array / 60
print("Instagram hours:", hours)

# Subtract Instagram minutes from Study minutes
diff = study_array - insta_array
print("Study minus Instagram:", diff)


# Part G — Boolean filtering

# Ask each value: greater than 100?
greater_than_100 = insta_array > 100
print("Greater than 100:", greater_than_100)

# Show only values greater than 100
greater = insta_array[insta_array > 100]
print("Values greater than 100:", greater)

# Count how many days were above 100
count = (insta_array > 100).sum()
print("Days above 100:", count)

# Show values above the average
above_average = insta_array[insta_array > np.mean(insta_array)]
print("Values above average:", above_average)