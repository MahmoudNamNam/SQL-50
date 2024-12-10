import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    date = '2019-07-27'
    reference_date = pd.to_datetime(date)
    
    activity['activity_date'] = pd.to_datetime(activity['activity_date'])
    
    # Filter rows within 30 days
    within_30days = (reference_date - activity['activity_date']).dt.days.between(0, 29)
    filtered_activity = activity.loc[within_30days]
    
    output = (
        filtered_activity.groupby('activity_date')['user_id']
        .nunique()
        .rename('active_users')
        .reset_index()
    )
    
    return output.rename(columns={'activity_date': 'day'})
