import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:

    def find_average_price(df : pd.DataFrame) -> float:
        output = ( (df['units'] * df['price']).sum() / df['units'].sum() ).__round__(2)
        
        return output if pd.notna(output) else 0.00
    
    return ( prices.merge(right=units_sold, how='left', on='product_id')
            .query("(start_date <= purchase_date) & (end_date >= purchase_date) | (purchase_date.isna())")
            .groupby(by='product_id')
            .apply(func=find_average_price, include_groups=False)
            .rename("average_price")
            .reset_index()
           )

# Example usage
data = [[1, '2019-02-17', '2019-02-28', 5], [1, '2019-03-01', '2019-03-22', 20], [2, '2019-02-01', '2019-02-20', 15], [2, '2019-02-21', '2019-03-31', 30], [3, '2019-02-21', '2019-03-31', 30]]
prices = pd.DataFrame(data, columns=['product_id', 'start_date', 'end_date', 'price']).astype({'product_id':'Int64', 'start_date':'datetime64[ns]', 'end_date':'datetime64[ns]', 'price':'Int64'})
data = [[1, '2019-02-25', 100], [1, '2019-03-01', 15], [2, '2019-02-10', 200], [2, '2019-03-22', 30]]
units_sold = pd.DataFrame(data, columns=['product_id', 'purchase_date', 'units']).astype({'product_id':'Int64', 'purchase_date':'datetime64[ns]', 'units':'Int64'})

print(average_selling_price(prices, units_sold))
