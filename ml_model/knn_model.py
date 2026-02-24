import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from data.fetch_data import load_mushroom_data

df, target_name = load_mushroom_data()

# I selected only the cap-color and odor features for classification.
X = df[['cap-color', 'odor']]
y = df[target_name]

# Encode categorical features using one-hot encoding
X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# I selected k=1 for the KNN classifier.
k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
y_train_pred = knn.predict(X_train)

# create confusion matrix
conf_matrix_knn = pd.crosstab(
    y_test,
    y_pred,
    rownames=['Actual'],
    colnames=['Predicted']
)

# compute accuracy on test data
accuracy_knn = (y_pred == y_test).mean()

# display results on test data
print(f"KNN classifier accuracy (k={k}): {accuracy_knn:.2%}\n")
print(conf_matrix_knn)

# Reconstruct plotting DataFrames from the original categorical columns
# Use the indices from the encoded splits to select matching rows from `df`.
test_df = df.loc[X_test.index, ['cap-color', 'odor']].copy()
test_df[target_name] = y_test
test_df['KNN_prediction'] = y_pred
test_df['correct'] = test_df['KNN_prediction'] == test_df[target_name]

# Reconstruct training plotting DataFrame
train_df = df.loc[X_train.index, ['cap-color', 'odor']].copy()
train_df[target_name] = y_train
train_df['KNN_prediction'] = y_train_pred
train_df['correct'] = train_df['KNN_prediction'] == train_df[target_name]

# Create a visualization of KNN classifier results
os.makedirs("ml_model/plots", exist_ok=True)

# Create a visualization for training data
# I left this commented out, but feel free to toggle this plot to see training results.
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=train_df,
    x='cap-color',
    y='odor',
    hue='correct',
    style='correct',
    s=100,
    palette={True: 'green', False: 'red'}
)

plt.title('KNN Algorithm (Training Set): Correct vs Incorrect Predictions')
plt.xlabel('Cap Color')
plt.ylabel('Odor')
plt.legend(title='Prediction Correct')
plt.grid(True)
plt.savefig('ml_model/plots/knn_model_training_results.png', dpi=150)
plt.close()

# Create a visualization for test data
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=test_df,
    x='cap-color',
    y='odor',
    hue='correct',
    style='correct',
    s=100,
    palette={True: 'green', False: 'red'}
)

plt.title('KNN Algorithm: Correct vs Incorrect Predictions')
plt.xlabel('Cap Color')
plt.ylabel('Odor')
plt.legend(title='Prediction Correct')
plt.grid(True)
plt.savefig('ml_model/plots/knn_model_test_results.png', dpi=150)
plt.close()