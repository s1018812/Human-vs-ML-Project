# Run --> pip install ucimlrepo
# Run --> pip install seaborn
from ucimlrepo import fetch_ucirepo
import pandas as pd
# import matplotlib.pyplot as plt
# import os

# Copied precisely from the UCI Machine Learning Repository package documentation

# fetch dataset 
mushroom = fetch_ucirepo(id=73) 

# data (as pandas dataframes) 
X = mushroom.data.features 
y = mushroom.data.targets 

# metadata 
print(mushroom.metadata) 

# variable information 
print(mushroom.variables) 