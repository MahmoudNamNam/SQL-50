import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # Calculate the rank of each order for a customer based on the order date (1 = earliest order).
    delivery['rank'] = delivery.groupby('customer_id')['order_date'].rank(method='dense', ascending=True)
    delivery = delivery[delivery['rank'] == 1]
    
    # indicate if the order was delivered on the customer's preferred delivery date.
    delivery['status'] = delivery.apply(lambda x: 1 if x['order_date'] == x['customer_pref_delivery_date'] else 0, axis=1)
    
    total_immdiate = delivery['status'].sum()
    
    immediate_percentage = round(total_immdiate / delivery.shape[0] * 100, 2)
    res = pd.DataFrame([immediate_percentage], columns=['immediate_percentage'])
    
    return res
