from sklearn import metrics
import numpy as np
import pandas as pd
import pprint


def find_entropy(df):
    clas = df.keys()[-1]
    values = df[clas].unique()
    entropy = 0
    for value in values:
        prob = df[clas].value_counts()[value] / len(df[clas])
        entropy += -prob * np.log2(prob)
    return np.cfloat(entropy)


def find_attr_entropy(df, attribute):
    clas = df.keys()[-1]
    attr_value = np.unique(df[attribute])
    target_values = np.unique(df[clas])
    avg_entropy = 0
    for value in attr_value:
        entropy = 0
        for value1 in target_values:
            num = len(df[attribute][df[attribute] == value]
                      [df[clas] == value1])
            den = len(df[attribute][df[attribute] == value])
            prob = num / den
            entropy += -prob * np.log2(prob + 0.00001)
        avg_entropy += (den / len(df)) * entropy
    return np.cfloat(avg_entropy)


def find_winner(df):
    ig = []
    for key in df.keys()[:-1]:
        ig.append(find_entropy(df) - find_attr_entropy(df, key))
    return df.keys()[:-1][np.argmax(ig)]


def get_subtable(df, attribute, value):
    return df[df[attribute] == value].reset_index(drop=True)


def buildtree(df, tree=None):
    node = find_winner(df)
    attval = np.unique(df[node])
    clas = df.keys()[-1]
    if tree is None:
        tree = {}
        tree[node] = {}
    for value in attval:
        subtable = get_subtable(df, node, value)
        clavalue, counts = np.unique(subtable[clas], return_counts=True)
        if len(counts) == 1:
            tree[node][value] = clavalue[0]
        else:
            tree[node][value] = buildtree(subtable)
    return tree


df = pd.read_csv('weather.csv')
tree = buildtree(df)
pprint.pprint(tree)
