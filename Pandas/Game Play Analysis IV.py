import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Use .transform(min) to assign the first login date to all rows of that player
    activity["first"] = activity.groupby("player_id").event_date.transform(min)

    # Add 1 day to the 'first' login date and compare it with 'event_date'
    activity_2nd_day = activity.loc[activity["first"] + pd.DateOffset(1) == activity["event_date"]]

    # activity.player_id.nunique(): Total number of unique players
    return pd.DataFrame({"fraction": [round(len(activity_2nd_day) / activity.player_id.nunique(), 2)]})
