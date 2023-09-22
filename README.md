# Linear-Regression Best-Fit-Slope Fundamentals
## Linear Regression
- Linear regression is a supervised machine learning algorithm used for predicting a continuous target variable based on one or more independent input features.
- It's one of the simplest and most widely used algorithms for regression tasks.
- The basic idea behind linear regression is to model the relationship between the input features and the target variable as a linear equation.<br/><br/>
![](https://www.wallstreetmojo.com/wp-content/uploads/2022/06/linear-regression-3.jpg)
-  The most common form of linear regression is the simple linear regression, where there is only one independent variable.
-  For multiple independent variables, you have multiple linear regression.

## Best-Fit-Slope
- In linear regression, the "best fit slope" refers to the coefficient (parameter) that represents the relationship between the independent variable(s) and the dependent variable.
- It quantifies how the dependent variable changes for a unit change in the independent variable while keeping all other variables constant (in the case of simple linear regression) or while accounting for the effects of other independent variables (in the case of multiple linear regression).

> Best-fit-slope for Simple Linear Regression:<br/><br/>
> ![](https://toptipbio.com/wp-content/uploads/2021/03/Linear-regression-model-equation.jpg)
<br/><br/>

> Best-fit-slope for multiple Linear Regression:<br/><br/>
> ![](https://miro.medium.com/v2/resize:fit:1400/0*pJsp76_deJvdDean)
<br/><br/>

> Equation for slope(m):<br/><br/>
> ![](https://cdn-images-1.medium.com/max/800/1*vji1X_3xW3lZsXUY4Vf-cg.png)
<br/><br/>

> Equation for finding the y-intersecpt(say a or b):<br/><br/>
> ![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4NDZ3ic9nakRBux1TtQMYbDzjh6rupnLAhhNza9J5PlbGpEEaVgWIEVJTH0A0G5G5DA&usqp=CAU)
<br/><br/>


The Pyhton code for finding the slope and the y-intersecpt are as follows:
```
def best_fit_slope_and_intercept(xs,ys):  #function for finding the slope and y intercept.

    m=( ((mean(xs) * mean(ys)) -mean(xs*ys)) /  #finding slope
    ((mean(xs)**2) - mean(xs**2)) )

    b = (mean(ys) - (m*mean(xs)))   #finding intercept
    return m,b
```
Where xs and ys are the values of x and y of the data pionts respectively.

## Squared Error and Coffecient Of Determination
### Squared Error

- In linear regression, squared error (also known as mean squared error or MSE) is a common metric used to evaluate the performance of the regression model.
- It measures the average of the squared differences between the predicted values and the actual (observed) values of the dependent variable.
- The squared error is a way to quantify how well the model's predictions align with the actual data points, with larger errors being penalized more heavily due to the squaring.
- The formula for squared error in the context of linear regression is as follows:

> For simple linear regression:
> ```
> MSE = (1 / n) * Σ(yi - ŷi)^2
> ```
> For multiple linear regression:
> ```
> MSE = (1 / n) * Σ(yi - ŷi)^2
> ```
- Where:
- __MSE__ is the mean squared error.
- __n__ is the number of data points in the dataset.
- __yi__ represents the actual observed value of the dependent variable for the ith data point.
- __ŷi__ represents the predicted value of the dependent variable for the ith data point as given by the linear regression model.

### Coefficient Of Determination
- The coefficient of determination, often denoted as R-squared (R²), is a statistical measure used in linear regression to assess the goodness of fit of the regression model to the observed data.
- It provides information about the proportion of the variance in the dependent variable (the target) that is explained by the independent variables (the predictors) in the model.
- In other words, R-squared quantifies how well the regression model captures the variability in the data.


> R² is calculates as follows:
> ```
> R² = 1 - (SSE / SST)
> ```
- Where,
- __SSE__ is the Residual Sum of Squares, represents the unexplained variability or the sum of the squared differences between the observed Y values and the predicted Y values from the regression model.
> - The formula for SSE is as follows:
>  ```
>  SSE = Σ(yi - ŷi)²
>  ```
> - Here, yi represents the observed values of the dependent variable.
> - ŷi represents the predicted values of the dependent variable from the regression model.

- __SST__ is the Total Sum of Squares, represents the total variability in the dependent variable (Y).It is calculated as the sum of the squared differences between each observed Y value and the mean of Y.
> - The formula for SST is as follows:
>   ```
>   SST = Σ(yi - ȳ)²
>   ```
> - Here, yi represents the observed values of the dependent variable.
> - ȳ represents the mean of the observed values.
<br/><br/>


From the Pyhton file posted above, The python code for finding the Squared error and the Coefficient of determination are as follows:
```
def squared_error(ys_orig, ys_line):   #calculating the squared error
    return sum((ys_line - ys_orig)**2)

def coefficient_of_determination(ys_orig, ys_line):  #calculates the coefficient of determinaton or the R squared values
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return  1 - (squared_error_regr / squared_error_y_mean)

r_squared = coefficient_of_determination(ys, regression_line)
print(r_squared)
```




