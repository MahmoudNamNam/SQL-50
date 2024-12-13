import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    follower_counts = followers.groupby('user_id')['follower_id'].count().reset_index()
    follower_counts.rename(columns={'follower_id': 'followers_count'}, inplace=True)

    follower_counts = follower_counts.sort_values(by='user_id')
    return follower_counts