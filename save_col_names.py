"""
Save the names of columns in a dataframe and export it to csv.
"""
#Libraries:
import pandas as pd
#
#Body of the function:
#
def save_col_names(data):
    """
    Save the names of the columns of a given dataset in a dataframe and export it to csv. 
    Arguments: data --> the given dataframe
    Return: The new dataframe containing the column names.
    """   
    column_names = pd.DataFrame({'Names':data.columns})   # Creates a dataframe with the column names
    column_names.to_csv('column_names.csv', sep = ';')   # Exports the column names to csv

    return column_names


