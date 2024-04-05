import csv
with open('dummy.csv', newline='') as csvfile:
    spamreader = list(csv.reader(csvfile, delimiter=','))
    print(spamreader[0])
    for row in spamreader:
        print(', '.join(row))