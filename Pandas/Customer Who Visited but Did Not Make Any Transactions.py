import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(visits, transactions, on='visit_id', how='left')
    # Filter rows where transaction_id is NaN (i.e., no transaction occurred)
    no_trans_df = merged_df[merged_df['transaction_id'].isna()]
    return no_trans_df.groupby('customer_id').size().reset_index(name='count_no_trans')
