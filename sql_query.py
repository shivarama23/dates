import cx_Oracle

# Connect to the Oracle database
connection = cx_Oracle.connect("username", "password", "hostname:port/service_name")

# Create a cursor object
cursor = connection.cursor()

# Define the SQL statement to insert a row
insert_row_sql = """
    INSERT INTO employees (employee_id, first_name, last_name, hire_date, salary)
    VALUES (:employee_id, :first_name, :last_name, :hire_date, :salary)
"""

# Define the data for the row to be inserted
employee_data = {
    "employee_id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "hire_date": "2023-07-06",
    "salary": 5000
}

# Execute the SQL statement to insert the row
cursor.execute(insert_row_sql, employee_data)

# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

