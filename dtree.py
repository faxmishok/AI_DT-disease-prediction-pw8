from utils import *
from query import *

class Child:
    def __init__(self, X, y):
        self.predictions = nb_counts(X, y)
class Tree:
    def __init__(self, query, true_branch, false_branch):
        self.query = query
        self.true_branch = true_branch
        self.false_branch = false_branch
def create_tr(X, y, attributes):
    gain, query = optimal_alt(X, y, attributes)
    if gain == 0:
        return Child(X, y)
    true_rows, false_rows, true_y, false_y = alternatives(X, y, query)
    true_branch = create_tr(true_rows, true_y, attributes)
    false_branch = create_tr(false_rows, false_y, attributes)
    
    return Tree(query, true_branch, false_branch)
def decide(row, node):
    if isinstance(node, Child):
        return node.predictions
    
    if node.query.compare(row):
        return decide(row, node.true_branch)
    else:
        return decide(row, node.false_branch)
def predict(counts):
    summa = sum(counts.values())*1.0
    targ = ''
    for lbl in counts.keys():
        targ = lbl 
    return targ
    