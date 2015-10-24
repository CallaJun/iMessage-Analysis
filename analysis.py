import csv

file_name = 'filename.csv'
f = open(file_name)
csv_f = csv.reader(f)

data = {
	
}

dates = []

for row in csv_f:
	if row[1][0:12] in data:
		data[row[1][0:12]] += 1
	else:
		data[row[1][0:12]] = 1
print data