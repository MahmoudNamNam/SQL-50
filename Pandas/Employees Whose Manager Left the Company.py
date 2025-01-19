import pandas as pd

data = [[3, 'Mila', 9, 60301], [12, 'Antonella', None, 31000], [13, 'Emery', None, 67084], [1, 'Kalel', 11, 21241], [9, 'Mikaela', None, 50937], [11, 'Joziah', 6, 28485]]
employees = pd.DataFrame(data, columns=['employee_id', 'name', 'manager_id', 'salary']).astype({'employee_id':'Int64', 'name':'object', 'manager_id':'Int64', 'salary':'Int64'})


def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
        return employees[employees.salary.lt(30_000) & employees.manager_id.notna() & ~employees.manager_id.isin(employees.employee_id)][['employee_id']].sort_values('employee_id')


print(find_employees(employees))