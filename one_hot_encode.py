import pandas as pd
item_features_part_1 = pd.read_csv("data/item_properties_part1.csv")
# We don't want to evaluate feature "available" because this property doesn't give us insights about the feature#
item_features_part_1 = item_features_part_1[item_features_part_1.property != "available"]
# Next, we would replace "categoryid" in property with the corresponded value(feature)
item_features_part_1.loc[item_features_part_1['property'] == "categoryid", 'property'] = item_features_part_1['value']
# Next, we would like to consider only the static features, which means the value does not change overtime
item_with_static_feature_1 = item_features_part_1[~item_features_part_1['value'].str.contains(' |n')]
# Do exact step for item_features_part_2 data
item_features_part_2 = pd.read_csv("data/item_properties_part2.csv")
item_features_part_2 = item_features_part_2[item_features_part_2.property != "available"]
item_features_part_2.loc[item_features_part_2['property'] == "categoryid", 'property'] = item_features_part_2['value']
item_with_static_feature_2 = item_features_part_2[~item_features_part_2['value'].str.contains(' |n')]
item_features_full = pd.concat([item_with_static_feature_1,item_with_static_feature_2], ignore_index=True)

#Drop duplicates
sorted_events = pd.read_csv("data/sorted_events.csv")
item_features_full = item_features_full[item_features_full["itemid"].isin(sorted_events["item_id"].unique().tolist())].drop_duplicates()
item_features_full = item_features_full.drop(["timestamp"], axis=1).drop_duplicates()

top_properties = item_features_full["property"].value_counts().head(500).index.tolist() # take top 500 properties
one_hot_encoded = pd.DataFrame()
itemids = []
sorted_events_item_list = sorted_events.item_id.unique()
sorted_events_item_list.sort()
feature_item_list = item_features_full["itemid"].unique()

import numpy as np
for item in sorted_events_item_list:

    if item not in feature_item_list:
        one_hot_encoded = pd.concat(
            [one_hot_encoded, pd.DataFrame(np.zeros(len(top_properties))).T],
            ignore_index=True)
        itemids.append(item)
    else:
        if item not in itemids:
            item_properties = item_features_full[item_features_full["itemid"] == item]["property"].unique()
            one_hot_encoded = pd.concat([one_hot_encoded,pd.DataFrame([1 if x in item_properties else 0 for x in top_properties]).T,], ignore_index=True)
            itemids.append(item)
one_hot_encoded.columns = top_properties
one_hot_encoded["itemid"] = itemids

one_hot_encoded = one_hot_encoded.drop(["itemid"], axis = 1)
one_hot_encoded.to_csv('item_onehotencode_new.csv', index=False)