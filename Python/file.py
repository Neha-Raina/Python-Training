# ---------------read line by line----------
fh = open("emp.csv")
for i in fh.readlines():
    print(i)
fh.seek(0)
for line in fh.read():
    print(line)