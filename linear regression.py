import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('headbrain.csv')

X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values

mean_x = np.mean(X)
mean_y = np.mean(Y)

n = len(X)
num = 0
den = 0
for i in range(n):
    num += (X[i]-mean_x)*(Y[i]-mean_y)
    den += (X[i]-mean_x)**2
m = num/den
c = mean_y-m*mean_x

print(f"y = {m}x + {c}")

ss_t = 0
ss_r = 0
for i in range(n):
    yp = c+m*X[i]
    ss_t += (Y[i]-mean_y)**2
    ss_r += (Y[i]-yp)**2
r = 1-(ss_r/ss_t)
print(r)
max_x = np.max(X)+100
min_x = np.min(X)-100

x = np.linspace(min_x, max_x, 1000)
y = c+m*x

plt.plot(x, y, color='red', label='regression line')
plt.scatter(X, Y, label='scater plot')
plt.xlabel('Head Size(cm^3)')
plt.ylabel('Brain Weight(grams)')
plt.legend()
plt.show()
