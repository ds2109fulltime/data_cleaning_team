def percentage(df,column):
        
    '''
    This functions become your column with % to decimal column of your dataframe.
    
    df: dataframe
    column: column to be represented.
    '''

    import pandas as pd
    x = df[column].str.replace('%', '').astype(float)
    df[column] = x/100
    return df[column]