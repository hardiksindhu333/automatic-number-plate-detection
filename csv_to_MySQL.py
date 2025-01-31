import mysql.connector

# Database connection details
db_config = {
    "host": "localhost",  # Replace with your MySQL server host
    "user": "root",       # Your MySQL username
    "password": "your_password",  # Your MySQL password
    "database": "parking_system"  # The database you want to use
}

try:
    # Establish the connection
    connection = mysql.connector.connect(**db_config)
    
    if connection.is_connected():
        print("Connected to the database!")
        
        # Create a cursor object to execute queries
        cursor = connection.cursor()
        
        # Example query to test the connection
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("Tables in the database:")
        for table in tables:
            print(table)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Database connection closed.")
        
        
        
        
        
        
        
        
        
        
# import csv
# import mysql.connector

# # Connect to MySQL
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="your_password",
#     database="parking_system"
# )

# cursor = db.cursor()

# # Open the CSV file
# with open('interpolate(1).csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         license_plate = row['license_number']
#         # Insert data into the table
#         cursor.execute("""
#             INSERT INTO booked_slots (license_plate)
#             VALUES (%s)
#         """, (license_plate,))
        
# # Update slot numbers
# cursor.execute("UPDATE booked_slots SET slot_number = id")

# db.commit()
# db.close()
