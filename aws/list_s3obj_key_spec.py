import boto
import boto.s3.connection
import uuid

def main():

    import argparse
 
    parser = argparse.ArgumentParser()
    parser.add_argument('--bucket')
    parser.add_argument('--key')
    args = parser.parse_args()

    conn = boto.connect_s3(
        #aws_access_key_id = access_key,
        #aws_secret_access_key = secret_key,
        host = 's3.amazonaws.com',
        #is_secure=False,               # uncommmnt if you are not using ssl
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

    bucket = conn.get_bucket(args.bucket)
  
    keys = ['432eea6a',
    '2c65db5a',
    'c2f11bed',
    '6bdc1526',
    '2010a653',
    '8690b3ff',
    '96591fe8',
    'a52d6998',
    '04808f8b',
    'b770cd92',
    '82bc9627',
    '405b79af',
    'b4d84a85',
    'c322e9df']

    #for k in keys:
    k = args.key
    I = bucket.list(prefix = k)
    L = list(I)

    for _ in L:
        key = bucket.lookup(_)
        # prints the object name and its size
        print key.name, key.size
        """
        if 'poseFull.ama' in str(key.name):
            print str(key.name)
        else:
            'bar'
        """

if __name__ == "__main__":
    main()
