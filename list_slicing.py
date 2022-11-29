import numpy as np
a = [1, 2, 3, 4, 5]
z = [i for i in range(0, 100, 10)]
c = [10, 20, 30, 40, 50, 60, 70, 80, 90]

f = []
for i in range(0, 100 ,10):
    f.append(i)

print(z[:4])

f = [[10, 20],
     [30, 40],
     [50, 60],
     [10, 30]]
f = np.array(f)
s = f[:3, :1]

print(s)
