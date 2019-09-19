import csv
fh = open("emp.csv")
reader = csv.reader(fh)
for rec in reader:
    print(rec)