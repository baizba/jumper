import csv

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression

X = []
y = []
with open('trainingData.csv', newline='') as csvFile:
    reader = csv.reader(csvFile, delimiter=';', quotechar='|')
    for row in reader:
        X.append(row[0])
        y.append(row[1])

X = X[2:]
y = y[2:]

X = np.array(X, dtype=int).reshape(-1, 1)
y = np.array(y, dtype=int)
# tmpCol = np.array([1] * len(X), dtype=int)
# X = np.column_stack((X, tmpCol))

# X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = 1 * x_0 + 2 * x_1 + 3
# y = np.dot(X, np.array([1, 2])) + 3

print(X)
print(y)
# reg = LinearRegression().fit(X, y)
reg = LogisticRegression().fit(X, y)
# print("score ", reg.score(X, y))

# print("coef ", reg.coef_)
# print("intercept ", reg.intercept_)
print(reg.predict(np.array([[25]])))
# reg.predict(np.array([[3, 5]]))
print(reg.score(X, y))

plt.scatter(X, y, color="g")
plt.plot(X, reg.predict(X), color="b")
plt.show()
