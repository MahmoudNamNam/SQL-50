import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    managers_counts = employee.groupby('managerId').size().reset_index(name='employee_count')
    managers_with_five_or_more = managers_counts[managers_counts['employee_count'] >= 5]

    return pd.merge(employee, managers_with_five_or_more, left_on='id', right_on='managerId')[['name']]

data = [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101], [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]]
employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})

print(find_managers(employee))