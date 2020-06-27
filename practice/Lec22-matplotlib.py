import matplotlib.pyplot as plt
import math

#val = [1, 5, 2, 4, 2]

#plt.plot(val)
#plt.ylabel("my numbers")
#plt.show() # displays figure



x_val = range(30)
y_val = [math.sin(x) for x in x_val]

plt.plot(x_val, y_val)
plt.xlabel("x")
plt.ylabel("sinx")
# plt.show()
plt.savefig("sinx.png")