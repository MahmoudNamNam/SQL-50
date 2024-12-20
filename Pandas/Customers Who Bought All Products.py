import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Get the total number of products
    total_products = product['product_key'].nunique()

    # Step 2: Count distinct products bought by each customer
    customer_products = customer.groupby('customer_id')['product_key'].nunique()

    # Step 3: Filter customers who bought all products
    result = customer_products[customer_products == total_products].index

    return pd.DataFrame({'customer_id': result})


data = [[1, 5], [2, 6], [3, 5], [3, 6], [1, 6]]
customer = pd.DataFrame(data, columns=['customer_id', 'product_key']).astype({'customer_id':'Int64', 'product_key':'Int64'})
data = [[5], [6]]
product = pd.DataFrame(data, columns=['product_key']).astype({'product_key':'Int64'})

print(find_customers(customer, product))