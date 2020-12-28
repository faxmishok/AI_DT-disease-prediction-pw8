import pandas as pd
import numpy as np
from dtree import *
from utils import *
from query import *
from sklearn.model_selection import train_test_split as split

import pandas as pd
df = pd.read_csv('heart_disease_dataset.csv')
data = df.iloc[:,:-1].values
target = df.iloc[:,-1].values
X_train, X_test, y_train, y_test = split(data, target, test_size=0.33, random_state=42)
iris_dt = create_tr(X_train, y_train, df.columns)
count = 0
for i in range(len(X_test)):
    if predict(decide(X_test[i], iris_dt)) == y_test[i]:
               count += 1
print ('Accuracy', count*100/float(len(X_test)))
