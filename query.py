from utils import *
class Query:
    def __init__(self, column, value, attributes):
        self.column = column
        self.value = value
        self.attributes = attributes
        
    def compare(self, example):
        val = example[self.column]
        if check_numeric(val):
            return val >= self.value
        else:
            return val == self.value
    
    def __repr__(self):
        condition = '=='
        if check_numeric(self.value):
            condition = '>='
        return 'Is %s %s %s?' %(self.attributes[self.column], condition, str(self.value))
def alternatives(rows, target, query):
        true_rows, false_rows, true_y, false_y = [], [], [], []
        for i in range(len(rows)):
            if query.compare(rows[i]):
                true_rows.append(rows[i])
                true_y.append(target[i])
            else:
                false_rows.append(rows[i])
                false_y.append(target[i])
        return true_rows, false_rows, true_y, false_y
def optimal_alt(X, target, attributes):
        case1 = 0 
        best_question = None 
        
        current_uncertainity = gini_index(X, target)
        n_features = len(X[0]) 
        for col in range(n_features): 
            values = set([row[col] for row in X]) 
            for val in values: 
                query = Query(col, val, attributes)
                
                true_rows, false_rows, true_y, false_y = alternatives(X, target, query)
                if len(true_rows) == 0 or len(false_rows) == 0:
                    continue
                
                gain = gini_gain(true_rows, false_rows, true_y, false_y, current_uncertainity)
                if gain>=case1:
                    case1, best_question = gain, query
        return case1, best_question
def gini_index(X, y):
        counts = nb_counts(X, y)
        ind = 1
        for label in counts:
            label_probability = counts[label] / float(len(X))
            ind -= label_probability ** 2
        return ind
    
def gini_gain(X_left, X_right, y_left, y_right, current_uncertainity):
        p = float(len(X_left)) / (len(X_left) + len(X_right))
        return current_uncertainity - p * gini_index(X_left, y_left) - (1 - p) * gini_index(X_right, y_right)
