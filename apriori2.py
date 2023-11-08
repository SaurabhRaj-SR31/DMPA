from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pandas as pd

# Define your transactional database as a list of lists
transactions = [
    ["A", "B", "E"],
    ["B", "D"],
    ["B", "C"],
    ["A", "B", "D"],
    ["A", "C"],
    ["B", "C"],
    ["A", "C"],
    ["A", "B", "C", "E"],
    ["A", "B", "C"]
]

# Create a pandas DataFrame from the transactions
df = pd.DataFrame(transactions)

# Use one-hot encoding to convert the data to a binary format
oht = pd.get_dummies(df, prefix="", prefix_sep="")

# Find frequent itemsets using the Apriori algorithm
min_support = 0.2  # Adjust the minimum support as needed
frequent_itemsets = apriori(oht, min_support=min_support, use_colnames=True)

# Generate association rules
min_confidence = 0.5  # Adjust the minimum confidence as needed
rules = association_rules(
    frequent_itemsets, metric="confidence", min_threshold=min_confidence)

# Print the frequent itemsets and association rules
print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules)
