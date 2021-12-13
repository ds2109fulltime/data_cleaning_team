import pandas as pd

def split_datetime(df, column, only_date = False):
    
    '''
    This function receives a dataframe with a column with values 'datetime' look like but in 'object' format and transforms it
    into 'datetime' format and divide every component in different columns to operate with the values. In that way, we will
    have days, months, years, hours and minutes in different columns.
    Parameters:
    - df: dataframe
    - column: dataframe's column with the values we want to transform. Tendrá la forma 'df[datetime]'
    - only_date: 'True' if there isn't time and 'False' if there is date and time in the column.
    '''
    column = pd.to_datetime(column)
    time = pd.DataFrame(column)

    time['day'] = column.dt.day
    time['month'] = column.dt.month
    time['year'] = column.dt.year
    time['weekday'] = column.dt.weekday

    if only_date == False:
        time['hour'] = column.dt.hour
        time['minutes'] = column.dt.minute
    
    df = pd.concat([df, time], axis = 1)
    df = df.loc[:,~df.columns.duplicated(keep='last')]
    
    return df


#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------
