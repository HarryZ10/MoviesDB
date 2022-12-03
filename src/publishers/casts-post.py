import psycopg2 as pg
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Connect to the database
conn = pg.connect(
    host=os.environ.get("PG_HOST"),
    database=os.environ.get("PG_DB"),
    user=os.environ.get("PG_USER"),
    password=os.environ.get("PG_PASS")
)

# Create a cursor to perform database operations
cur = conn.cursor()

# Open the file for reading
ppl_path = os.path.join(os.path.dirname(__file__), "casts124.xml.csv")
f = open(ppl_path, "r")

# Read the first line (column names)
line = f.readline()

# Read the rest of the lines
for line in f:
    # Split the line into a list of strings
    fields = line.split(',')
    # Remove the newline character from the last field
    fields[-1] = fields[-1].strip()

    print(fields)
    # Insert the record into the database

    cur.execute("""
        INSERT INTO casts (dir_id,dir_lname,movie_id,movie_title,actor_name,role_name,award)
        VALUES (%s, %s, %s, %s, %s, %s, %s)""", fields)
    
    # Commit the changes to the database
    conn.commit()

# Close the cursor
cur.close()

# Close the connection
conn.close()

# Close the file
f.close()
