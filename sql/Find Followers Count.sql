select user_id,count(distinct follower_id) followers_count
from Followers
group by 1