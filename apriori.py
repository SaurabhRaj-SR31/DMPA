

def load_transactions_from_csv(csv_file):
    transactions = []
    with open(csv_file, 'r') as file:
        for line in file:
            items = line.strip().split(',')
            # Filter out empty items
            transaction = [item for item in items if item]
            if transaction:  # Check for empty transactions
                transactions.append(transaction)
    return transactions

# Generate candidate itemsets for the given frequent itemsets


def generate_candidates(frequent_items, k):
    candidates = []
    for itemset1 in frequent_items:
        for itemset2 in frequent_items:
            if itemset1 != itemset2:
                candidate = sorted(list(set(itemset1 + itemset2)))
                if len(candidate) == k and candidate not in candidates:
                    candidates.append(candidate)
    return candidates

# Prune the candidate itemsets based on the subset property


def prune_candidates(candidates, frequent_items):
    pruned_candidates = []
    for candidate in candidates:
        is_valid = True
        for item in candidate:
            subset = sorted(list(set(candidate) - {item}))
            if subset not in frequent_items:
                is_valid = False
                break
        if is_valid:
            pruned_candidates.append(candidate)
    return pruned_candidates

# Calculate the support count of an itemset in the transactions


def calculate_support(transactions, itemset):
    count = 0
    for transaction in transactions:
        if all(item in transaction for item in itemset):
            count += 1
    return count

# Implement the Apriori algorithm


def apriori(transactions, min_support):
    # Initialize the frequent items with single items found in the dataset
    frequent_items = [[item]
                      for transaction in transactions for item in transaction]
    k = 2

    unique_1_itemsets_printed = set()

    while frequent_items:
        print(f"Frequent Itemsets of Size {k - 1}:")
        for itemset in frequent_items:
            if len(itemset) == 1:
                item = itemset[0]
                if item not in unique_1_itemsets_printed:
                    support = calculate_support(transactions, itemset)
                    if support >= min_support:
                        print(f"Itemset: {itemset}, Support: {support}")
                    unique_1_itemsets_printed.add(item)
            else:
                support = calculate_support(transactions, itemset)
                if support >= min_support:
                    print(f"Itemset: {itemset}, Support: {support}")

        candidates = generate_candidates(frequent_items, k)
        candidates = prune_candidates(candidates, frequent_items)

        frequent_items = []
        for candidate in candidates:
            support = calculate_support(transactions, candidate)
            if support >= min_support:
                frequent_items.append(candidate)

        k += 1


if __name__ == "__main__":
    csv_file = "apriori_DB.txt"  # Replace with your CSV file path
    transactions = load_transactions_from_csv(csv_file)
    min_support = 2  # Adjust the minimum support as needed
    apriori(transactions, min_support)
