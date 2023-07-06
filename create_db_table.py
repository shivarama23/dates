import cx_Oracle

# Connect to the Oracle database
connection = cx_Oracle.connect("username", "password", "hostname:port/service_name")

# Create a cursor object
cursor = connection.cursor()

# Define the SQL statement to create the table
create_table_sql = """
    CREATE TABLE employees (
        employee_id NUMBER,
        first_name VARCHAR2(50),
        last_name VARCHAR2(50),
        hire_date DATE,
        salary NUMBER
    )
"""

# Execute the SQL statement to create the table
cursor.execute(create_table_sql)

# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
