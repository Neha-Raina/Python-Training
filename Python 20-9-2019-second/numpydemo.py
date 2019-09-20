import numpy as np
ar = np.array([1,2,3,4])
print(ar)
print(ar.max())
print(np.max(ar))
print(np.min(ar))
print(np.sum(ar))
ar1 = np.array([11,22,33,44])

print(ar+ar1)
print(ar-ar1)
print(ar+ar1)
print(ar*ar1)

print(np.shape(ar))

arr = np.array([[1,2,3,4],[10,20,30,40],[11,22,33,44]])
print(arr)
print(np.shape(arr))
print(np.max(arr))
print(np.max(arr,axis=0))
print(np.max(arr,axis=1))
# ----------------------------------
print("---------------------------------")

print(np.min(arr,axis=0))
print(np.min(arr,axis=1))

print(np.sum(arr,axis=0))
print(np.sum(arr,axis=1))

# -------------------------------------------

ar1 = np.arange(10)
print(ar1)
# --------------------------

ar2 = np.arange(5,10)
print(ar2)

# -------------------------

ar3 = np.arange(0,10,3)
print(ar3)

# ----------------------------

ar4 = np.arange(0,2,0.3)
print(ar4)

# -------------------------------------
print("---------------------------------------------------------")

arr1 = np.array([11,22,33,1,2,3])
ar2d = arr1.reshape(2,3)
print(ar2d)

arr2 = arr1.reshape(3,2)
print(arr2)
print(ar2d.dot(arr2))

# ----------------------------------

dig = np.eye(4)
print(dig)



