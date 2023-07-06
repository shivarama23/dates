import cx_Oracle

# Connect to the Oracle database
connection = cx_Oracle.connect("username", "password", "hostname:port/service_name")

# Create a cursor object
cursor = connection.cursor()

# Define the SQL statement to delete the table
delete_table_sql = "DROP TABLE employees"

# Execute the SQL statement to delete the table
cursor.execute(delete_table_sql)

# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
