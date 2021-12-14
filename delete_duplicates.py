"""
Delete duplicated values in pandas Dataframe
"""
#Libraries:
import pandas as pd
import numpy as np
#
#Body of the function:
#
def delete_duplicates(data, column_names = None):
    """
    Delete the rows with duplicated values in a dataframe. Arguments: data --> dataframe, column_names --> names of the columns to take into account.
    Returns the dataframe without the duplicated values and prints the number of deleted rows.
    """   
    quant_dup_rows = np.size(data[data.duplicated(subset= column_names)].index)  # Get the number of duplicated rows
    print(f"{quant_dup_rows} rows have been deleted")   # Print the number of duplicated rows

    return data.drop_duplicates(subset= column_names)



