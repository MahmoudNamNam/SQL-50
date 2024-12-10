import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:

        # Add rank based on the first year of sales per product
    sales['rank'] = sales.groupby('product_id')['year'].rank(method='min', ascending=True)
    
    # Filter rows where rank == 1
    res = (
        sales.loc[sales['rank'] == 1, ['product_id', 'year', 'quantity', 'price']]
        .rename(columns={'year': 'first_year'})
    )
    return res