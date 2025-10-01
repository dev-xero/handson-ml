## Notes

1. Correlation coefficient only measures linear correlations, so it's hard to get accurate insight on non-linear relationships.
2. The first step in preparing data for Machine Learning algorithms often is cleaning.
3. Imputation is when you set missing values from a dataset to zero, or the mean/median.
4. A common step in MLE is data transformation, this can be done using what's called "Pipelines", in the book they use:
   1. SimpleImputer: for filling in missing values
   2. StandardSCaler: many ML models are sensitive to scales, using this transformer scales the features reasonably:
      1. for instance, mean=0, std=1
   3. OneHotEncoder: some categorical data in text format can't be fed into models, they work with numbers, OneHotEncoders convert categorical data into binary format.
   4. ColumnTransformer: in the book, this is an example of what's known as "Feature Engineering", it's combining existing features to create a new meaningful feature.
   5. ClusterSimilarity: they create a custom data transformer that uses KMeans clustering, they're looking for patterns involving geographical coordinates and possibly pricing.
5. In a situation where we have model underfitting, common workarounds are to:
   1. Select a more powerful model
   2. Improve the features
   3. Reduce model constraints
6. We usually split the dataset into (3) portions:
   1. Training set (60%)
   2. Validation set (20%)
   3. Test set (20%)