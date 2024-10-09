import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:

    examination_count = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name = 'attended_exams')

    student_subject = pd.merge(students, subjects, how = 'cross')

    result_df = pd.merge(student_subject, examination_count, on = ['student_id', 'subject_name'], how = 'left')

    result_df = result_df[['student_id', 'student_name','subject_name', 'attended_exams']].sort_values(by = ['student_id', 'subject_name'])


    result_df['attended_exams'] = result_df['attended_exams'].fillna(0)


    return result_df    

data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype({'student_id':'Int64', 'student_name':'object'})
data = [['Math'], ['Physics'], ['Programming']]
subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name':'object'})
data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype({'student_id':'Int64', 'subject_name':'object'})

print(students_and_examinations(students,subjects,examinations))