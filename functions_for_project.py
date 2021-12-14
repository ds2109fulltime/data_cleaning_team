
def get_n_of_sales_by_cat(df, col1, col2):
    ''' 
    params: df-> dataframe name, col1 -> column that you want to groupby, could be country, state, product, col2 -> column which will indicate a number of sales.  
    Then it will sort values by descending order, from most to least, and top 10. 
    It will create another dataframe that will show col1, column you want to groupby, 
    col2 is the number of sales based on col1 groupby
    '''
    get_n_of_by_cat = df[[col1,col2]].groupby([col1]).count().sort_values(col2, ascending=False).head(10)
    get_n_of_by_cat = get_n_of_by_cat.rename(columns={col2: 'Number of Sales'})
    get_n_of_by_cat = get_n_of_by_cat.reset_index()
    get_n_of_by_cat

    return get_n_of_by_cat


import calendar
def from_month_into_to_name(df, col1): 
    '''
    Params: dataframe, and col1 should be month, in datatime format
    It will return a values of Month in name format for example, 03 -> March 
    
    '''
    df[col1] = df[col1].apply(lambda x: calendar.month_abbr[x])
    return df


from itertools import combinations
from collections import Counter
def get_products_that_are_sold_together(df, order_id_column, product_column, products_bought_together_column):
    '''
    This function will return a dataframe along with number of transactions of products
    that were purchased together. 

    params: 
        df -> is the dataframe that will be used 
        order_id_column -> is the transaction id, could be order ID. 
        product_column -> is the column for products 
        products_bought_together_column -> the column that will two products purchased together

    '''
    # creating a new dataframe to separate duplicates from Order ID
    df_updated = df[df[order_id_column].duplicated(keep=False)]
    #Joining the products with the same Order ID group to be on the same line 
    df_updated[products_bought_together_column] = df_updated.groupby(order_id_column)[product_column].transform(lambda x: ','.join(x))
    #Getting rid of the duplicate values 
    df_updated = df_updated[[order_id_column, products_bought_together_column]].drop_duplicates()


    count = Counter()

    for row in df_updated[products_bought_together_column]:
        row_list = row.split(',')
        count.update(Counter(combinations(row_list,2)))

    # Below Will return products bought together along with the number of transactions
    products_bought_together = count.most_common(20)

    return products_bought_together



