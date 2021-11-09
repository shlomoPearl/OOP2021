import csv
import json

file = open('C:/Users/Hp/Downloads/Calls_a.csv')

csvreader = csv.reader(file)

calls = []
for call in csvreader:
    calls.append(call)

elevator_id = 5

for item in calls:
    item[elevator_id] = 0

# for call in calls:
#     print(call)

f = open('C:/Users/Hp/Desktop/csv_file.csv', 'w', newline='')
writer = csv.writer(f)

writer.writerows(calls)

f.close()
#
# file2 = open('C:/Users/Hp/Desktop/csv_file.csv')
# reader = csv.reader(file2)
#
# new_calls = []
#
# for call in reader:
#     new_calls.append(call)
#
# file.close()
#
# for call in new_calls:
#     print(call)
#
# with open("C:/Users/Hp/Downloads/B4.JSON") as f2:
#     reader = json.load(f2)
#
# f2.close()
#
# elevators = reader['_elevators']
#
# print(type(elevators[0]["_closeTime"]))


