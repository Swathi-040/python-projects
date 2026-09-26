import numpy as np


insta_list = []

study_time = []
 
 
with open("digital_behaviour.cs","r", encoding="utf-8") as f:
    reader = csv.DicReader(f)

    for row in reader:
        insta_list.append(row[APP])
        study_time.append(row["Study time"])



insta_list = insta_list[:7]
study_list = study_time[:7]



insta_array = np.array(insta_list)
study_array = np.array(study_time)


#total = np.sum(insta_array)

total = insta_array.sum()

Avg = insta_array.mean()

Maxi = insta_array.max()
Min = insta_array.min()

insta_array[0]
insta_array[-1]

insta_array[0:3]
insta_array[-2::]# it goes to direct -2 and reverse
insta_array[1:4]



hours = insta_array / 60

diff = insta_array - study_array

greater_than_100 = insta_array > 100


greater = insta_array[insta_array >100]
count =(insta_array > 100).sum()

greater = insta_array[insta_array > Avg]