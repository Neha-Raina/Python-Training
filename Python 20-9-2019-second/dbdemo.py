import sqlite3
import csv
#------Get DB connection---------
conn = sqlite3.connect("pythondb.sqlite")
if conn is not None:
    print("Connected...........")
else:
    print("Connection Failed........")

# result = conn.execute("select * from Product")

# for rec in result:
    # print(rec)

# conn.execute("Insert into Product (PROD_ID,PROD_NAME,PRICE) VALUES (5,'Head Phones',500)")
# price = int(input("Enter new price : "))
# conn.execute("Update Product Set PRICE = "+str(price)+" where PROD_ID = 4 ")
# conn.execute("Update Product Set PRICE = ? where prod_id = ? ",[price,PROD_ID])
# conn.commit()
# conn.close()

# fh = open("prod.csv")
# content = csv.reader(fh)
# print(content)
# for rec in content:
#     print(rec)
#     conn.execute("Insert into Product  Values (?,?,?)",rec)
# conn.commit()
# conn.close()

# Writing to a file from database
result = conn.execute("select * from Product")

with open('file.txt','w') as writefile:
    final =csv.writer(writefile)
    for content in result:
        final.writerow(content)

