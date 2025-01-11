import pandas as pd

def price_at_given_date(products: pd.DataFrame, given_date: str = '2019-08-16') -> pd.DataFrame:
    # Filter for changes on or before the given date
    filtered_products = products[products['change_date'] <= given_date]
    
    # Get the latest price for each product
    latest_prices = (
        filtered_products.sort_values(by='change_date', ascending=False)
        .drop_duplicates(subset='product_id', keep='first')
        .set_index('product_id')['new_price']
    )
    
    # Create a complete product list and fill missing prices with 10
    all_products = pd.DataFrame({'product_id': products['product_id'].unique()})
    all_products['price'] = all_products['product_id'].map(latest_prices).fillna(10)
    
    return all_products


data = [[1, 20, '2019-08-14'], [2, 50, '2019-08-14'], [1, 30, '2019-08-15'], [1, 35, '2019-08-16'], [2, 65, '2019-08-17'], [3, 20, '2019-08-18']]
products = pd.DataFrame(data, columns=['product_id', 'new_price', 'change_date']).astype({'product_id':'Int64', 'new_price':'Int64', 'change_date':'datetime64[ns]'})


print(price_at_given_date(products, '2019-08-16'))