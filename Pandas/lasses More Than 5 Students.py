import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class')['student'].size().reset_index()
    df=df[df['student'] >= 5][["class"]]
    return df


data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})


print(find_classes(courses))


import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:

    grp = courses.groupby('class')['student'].apply(len).reset_index()

    return grp[grp.student >= 4].iloc[:,[0]]