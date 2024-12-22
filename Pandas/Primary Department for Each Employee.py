import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where primary_flag is 'Y'
    filtered_by_flag = employee.loc[employee['primary_flag'] == 'Y', ['employee_id', 'department_id']]
    
    # Find employees who are in only one department
    unique_employees = employee[employee.groupby('employee_id')['employee_id'].transform('count') == 1][['employee_id', 'department_id']]
    
    # Combine the filtered dataframes
    combined = pd.concat([filtered_by_flag, unique_employees])
    
    # Remove duplicate rows
    combined = combined.drop_duplicates()
    
    # Reset the index of the dataframe
    combined = combined.reset_index(drop=True)
    
    return combined

# Sample data
data = [['1', '1', 'N'], ['2', '1', 'Y'], ['2', '2', 'N'], ['3', '3', 'N'], ['4', '2', 'N'], ['4', '3', 'Y'], ['4', '4', 'N']]
employee = pd.DataFrame(data, columns=['employee_id', 'department_id', 'primary_flag']).astype({'employee_id':'Int64', 'department_id':'Int64', 'primary_flag':'object'})

# Print the result of the function
print(find_primary_department(employee))