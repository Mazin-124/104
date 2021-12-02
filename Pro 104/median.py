import csv
with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

#sort data to get the height of the people.
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

n = len(new_data)
new_data.sort()

#using floor division to get to the nearest number whole number
# floor //
if n % 2 == 0:
    #get the first number
    median1 = float(new_data[n//2])

    #get the second number
    median2 = float(new_data[n//2 -1])

    #finding mean of the number
    median = (median1 + median2)/2
else:
    median = (new_data[n//2])

print('Median is: ' + str(median))