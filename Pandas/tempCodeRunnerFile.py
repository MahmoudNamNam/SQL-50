def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    pivot_table = examinations.pivot_table(index='student_id', columns='subject_name', aggfunc='size', fill_value=0)
    pivot_table_stacked = pivot_table.stack().reset_index()
    pivot_table_stacked.columns = ['student_id', 'subject_name', 'attended_exams']

    result = pd.merge(students, pivot_table_stacked, how='left', on='student_id')

    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)

    result = result.sort_values(by=['student_id', 'subject_name']).reset_index(drop=True)

    return result
