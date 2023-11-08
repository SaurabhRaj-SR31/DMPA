from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pandas as pd

# Load your data
data = pd.read_csv('apriori_DB.txt', header=None)
data = data.applymap(str)  # Ensure the data is treated as strings

# Encode the data for Apriori
data_encoded = pd.get_dummies(data, prefix='', prefix_sep='')

# Find frequent itemsets using Apriori
min_support = 0.2  # Adjust this value as needed
frequent_itemsets = apriori(
    data_encoded, min_support=min_support, use_colnames=True)

# Generate association rules
min_confidence = 0.7  # Adjust this value as needed
rules = association_rules(
    frequent_itemsets, metric='lift', min_threshold=min_confidence)

# Display frequent itemsets and association rules
print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules)
