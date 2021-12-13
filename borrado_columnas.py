import pandas as pd
import numpy as np
import os 
def borrado_columnas(df,col):
    '''
    Deleting columns and automatically saving the dataframe
    
    df:pandas Dataframe
    col: column to delete
    axis:1
    inplace:True'''
    df.drop(col,axis=1,inplace=True)