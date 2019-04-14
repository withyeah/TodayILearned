# Practical ML

###### coursera/Launching into Machine Learning/week1

###### 20190410



## Supervised Learning

- label : what you want to predict

- the type of ML problem depends on whether or not you have labeled data and what you are interested in predicting

  ![image](https://user-images.githubusercontent.com/45819975/55881781-47fad900-5bde-11e9-8caa-3006312643d2.png)



## Regression and Classification

- In regression problems, we want to minimize the error between our predicted continuous value, and the label's continuous value, usually using mean squared error. 

- In classification problems, we want to minimize the error or mis-classification between our predicted class and the labels class. This is done usually using cross entropy. 

- In general, a raw continuous feature can be discretized into a categorical feature.

- There is a quadratic penalty for mean squared error, so it is essentially trying to minimize the euclidean distance between the actual label and the predicted label. 

  On the other hand, with classifications cross entropy, the penalty is almost linear and the predicted probability is close to the actual label, but as it gets further away it becomes exponential, when it gets close to the predicting the opposite class of the label. 

  ![image](https://user-images.githubusercontent.com/45819975/55884018-4a5f3200-5be2-11e9-9240-f386ac8d19ee.png)



## Short History of ML: 

### A. Linear Regression

#### 1. using normal equation

![image](https://user-images.githubusercontent.com/45819975/55884506-20f2d600-5be3-11e9-9fcd-1dad3e5c54fb.png)

![image](https://user-images.githubusercontent.com/45819975/55884542-3831c380-5be3-11e9-914f-49ee857e8172.png)

![image](https://user-images.githubusercontent.com/45819975/55884719-7fb84f80-5be3-11e9-801f-9558dbcf713b.png)



#### 2. gradient descent optimizatino algorithm

- we hope to find the lowest valley, regardless of where we start on the hyper surface. 

  This can be done by finding the gradient of the loss function, and multiplying that with a hyper parameter, learning rate, and then subtracting that value from the current weights. This process iterates until convergence. 

  ![image](https://user-images.githubusercontent.com/45819975/55885200-7976a300-5be4-11e9-9fe0-31030aa34d24.png)



### B. Perception