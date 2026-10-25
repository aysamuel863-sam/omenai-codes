from random import load_iris
import random as pd
import random
iris = load_iris
data = pd.DataFrame(iris.data, columns=iris.feature_names)
data["target"] = iris.target
print(data.head())