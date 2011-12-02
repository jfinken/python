#!/usr/bin/python
import psycopg2
import sys

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

    type = 'good'
    if len(sys.argv) < 3:
        print "\nUsage: pre_proc_report [dmr_id] [good, filtered, or bad]\n"
        exit() 

    dmr_id = sys.argv[1]
    type = sys.argv[2]

    #Define our connection string
    conn_process = "host='localhost' dbname='process' user='postgres' password='earthuser'"
    # print the connection string we will use to connect
    #print "Connecting to database\n ->%s" % (conn_process)

    panos = []
    try:
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_process)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor_process = conn.cursor()
        #print "Connected!\n"

        if type == 'good':
            dmr_query = "SELECT b.gps_week as gps_week, b.gps_millisecs as gps_millisecs, x(b.geometry) as xx, y(b.geometry) as yy, z(b.geometry) as zz FROM cap_event b, session c WHERE b.session_id=c.session_id and c.dmr='%s' AND b.proc_ignore='f' AND b.bad_position='f' and b.quality > '1' AND c.track_status='TRUE' AND c.verified='TRUE' AND toprocess='TRUE' ORDER BY b.cap_id;" % dmr_id
        elif type == 'filtered':
            dmr_query = "SELECT b.gps_week as gps_week, b.gps_millisecs as gps_millisecs, x(b.geometry) as xx, y(b.geometry) as yy, z(b.geometry) as zz FROM cap_event b, session c WHERE b.session_id=c.session_id and c.dmr='%s' AND b.proc_ignore='f' AND b.bad_position='f' and b.quality > '1' AND c.track_status='TRUE' AND c.verified='TRUE' AND toprocess='FALSE' ORDER BY b.cap_id;" % dmr_id
        elif type == 'bad':
            dmr_query = "SELECT b.gps_week as gps_week, b.gps_millisecs as gps_millisecs, x(b.geometry) as xx, y(b.geometry) as yy, z(b.geometry) as zz FROM cap_event b, session c WHERE b.session_id=c.session_id and c.dmr='%s' and (b.proc_ignore='t' OR b.bad_position='t' OR b.quality = '1' OR c.track_status='FALSE' OR c.verified='FALSE') AND toprocess='FALSE' ORDER BY b.cap_id;" % dmr_id

        cursor_process.execute(dmr_query)
        records = cursor_process.fetchall()

        for row in records:
            print row

        # print out the records using pretty print
        # note that the NAMES of the columns are not shown, instead just indexes.
        # for most people this isn't very useful so we'll show you how to return
        # columns as a dictionary (hash) in the next example.
        #pprint.pprint(records)
        
        #panos.append( parse_pano_record(pano_record[0]) )

        #FILE = open("darsh_nt_metadata.csv", "w")
        #FILE.writelines(panos)


    except:
        # Get the most recent exception
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        # Exit the script and print an error telling what happened.
        sys.exit("Something failed!\n ->%s" % (exceptionValue))

if __name__ == "__main__":
    sys.exit(main())

