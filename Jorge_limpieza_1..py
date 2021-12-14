def numeric(columns, df):
    '''Esta función es para cambiar los valores categóricos a valores numéricos de una columna concreta
    Los parámetros son:
    columns = columna a modificar
    df = DataFrame
    '''
    from sklearn import preprocessing
    le = preprocessing.LabelEncoder()
    for i in columns:
        le.fit(df[i])
        df[i] = le.transform(df[i])
    return columns
