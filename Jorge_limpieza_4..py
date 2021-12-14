def drop_NaN(df, df_column):
    '''This function eliminates the NaN values of a specific column
    Los parámetros que necesitamos son:
    df = DataFrame
    df_column = columna de la que queremos eliminar los valorers NaN
    '''
    import numpy as np
    df_column.replace(0,np.nan)
    df.dropna(axis=0, implace=True)