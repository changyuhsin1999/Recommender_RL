# Recommender_RL

Original source code (https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F185KB520pBLgwmiuEe7JO78kUwUL_F45t%2Fview%3Fusp%3Dsharing)

Train different session (contextual, sequential) based product recommendation recommenders
for E-commerce use cases and compare the performances of the recommenders.

##Data processing and training approach

From sorted event csv filter out unique item: 70852

Select only static properties (properties that doesn't change over time, such like color or size)

Pick out the top 500 most mentioned properties

One-hot encode these item features into the size of (70852,500)

Modified the logits of SNQN.py

Feed in the item feature with the modified logits
