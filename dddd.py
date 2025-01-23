from matplotlib import pyplot as plt

x = list(range(-10, 11))
y = []
for i in x:
    y.append(i**3)
print(x)
print(y)
plt.plot(x, y)
plt.show()


