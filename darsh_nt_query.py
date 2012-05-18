#!/usr/bin/python
import psycopg2
import sys
import csv

def parse_pano_record(pano):
    res = []
    for field in pano:
        res.append(str(field) +'|')

    # trim off the last bar
    line = ''.join(res)[:-1]
    line += '\n'
    return line

def main():
    #start of script

    if len(sys.argv) < 2:
        print "\nUsage: darsh_path\\to\\csv_file\n"
        exit() 

    csv_file = sys.argv[1]
    reader = csv.reader(open(csv_file, 'rb'))
    print "Num rows in csv: %i" % reader.line_num

    #Define our connection string
    conn_process = "host='localhost' dbname='process' user='postgres' password='earthuser'"
    conn_staging = "host='localhost' dbname='staging' user='postgres' password='earthuser'"
    # print the connection string we will use to connect
    print "Connecting to database\n ->%s" % (conn_process)
    print "Connecting to database\n ->%s" % (conn_staging)

    panos = []
    try:
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_process)
        conn2 = psycopg2.connect(conn_staging)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor_process = conn.cursor()
        cursor_staging = conn2.cursor()
        print "Connected!\n"

        for row in reader:
            # get pano_id given the cap_id, effectively a join
            query = "SELECT pano_id FROM cap_process where cap_id='%s';" % row[0]
            cursor_process.execute(query)

            # retrieve the records from the database
            records = cursor_process.fetchall()
            pano_id = records[0]
            # got pano id, get record from pano
            # print "Retrieved pano_id: %s" % pano_id
            pano_query = "SELECT pano_id, x(ST_Transform(geometry,(SELECT utmzone(geometry)))), y(ST_Transform(geometry,(SELECT utmzone(geometry)))), Z(geometry), yaw, pitch, roll,global_stddev,timestamp,avg_intensity,cap_interval FROM pano where pano_id='%s';" % pano_id
            cursor_staging.execute(pano_query)
            pano_record = cursor_staging.fetchall()

            # print out the records using pretty print
            # note that the NAMES of the columns are not shown, instead just indexes.
            # for most people this isn't very useful so we'll show you how to return
            # columns as a dictionary (hash) in the next example.
            #pprint.pprint(records)
            panos.append( parse_pano_record(pano_record[0]) )

        FILE = open("darsh_nt_metadata.csv", "w")
        FILE.writelines(panos)


    except:
        # Get the most recent exception
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        # Exit the script and print an error telling what happened.
        sys.exit("Something failed!\n ->%s" % (exceptionValue))

if __name__ == "__main__":
    sys.exit(main())

