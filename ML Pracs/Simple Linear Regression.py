import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = np.array([10, 9, 2, 15, 10, 16, 11, 16])
y = np.array([95, 80, 10, 50, 45, 98, 38, 93])
plt.xlabel('No of hours')
plt.ylabel('Risk Score')
plt.scatter(x,y,color='red',marker='+')
def getCoef(x,y):
    #mean of x and y
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    
    #Total no of values
    n = len(x)
    
    # formula to calculate b1 and b2
    numer = 0
    denom = 0
    for i in range(n):
        numer += (x[i] - mean_x) * (y[i] - mean_y)
        denom += (x[i] - mean_x) ** 2
    b1 = numer / denom
    b0 = mean_y - (b1 * mean_x)
    
    return(b0, b1)
coefs_ = getCoef(x,y)
print("Coefficients")
print(coefs_[0])
print(coefs_[1])
plt.xlabel('No of hours')
plt.ylabel('Risk Score')
plt.scatter(x,y,color='red',marker='+')
y_pred = coefs_[0] + coefs_[1]*x
plt.plot(x, y_pred, color = "b")

