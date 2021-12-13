
def get_n_of_sales_by_cat(df3, col1, col2):
    '''' This function will return a new dataframe based on the number of sales by col1. It will return the highest number. It could be based on a product, STATE or even a country. Then it will sort values by descending order, from most to least, and top 10 '''
    counted_by_cat = df3[[col1,col2]].groupby([col1]).count().sort_values(col2, ascending=False).head(10)
    counted_by_cat = counted_by_cat.rename(columns={col2: 'Number of Sales'})
    counted_by_cat = counted_by_cat.reset_index()
    counted_by_cat

    return counted_by_cat


import calendar
def from_month_into_to_name(df):
    '''This function will convert an integer of a month to a name, for example, lets say it is March, by default it will return 03, this function will make it as "MAR" as name. '''
    df['Month'] = df['Month'].apply(lambda x: calendar.month_abbr[x])
    return df


