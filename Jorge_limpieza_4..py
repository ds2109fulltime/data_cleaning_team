df_str = df[['pclass', 'survived', 'sibsp', 'parch', 'age', 'fare', 'body']]
def drop_NaN(df, column):
    '''This function eliminates the NaN values of a specific column
    Los parámetros que necesitamos son:
    df = DataFrame
    df_column = columna de la que queremos eliminar los valorers NaN
    '''
    import numpy as np
    import pandas as pd
    column.replace(0,np.nan)
    df.dropna(axis=0, inplace=True)
drop_NaN(df=df, column=df['body'])