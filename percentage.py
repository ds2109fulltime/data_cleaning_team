def percentage(data,column):
        
    '''
    This functions become your column with % to decimal column of your data.
    
    data: dataframe
    column: column to be represented.
    '''

    import pandas as pd
    x = data[column].str.replace('%', '').astype(float)
    data[column] = x/100
    return data[column]