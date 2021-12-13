

def df_informacion(df):
    '''Finción para ver toda la información del DataFrame
    '''
    print(df.info())
    print(df.describe())
    print(df.corr())
    print(df.head())