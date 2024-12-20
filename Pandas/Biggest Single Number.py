import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    counts = my_numbers['num'].value_counts()
    single_nums = counts[counts==1].index
    largest_single_number = max(single_nums) if len(single_nums) > 0 else None

    return pd.DataFrame({'num': [largest_single_number]})
