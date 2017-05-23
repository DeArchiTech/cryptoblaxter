import psycopg2 as db
import csv

try:
    # Open Postgres Connection
    conn = dp.connect("dbname='cryptoblaxter' user='davix' host='localhost' password='giovanni1013'")
    cur = conn.cursor()

    # 1 Create a new Table
    fieldnames = ['Name', 'Address', 'City', 'State']
    sql_table = 'CREATE TABLE TableName (%s)' % ','.join('%s VARCHAR(50)' % name for name in fieldnames)
    cur.execute(sql_table)

    # 2 Open CSV File
    csvObject = csv.reader(open(r'/Users/davix/Source/cryptoblaxter/data', 'r'), dialect='excel', delimiter=',')

    # 3 Insert into the table plus one field called file Name, one field for coin type
    passData = "INSERT INTO TableName (param1, param2, param3, param4, param5) VALUES (%s,%s,%s,%s,%s);"

    for row in csvObject:
        csvLine = row
        cur.execute(passData, csvLine)

    conn.commit()

except:
    print "I am unable to connect to the database"

#1) Function that takes a csv file name as input, and insert into database and spending one column, file_name
#2) Function that takes a directory name as input, and insert all csv files into database
