import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue = queue.sort_values('turn')
    queue['cumulative_weight'] = queue['weight'].cumsum()
    valid = queue[queue['cumulative_weight'] <= 1000]
    last_turn_idx = valid['turn'].idxmax()
    name = valid.loc[last_turn_idx, 'person_name']
    
    return pd.DataFrame({'person_name': [name]})


