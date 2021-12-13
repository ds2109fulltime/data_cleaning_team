"""
Function to deal with missing values in dataframes
"""
#Libraries:
import pandas as pd
#
#Body of the function:
#
def missing_values(data, method = 'drop', column_names = None):
    """
    Function to deal with missing values in dataframes. Three different options: 1 - Drop the rows with missing values, 
    2 - Fill the missing values with zeros, 3 - Fill the missing values with the average of the column values.
    Arguments: data --> the given dataframe // method --> 'drop' : drop the missing values, 'zero' : fill with zeros, 'avg' : fill with the average
    Default: 'drop' // column_names --> the columns to take into account
    Return: The resulting dataframe.
    """   
    if method == 'drop':
        df_res = data.dropna(subset = column_names)   # Drop the rows with missing values in the given columns
    elif method == 'zero':
        for name in column_names:
            data[name] = data[name].fillna(0)    # Fill missing values with zeros
        df_res = data
    else:
        for name in column_names:
            data[name] = data[name].fillna(data[name].mean())   # Fill missing values with the average
        df_res = data  

    return df_res       
