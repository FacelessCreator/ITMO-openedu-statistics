import math
import matplotlib.pyplot as plt

# insert name of sample file
SAMPLE_FILENAME = 'sample.csv'

PLOT_INTERVALS_COUNT = 10

data = []

file = open(SAMPLE_FILENAME)
for line in file:
    v = float(line)
    data.append(v)
file.close()

n = len(data)
max_v = max(data)
min_v = min(data)
middle_v = sum(data) / n

s_squired = sum(list(map(lambda v: (v - middle_v)**2, data))) / n
s0_squired = s_squired * n / (n-1)

print('middle X: {}; S0^2: {}'.format(middle_v, s0_squired))

plot_interval = (max_v-min_v) / PLOT_INTERVALS_COUNT
X = list(map(lambda i: min_v+plot_interval*i, range(0, PLOT_INTERVALS_COUNT)))

Y = [0] * PLOT_INTERVALS_COUNT
for v in data:
    if v < max_v:
        Y[math.floor((v-min(data))/plot_interval)]+=1
print('plot intervals: ')
print(Y)

plt.plot(X, Y)
plt.show()

# FOR NORMAL SPREADING
teta_1 = middle_v
teta_2 = s0_squired # trololololololololololo from course authors
"""
# FOR EXPONENTIAL SPREADING
teta_1 = 1 / middle_v
teta_1 = 1 / s_squired**0.5 # OR
teta_2 = -999

# FOR EVEN SPREADING
teta_1 = 0 # ???
teta_2 = (2*middle_v-1) / 2
"""

print('teta1: {}; teta2: {}'.format(teta_1, teta_2))

