# Recommender_RL

[Original source code](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F185KB520pBLgwmiuEe7JO78kUwUL_F45t%2Fview%3Fusp%3Dsharing)

[Kaggle data](https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset)

Train different session (contextual, sequential) based product recommendation recommenders
for E-commerce use cases and compare the performances of the recommenders.

## Data processing and training approach

From sorted event csv filter out unique item: 70852

Select only static properties (properties that doesn't change over time, such like color or size)

Pick out the top 500 most mentioned properties

One-hot encode these item features into the size (70852,500) of 1 and 0

Modified the logits of SNQN.py

Feed in the item feature with the modified logits and train with 5 epochs

Hyperparameter lambda with 0.1, 0.15, 0.2

## Comparison and Evaluation
recommender without features

![Screenshot](https://github.com/changyuhsin1999/Recommender_RL/blob/main/images/Screenshot%202023-11-23%20at%208.37.15%20PM.png)

recommender with item features (lambda = 0.1)

![Screenshot](https://github.com/changyuhsin1999/Recommender_RL/blob/main/images/Screenshot%202023-11-23%20at%208.43.37%20PM.png)

recommender with item features (lambda = 0.15)

![Screenshot](https://github.com/changyuhsin1999/Recommender_RL/blob/main/images/Screenshot%202023-11-23%20at%208.45.05%20PM.png)

recommender with item features (lambda = 0.2)

![Screenshot](https://github.com/changyuhsin1999/Recommender_RL/blob/main/images/Screenshot%202023-11-23%20at%208.47.04%20PM.png)


