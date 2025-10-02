from sklearn.model_selection import StratifiedKFold
from sklearn.base import clone


def CustomKFoldsCV(estimator, X_train, y_train, X_test, y_test, n_splits=3):
    sk_folds = StratifiedKFold(n_splits)
    
    for train_idx, test_idx in sk_folds.split(X_train, y_train):
        clone_estimator = clone(estimator)

        X_train_folds = X_train[train_idx]
        y_train_folds = y_train[train_idx]

        X_test_folds = X_test[test_idx]
        y_test_folds = y_test[test_idx]

        clone_estimator.fit(X_train_folds, y_train_folds)
        y_pred = clone_estimator.predict(X_test_folds)
        n_correct = sum(y_pred == y_test_folds)

        print(n_correct / len(y_pred))
