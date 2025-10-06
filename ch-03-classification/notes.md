1. Binary classifiers are one way to do image classification.
2. Stochastic Gradient Descent can be thought of as a Stochastic optimization of GD. It works by approximating an objective function with suitable smoothness properties.
3. A loss function maps an event with a "cost" associated with it.
4. Confusion Matrices are a way of counting how many times A is guessed as B for an A/B pair.
5. We can use confusion matrices to get the Precision and Recall scores of a model. But first, some definitions:
    1. False positives: Incorrectly flagged instances (we flagged wrongly)
    2. False negatives: Missed instances that should have been flagged (we accepted wrongly)
    3. Precision is concerned with false positives, when we flag, are we correct? TP / (TP + FP)
    4. Recall is concerned with false negatives, are we flagging enough? TP / (TP + FN)
6. You should prefer the PR curve whenever the positive class is rare or when you care more about the false positives than the false negative. Otherwise consider using the ROC curve.
7. Gaussian NB: Gaussian Naive Bayes.
8. SGD and Support Vector Machines (SVMs) are purely Binary Classifiers.
