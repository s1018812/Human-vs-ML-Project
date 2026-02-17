# Run --> pip install ucimlrepo
# Run --> pip install seaborn
from ucimlrepo import fetch_ucirepo
import pandas as pd
# import matplotlib.pyplot as plt
# import os

def load_mushroom_data(): 

    # Copied precisely from the UCI Machine Learning Repository package documentation

    # fetch dataset 
    mushroom = fetch_ucirepo(id=73) 

    # data (as pandas dataframes) 
    X = mushroom.data.features 
    y = mushroom.data.targets 

    # metadata 
    # print(mushroom.metadata) 

    # # variable information 
    # print(mushroom.variables) 

    # ---------------------------------------------------------------------

    feature_names = mushroom.variables[mushroom.variables['role'] == 'Feature']['name'].tolist()
    target_name = mushroom.variables[mushroom.variables['role'] == 'Target']['name'].values[0]

    df = pd.DataFrame(mushroom.data.features, columns=feature_names)
    df[target_name] = mushroom.data.targets

    # I printed here to confirm that I was importing data correctly.
    # print(df.head(20))

    return df, target_name
