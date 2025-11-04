## Chapter 4: Training Models

In this chapter I learn about the mathematics behind some well known Machine Learning algorithms and models.

### Regression

Linear Regression is one of the simplest models there is. There are two different ways of training one:

1. Using a closed-form equation: In this way, compute model parameters to best fit the model to the training set. We are essentially minimizing a cost function.

2. Using Gradient Descent (GD): GD is an important optimization algorithm that iteratively minimizes the cost function, and eventually converges to the right model parameters.

Polynomial regression is a more complex model used on non-linear datasets. Due to it having more parameters, it is prone to model over-fitting. One of the more popular regression models include Logistic Regression and one other, Softmax Regression.

#### Linear Regression

Linear regression is a linear model. This means that it makes prediction by taking the weighted sum of input features added onto a "bias" (or intercept) term.

$$
\hat{y} = \theta_{0} + \theta_{1}x_{1} + \theta_{2}x_{2} + \dots + \theta_{n}x_n
$$

$$
\hat{y} = \theta_{0} + \sum_{i = 1}^{n}{\theta_{i} x_i }
$$

Where:

-   `ŷ` (y-hat): is the predicted y value
-   `x_i`: is the ith feature
-   `θ_0` (theta_0): is the bias/intercept term
-   `θ_i` (theta_i): is the ith model parameter/weight

We can represent this much more concisely in vectorized form:

$$
\hat{y} = h_{\theta}(x) = \vec{\theta} \cdot \vec{x}
$$

Where:

-   `h`: is the hypothesis function
-   `θ` (theta): is an n-dimensional vector of model weights, called the parameter vector
-   `x`: is an n-dimensional vector of model features/inputs, called the feature vector

Common metrics for evaluating Regression models include:

-   Root Mean Squared Error
-   Mean Squared Error

$$
MSE(\textbf{X}, h_{\theta}) = \frac{1}{m} \sum_{i = 1}^{m} (\theta^{T} x^{(i)} - (y)^{(i)}) ^2
$$

Here X represents the entire dataset matrix, while x is the ith row from that matrix.

### Ridge Regression

Ridge Regression or L2 Regularization is simply a regularized version of Linear Regression. This is done by adding a regularization term.

$$
J(\theta) = MSE(\theta) + \frac{\alpha}{m} \sum_{i = 1}^{n} \theta_{i}^{2}
$$

**Note:** The bias term is not regularized. Also note that it is important to scale the features before using any regularized models.

The `l2` norm is also called the Euclidean norm, a measure of the vector's magnitude.

### Lasso Regression

Least absolute shrinkage and selection operator regression (LASSO) is another regularization model like R2, but instead uses the `l1` norm.

$$
J(\theta) = MSE(\theta) + 2 \alpha \sum_{i = 1}^{n} | \theta |
$$
