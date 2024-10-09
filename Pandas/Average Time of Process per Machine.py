import pandas as pd

def get_average_time(df: pd.DataFrame) -> pd.DataFrame:
    start_times = df[df['activity_type'] == 'start'].copy()
    end_times = df[df['activity_type'] == 'end'].copy()
    start_times.rename(columns={'timestamp': 'start_time'}, inplace=True)
    end_times.rename(columns={'timestamp': 'end_time'}, inplace=True)
    merged = pd.merge(start_times, end_times, on=['machine_id', 'process_id'])

    merged['process_time'] = merged['end_time'] - merged['start_time']

    result = merged.groupby('machine_id')['process_time'].mean().reset_index()

    result['processing_time'] = result['process_time'].round(3)

    final_result = result[['machine_id', 'processing_time']]

    return final_result


data = [[0, 0, 'start', 0.712], [0, 0, 'end', 1.52], [0, 1, 'start', 3.14], [0, 1, 'end', 4.12], [1, 0, 'start', 0.55], [1, 0, 'end', 1.55], [1, 1, 'start', 0.43], [1, 1, 'end', 1.42], [2, 0, 'start', 4.1], [2, 0, 'end', 4.512], [2, 1, 'start', 2.5], [2, 1, 'end', 5]]
activity = pd.DataFrame(data, columns=['machine_id', 'process_id', 'activity_type', 'timestamp']).astype({'machine_id':'Int64', 'process_id':'Int64', 'activity_type':'object', 'timestamp':'Float64'})

print(get_average_time(activity))