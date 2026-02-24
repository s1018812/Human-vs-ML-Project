# Human vs Machine Learning Project

This project challenges you to explore the differences between human-designed algorithms and machine learning models. You will first create a human algorithm (pseudo-code) to classify data based on features, then translate that algorithm into Python. Next, you will train a K-Nearest Neighbors (KNN) classifier on the same dataset and compare your results. Finally, you will record a short screen-share with narration explaining your methods and observations.

You may work alone or with a partner. You may choose to work with the provided Penguins dataset, or select your own pre-cleaned dataset from the links below (I have suggested a few datasets as a guide, but you are welcome to select something different with approval).  The most important detail regarding your data-set is that your data needs to lend itself to classification.  For example, an iris with a sepal length of x and a petal width of y can be classified as ‘Setosa’. I also recommend that you use github codespaces, as you will need access to command-line tools that are unavailable in VS Code for EDU.

[UCI Machine Learning Repository](https://archive.ics.uci.edu/datasets)
 - Iris (classic 3-class classification)
 - Mushroom (binary classification: edible/poisonous)
 - Student Performance (predict grades, numeric features)

[Kaggle Datasets](https://www.kaggle.com/datasets)   *Note: For Kaggle, I will have to download the data for you and post on a shared drive.
 - Titanic survival dataset (binary classification)
 - Heart disease dataset (binary classification)
 - Breast cancer diagnosis (binary)
 - Penguins dataset (same as Kira, already cleaned)

---

**Team Members:**  
Harshita Nagar

**Dataset Used:**  
Mushroom Dataset

**Source:**  
[UCI Mushroom Data](https://archive.ics.uci.edu/dataset/73/mushroom)
[Import ReadMe for Data](https://github.com/uci-ml-repo/ucimlrepo)

**Target Variable (What we are predicting):**  
Predicted Attribute: Classify if a mushroom is edible or poisionous 

**Features Used:**  
- Bruises
- Odor
- Cap-color
- Habitat

**[Video Review](https://)**



## Getting Started
<img src="/workspaces/Human-vs-ML-Project/getting_started/plots/bruises_v_odor.png" alt="X vs Y – Mushroom Dataset" width="400">
<img src="/workspaces/Human-vs-ML-Project/getting_started/plots/odor_v_cap-color.png" alt="X vs Y – Mushroom Dataset" width="400">
<img src="/workspaces/Human-vs-ML-Project/getting_started/plots/odor_v_habitat.png" alt="X vs Y – Mushroom Dataset" width="400">

## Human Algorithm

### Pseudo-Code
```text
Out of the variables analyzed, odor had the clearest diffrence to classify a mushroom as posionous or edible. The human-algorithm is: 

    IF odor == almond:  
        Predict edible 
    ELIF odor == anise: 
        Predict edible 
    ELIF odor == none: 
        Predict edible
    ELSE: 
        Predict posionous

```

When examining the data and visualizations, I focused on the feature odor only because of the ones analyzed, it had the clearest distinction between poisonous and edible mushroom.

The plots/tables suggested values for edible odors to be almond, anise and none. I considered values other than these to see how they might relate to a mushroom being edible.

From the summary tables and visualizations, it appeared that odor could influence whether a mushroom was poisionous, which led us to using this factor in our decision rules.

### Confusion Matrix

Accuracy: 98.69%

| Actual \ Predicted| Posionous| Edible |
|-------------------|---------|---------|
| **Posionous**      |    1143     |    32    |
| **Edible**         |    0     |    1263   |

One example where our algorithm worked well is when the inputs were spicy or pungent, leading to a correct prediction of posionous because all of the mushrooms in the data set with that odor are poisionous.

An example where the algorithm did not perform as expected is when there was no odor, resulting in a prediction of poisionous instead of edible, which may have happened because no odor isn't as clear between posionous and edible as the other inputs.

These examples of success and failure highlight patterns in the data or limitations in our rules, such as the fact that there are some odors that didn't perfectly fit into the categories of posionous or edible. The exceptions to the rule caused the failures in the human model.

<img width="400" height="334" alt="image" src="/workspaces/Human-vs-ML-Project/human_algorithm/plots/human_model_training_results.png" />

## Machine Learning Model

I chose a value of k = 3 after comparing model performance across different values of k and observing that 3 was giving the most accurate results. If I increased the k number too much, the accuracy rates actually started to decrease. 

When analyzing the outputs and metrics, we noticed that changing k affected from 3-10 didn't change our results at all, which influenced our final choice as 3 was the first number where the best accuracy rate occured. If we increased the k-value dramatically (ex. k = 50) the accuracy actually went down

Based on the results shown in the tables or visualizations, k = 3 best matched our goals for model performance because it's able to capture local patterns without breaking because of a single outlier.

### Confusion Matrix

Accuracy: 98.97

| Actual \ Predicted| Posionous| Edible |
|-------------------|---------|---------|
| **Posionous**     |  1150   |    25   |
| **Edible**        |    0    |   1263  |

The table/visualization shows a clear pattern where the model predicts whether a mushroom is posionous or edible when cap color and odor are considered, indicating a strong relationship between these features.

The confusion matrix reveals that the model most often predicts posionous mushrooms as edible, suggesting these classes have similar feature values.

Compared to the human algorithm, the KNN model shows different behavior when utilizing the KNN method, as seen in the visualization below.

<img width="400" height="334" alt="image" src="/workspaces/Human-vs-ML-Project/ml_model/plots/knn_model_test_results.png" />
