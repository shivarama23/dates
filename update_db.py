import cx_Oracle

# Connect to the Oracle database
connection = cx_Oracle.connect("username", "password", "hostname:port/service_name")

# Create a cursor object
cursor = connection.cursor()

# Define the SQL statement to update multiple cells
update_row_sql = """
    UPDATE employees
    SET first_name = :new_first_name, salary = :new_salary
    WHERE employee_id = :employee_id
"""

# Define the data for the update
employee_id = 1
new_first_name = "John"
new_salary = 6000

# Execute the SQL statement to update the row
cursor.execute(update_row_sql, new_first_name=new_first_name, new_salary=new_salary, employee_id=employee_id)

# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
