import numpy as np

def outliers (df, feature):
    '''
    Function that removes outliers from the given column. 
    Arguments: the Dataframe and the column you want to modify.
    '''
    mean = df[feature].mean() 
    std = df[feature].std() 
    values = []
    for i in df[feature]:
        if i >= (mean + (2*std)):
            i == mean
        values.append(i)
    return values


#...........................

import sys, os

def get_root_path(n):
    '''
    This function allows us to iterate over folders to add the path of our root folder
    Arguments:
    - n (int): the number of times we will iterate to reach the desired folder
    '''
    path = os.path.dirname(os.path.abspath(__file__)) #__file__ --> para .py
    for i in range(n):
        path = os.path.dirname(path)
    print(path)
    sys.path.append(path)

get_root_path(n=1)

#...........................

