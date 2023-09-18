from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')  #sets the style.

#creating the data points.
xs = np.array([1,2,3,4,5,6], dtype=np.float64)
ys = np.array([5,4,6,5,6,7], dtype=np.float64)

def best_fit_slope_and_intercept(xs,ys):  #function for finding the slope and y intercept.

    m=( ((mean(xs) * mean(ys)) -mean(xs*ys)) /  #finding slope
    ((mean(xs)**2) - mean(xs**2)) )

    b = (mean(ys) - (m*mean(xs)))   #finding intercept
    return m,b

m,b = best_fit_slope_and_intercept(xs, ys)
print("m: ", m, "b: ", b)

regression_line= [(m*x)+b for x in xs]  #calculates the y-coordinates for the points on the best-fit line

#use the below code for calculating the predicted value of y-coordinate for a given x-coordinate
predict_x = 8
predict_y = (m*predict_x)+b

#plotting the values
plt.scatter(xs, ys)
plt.scatter(predict_x, predict_y, color='g')  #plotting the predicted values
plt.plot(xs, regression_line)
plt.show()