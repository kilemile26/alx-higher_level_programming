#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa in
ascending order by their ids and using 'format' to create the
SQL query with the user input.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if three arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Get credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to select all states, ordered by id
    query = "SELECT * FROM states" \
    "WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
