import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    # Group employees by their manager to calculate the count of reports and the average age
    by_manager = employees.groupby("reports_to", as_index=False).agg(
        reports_count=("employee_id", "size"),  # Count of reports per manager
        average_age=("age", "mean"),  # Average age of reports
    )

    # Adjust for banker's rounding by adding a very small number before rounding
    by_manager["average_age"] = (by_manager["average_age"] + 1e-12).round(0)

    # Merge the aggregated data with the original employees DataFrame to get the names of managers
    merged = by_manager.merge(
        employees[["employee_id", "name"]],
        how="left",
        left_on="reports_to",
        right_on="employee_id",
    )

    merged.rename(
        columns={
            "employee_id_y": "employee_id", 
        },
        inplace=True,
    )

    final_output = merged[["employee_id", "name", "reports_count", "average_age"]]

    return final_output
