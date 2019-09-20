import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "months" : ["Jan","Feb","Mar","Apr","May"],
    "tickets" : [123,346,599,568,770],
    "open" : [10,3,5,66,7]
}

df7 = pd.DataFrame(data)
df7.set_index("months",inplace=True)
print(df7)

# df7.plot.bar()
# plt.show()

plt.pie(df7["open"])
plt.show()


ar = np.random.rand(10)
df = pd.DataFrame(ar)
print(df)

# ------------------------------

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

ar2d = np.random.rand(2,3)
df1 = pd.DataFrame(ar2d)
print(df1)

# ____________________________________________

file1 = pd.read_csv("prod.csv",header = None,index_col =0)
df2 = pd.DataFrame(file1)
# df2.columns = ["ID","Text","EMP ID"]
# df2.index = ["R1","R2","R3"]
print(df2)

# -------------------------------------

