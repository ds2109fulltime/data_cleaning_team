import pandas as pd
import numpy as np
import os 

def replace_string(df, col, string_list, replacement):
    '''
    Run through list of strings to replace for a value
    df: pandas Dataframe
    col: replaced column
    string_list: list of strings to be runned
    replacement: new value
    '''

    for pos, val in enumerate(string_list):
        df[col] = df[col].str.replace(string_list[pos], replacement)