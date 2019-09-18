# ------Tuple-------
tp = tuple([11,22,44,55])
tp0 = (11,22,44,55)
print(tp)

print("--------------")
for ele in tp:
    print(ele)

print("------------------")

# Index base access

i = 0
while i<len(tp)-1:
    print(tp[i],end= ",")
    i+=1
print(tp[i])
# -------------Slicing-----------

tp1 = tp[1:3]
print(tp1)

tp2 = tuple([[100,200],[300,400],[500,600]])
print(tp2)

tp3 = (100,)
print(tp3)

tp4 = ([100])
for item in tp4:
    print(item)
