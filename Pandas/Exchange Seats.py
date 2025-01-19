import pandas as pd


data = [[1, 'Abbot'], [2, 'Doris'], [3, 'Emerson'], [4, 'Green'], [5, 'Jeames']]
seat = pd.DataFrame(data, columns=['id', 'student']).astype({'id':'Int64', 'student':'object'})


def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    for i in range(1, len(seat), 2):
        seat.loc[i-1,"student"], seat.loc[i,"student"] = seat.loc[i,"student"], seat.loc[i-1,'student']
    return seat
print(exchange_seats(seat))