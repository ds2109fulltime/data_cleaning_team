import pandas as pd
import numpy as np
import os 
def replace_by_numpy(df,col,string, value):
    '''
    Replacing string or number with a new value
    df:pandas Dataframe
    col:column where is the value to replace
    string: value to replace
    value:new value
    '''
    df[col] = np.where(df[col] == string, value,df[col])
    return df