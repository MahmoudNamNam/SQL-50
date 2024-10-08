import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values(by='recordDate')
    weather['prev_recordDate'] = weather['recordDate'].shift(1)
    weather['prev_temp'] = weather['temperature'].shift(1)
    return weather[
        (weather['recordDate'] - weather['prev_recordDate'] == pd.Timedelta(days=1)) &
        (weather['temperature'] > weather['prev_temp'])
        ][['id']]






data = [[1, '2015-01-01', 10], [2, '2015-01-02', 25], [3, '2015-01-03', 20], [4, '2015-01-04', 30]]
weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype({'id':'Int64', 'recordDate':'datetime64[ns]', 'temperature':'Int64'})

print(rising_temperature(weather))