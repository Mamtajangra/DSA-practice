import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# x represents the roll number of students and y represents the overall score of students
x_data = np.array([6,7,8,9,10,11,12])
y_data = np.array([500,590,650,690,700,850,1000])

# trying to normalize function for fast result
# so  first of all we will find out mean
x_mean = np.mean(x_data)
x_mean
# now standard deviation
x_std = np.std(x_data)
x_std
# now normalize the data
x_norm = (x_data - x_mean)/x_std
x_norm
# similarly for y normalize
y_mean = np.mean(y_data)
y_mean

y_std = np.std(y_data)
y_std

y_norm = (y_data - y_mean)/y_std
y_norm

# now moving toward cost function means error loss
m = 0
b = 0
def cal_cost(x = x_data,y=y_data,m =m,b = b):
    n = len(x_data)
    y_pred = m*x  + b
    squared_error = (y_pred - y)**2
    cost = (1/2*n)*np.sum(squared_error)
    return cost

# now gradient descent here normalize x and y uses for best result 
# init are initialize values and lr is learning rate iter count means how much iterations are reqquired
def gradient_descent(x_norm, y_norm, m_init, b_init,lr  , iter_count):
    n = len(x_norm)
    m = m_init
    b = b_init
    for i in range(iter_count):
        y_pred = m*x_norm + b
        error = y_pred - y_norm
    # now partial derivative of m and b 
        der_m_init = (1/n)*np.sum(error*x_norm)
        der_b_init = (1/n)*np.sum(error)
    # other values of m and b after descent these are low values shows less error 
        m = m - lr * der_m_init
        b = b - lr * der_b_init
        cost1 = cal_cost(x = x_norm, y = y_norm,b = b, m = m)

    # for these iterations we will store values in a file 
        with open("regr.txt","a") as f:
            f.write(f"m-->{m},b-->{b},cost1-->{cost1}\n")
        print(f"m-->{m},b-->{b},cost1-->{cost1}\n")  


    # now call gradint function after provide values  to m,b b iter,lr 
    m_init = 0
    b_init = 0
    lr = 0.2
    iter_count = 20000
# call gradient descent
    gradient_descent(x_norm , y_norm,m_init, b_init,lr , iter_count)


# now find the values of last iteration of m and b and find actual values 

my_m = 0.9593207971020835
my_b = -1.0150610510858576e-16
m_actual = my_m*(y_std/x_std)
b_actual = y_mean - m_actual * x_mean
# print last iteration values
print(f" m_actual :{m_actual},b_actual:{b_actual}")

# predicted y in terms of actual data  
y_pred = m_actual * x_data + b_actual


# plotting graph and see the errors
plt.figure(figsize =(12,9))
plt.scatter(x_data,y_pred,color= "blue")
plt.plot(x_data,y_pred,color = "green")
plt.xlabel("roll number")
plt.ylabel("overall score")
plt.title("performance of students")
plt.grid()
plt.legend()
plt.show()