

def merge_df(df_0, df_1, df_2, df_3, how, on):
    '''Función para unificar 4 DataFrames
    df_n = Cada uno de los Data Frames
    how = forma en las que se van a unir
    on = nivel o lista
    '''
    import pandas as pd
    df3 = pd.merge(df_1, df_2, how, on)
    df = pd.merge(df3, df_0, how, on)
    return df