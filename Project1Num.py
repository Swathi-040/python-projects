import csv
import numpy as np
APP="Instagram"
insta_list = []
study_time = []

with open("digital_behaviour.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        insta_list.append(int(row["Instagram_Minutes"]))
        study_time.append(int(row["Study_Minutes"]))

insta_list = insta_list[:7]
study_time = study_time[:7]

insta_array = np.array(insta_list)
study_array = np.array(study_time)
total = np.sum(insta_array)
print("Total:", total)
average = np.mean(insta_array)
print("Average:", average)
largest = np.max(insta_array)
print("Largest:", largest)
smallest = np.min(insta_array)
print("Smallest:", smallest)
count_values = len(insta_array)
print("Number of values:", count_values)
print("First day:", insta_array[0])
print("Last day:", insta_array[-1])
print("Third day:", insta_array[2])
print("First three days:", insta_array[:3])
print("Last two days:", insta_array[-2:])
print("Days 2, 3 and 4:", insta_array[1:4])
hours = insta_array / 60
print("Instagram hours:", hours)
diff = study_array - insta_array
print("Study minus Instagram:", diff)
greater_than_100 = insta_array > 100
print("Greater than 100:", greater_than_100)
greater = insta_array[insta_array > 100]
print("Values greater than 100:", greater)
count = (insta_array > 100).sum()
print("Days above 100:", count)
above_average = insta_array[insta_array > np.mean(insta_array)]
print("Values above average:", above_average)
