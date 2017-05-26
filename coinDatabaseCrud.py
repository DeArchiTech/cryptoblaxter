import psycopg2 as db

try:
    # Open Postgres Connection
    conn = db.connect("dbname='cryptoblaxter' user='davix' host='localhost'")
    cur = conn.cursor()
    print("Shit Works")

except:
    print("I am unable to connect to the database")

