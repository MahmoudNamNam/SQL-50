import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    return (
        register.groupby("contest_id", as_index=False)
        .agg(percentage=("user_id", lambda x: len(x) / len(users) * 100))
        .sort_values(by=["percentage", "contest_id"], ascending=[False, True])
        .round(2)
    )